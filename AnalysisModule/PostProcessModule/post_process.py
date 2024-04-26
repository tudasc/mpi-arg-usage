import pandas as pd
from tqdm.auto import tqdm
from pandarallel import pandarallel

from AnalysisModule.PostProcessModule.MPI_Versions import get_version_dict
from AnalysisModule.MPIAnalysisModule.MPIAPICategories import *


def post_process_data(df_raw, match_only_same_file=False):
    print("Post-Process-data")
    tqdm.pandas()
    pandarallel.initialize(progress_bar=True)

    print("Stage 1 of 7")
    # remove all leading/trailing whitespaces from string
    df_raw = df_raw.progress_applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # for the more expensive matching: usage of parallelism is beneficial
    print("Stage 2 of 7")
    defines_df = df_raw[df_raw['call'] == "#define"]
    defines_df = defines_df[['Code', 'src_location', 'define_value', 'defined_token']]
    df = df_raw.parallel_apply(get_definition, axis=1, args=(defines_df, match_only_same_file))
    # load balancing is bad

    # we dont want to analyze the defines
    df = df[df['call'] != "#define"]

    # try to match a corresponding type creation function for ech type used
    print("Stage 3 of 7")
    if 'DATATYPE' in df.columns and "newDATATYPE" in df.columns:
        df = df.parallel_apply(get_corresponding_creator, axis=1,
                               args=(df_raw, 'DATATYPE', 'newDATATYPE', False, match_only_same_file))
    print("Stage 4 of 7")
    if 'COMMUNICATOR' in df.columns and "newCOMMUNICATOR" in df.columns:
        df = df.parallel_apply(get_corresponding_creator, axis=1,
                               args=(df_raw, 'COMMUNICATOR', 'newCOMMUNICATOR', False, match_only_same_file))
    print("Stage 5 of 7")
    if 'GROUP' in df.columns and "newGROUP" in df.columns:
        df = df.parallel_apply(get_corresponding_creator, axis=1,
                               args=(df_raw, 'GROUP', 'newGROUP', False, match_only_same_file))
    print("Stage 6 of 7")
    version_dict = get_version_dict()
    df['version'] = df.progress_apply(get_version, axis=1, args=(version_dict,))
    print("Stage 7 of 7")
    for p in tqdm(df.columns):
        if p.isupper():
            df[p + '_CATEGORY'] = df.apply(get_category, axis=1, args=(p, df_raw))

    return df


def get_corresponding_creator(row, full_df, col, col_new, print_inconclusive=False, match_only_same_file=False):
    if not pd.isnull(row[col]):
        datatype = row[col].strip()
        if not re.fullmatch(is_mpi_builtin, datatype):
            select_matching_code = full_df[full_df['Code'] == row['Code']]
            if match_only_same_file:
                select_matching_code = select_matching_code[select_matching_code['src_location'] == row['src_location']]
            # the dtype creators take a pointer
            matching_types = [datatype, '&' + datatype]
            if datatype.startswith('*'):
                matching_types.append(datatype[1:])
            select_matching = select_matching_code[
                select_matching_code[col_new].isin(matching_types)]

            if len(select_matching) > 0:
                matches = True
                if len(select_matching) > 1:
                    if select_matching['call'].unique().size > 1:
                        if print_inconclusive:
                            print(f"\nInconclusive analysis result for type {datatype}")
                            print(select_matching[['Code', 'call', col, col_new]].head(10))
                        matches = False
                        row[col] = 'inconclusive'

                if matches:
                    matching_creator = select_matching['call'].iloc[0]
                    row[col] = matching_creator
            else:
                if row['call'] == "MPI_Type_commit":
                    print("NOT MATCHING:" + datatype)
                    #ASSERTION DID NOT TRIGGER: this part works correct
                    assert False
                pass
    return row


def get_definition(row, defines_df, match_only_same_file=False):
    if row["call"] != "#define":
        same_code = defines_df[defines_df['Code'] == row['Code']]
        if match_only_same_file:
            same_code = same_code[same_code['src_location'] == row['src_location']]

        row['params_by_define'] = []
        for index, value in row.items():
            if value != "" and not value in predefined_mpi_constants and index not in ['Code', 'src_location',
                                                                                       'src_location_line_number',
                                                                                       'call',
                                                                                       'analysis_successful',
                                                                                       'define_value', 'defined_token',
                                                                                       'params_by_define']:
                matching_defines = same_code[same_code['defined_token'] == value]
                if len(matching_defines) > 0:
                    row['params_by_define'] = row['params_by_define'] + [index]
                    # if larger than 1: define was inconclusive, but we at least know it is "by #define"
                if len(matching_defines) == 1:
                    # print(f"Fetched definition for {value}")
                    row[index] = matching_defines.iloc[0]['define_value']
                    # also encode the parameters given via define for later statistic

    return row


def get_category(row, param, df_raw):
    value = row[param]

    if pd.isna(value):
        return pd.NA

    if value in predefined_mpi_constants:
        return 'MPI_constant'
    try:
        as_int = int(value)
        return 'literal_constant'
    except ValueError as e:
        pass

    if value in mpi_type_creation_funcs + mpi_comm_group_funcs + mpi_group_creator_funcs:
        return 'handle'
    if value == 'inconclusive':
        return 'handle'

    # the expression should be formatted correctly, with whitespace around the operator
    # otherwise we will treat it like any other variable
    if any(op in value for op in [' * ', ' / ', ' + ', ' - ', '++', '--']):
        return 'arith_expression'

    if value.endswith(')'):
        if not '(' in value:
            print("WARNING: closing brace without opening brace in parameter: " + value)
        else:
            return 'function_call'

    if param in row['params_by_define']:
        return 'by_define'

    # other:
    if param == 'DATATYPE':
        if len(df_raw[(df_raw['Code'] == row['Code']) & df_raw['call'].isin(mpi_type_creation_funcs)]) > 0:
            return 'other_variable_creation_func_exist'
    if param == 'COMMUNICATOR':
        if len(df_raw[(df_raw['Code'] == row['Code']) & df_raw['call'].isin(mpi_comm_creator_funcs)]) > 0:
            return 'other_variable_creation_func_exist'
    if param == 'OPERATION':
        if len(df_raw[(df_raw['Code'] == row['Code']) & df_raw['call'].isin(['MPI_Op_create'])]) > 0:
            return 'other_variable_creation_func_exist'
    return 'other_variable'


def get_version(row, version_dict):
    call = row['call']
    if call in version_dict:
        return version_dict[call]
    elif call in ['#define', 'openmp', 'cuda_device_kernel', 'cuda_global_kernel', 'openacc', 'opencl_global',
                  'opencl_kernel']:
        # no mpi
        return "0.0"
    else:
        return "4.0"
    # dict does not contain 4.0 so we assume everything not present is 4.0
