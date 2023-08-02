import pandas as pd
import numpy as np

from tqdm.auto import tqdm

tqdm.pandas()

from AnalysisModule.MPIAnalysisModule.MPIAPICategories import mpi_all_mpi

# Settings
categories_to_score = ["RANK", "TAG", "POLYXFER_NUM_ELEM_NNI", "DATATYPE", "COMMUNICATOR", "OPERATION"]

# maximum total score
maximum_score = 100
# maximum score per call
maximum_call_score = 1

# calls to completely ignore while scoring
# ALL Programs must use MPI init, using it for scoring is therefore not that useful
calls_to_exclude = ["MPI_Comm_rank", "MPI_Comm_size", "MPI_Init", "MPI_Finalize", "MPI_Init_thread"]

# end settings
max_call_weight = float(maximum_score) / float(maximum_call_score)


# replace value with other to use as wildcard
def clean_data_to_score(row, categories_to_score):
    for c in categories_to_score:
        cc = c + "_CATEGORY"
        if not pd.isna(row[c]):
            if row[cc] not in ["MPI_constant", "literal_constant", "handle"]:
                row[c] = "other"
            if row[c] == "inconclusive":
                row[c] = "other"
            if c == "TAG" and row[c] != "MPI_ANY_TAG":
                # discard all tag values besides the one with special meanings
                row[c] = "other"
    return row


def get_scoring_table(df):
    df = df[~df["call"].isin(calls_to_exclude)]
    columns = ["call"] + categories_to_score + ["score"]
    num_categories = len(categories_to_score)
    types = [pd.StringDtype] + [pd.StringDtype for _ in range(num_categories)] + [np.float64]

    scoring_table = pd.DataFrame(columns=columns)

    call_weights = {}
    # other ist ein wildcard, der alles matcht

    # there may also be openmp, cuda etc. in the data
    df_only_mpi = df[df["call"].isin(mpi_all_mpi)].apply(clean_data_to_score, args=(categories_to_score,), axis=1)
    total_calls = float(len(df_only_mpi))

    for call, count in df_only_mpi["call"].value_counts().items():
        call_weights[call] = (float(count) / total_calls) * max_call_weight

    for call, this_call_weight in tqdm(call_weights.items()):
        if num_categories == 0:
            scoring_table.loc[len(scoring_table)] = [call, this_call_weight]
        else:
            this_call_only = df_only_mpi[df_only_mpi["call"] == call][categories_to_score]
            unique_calls_to_this = (
                # drops all NA but disregards the cols where all values are NA (e.g. the param is not used in this call
                # but all other NA values (wrong reading of calls) are discarded
                this_call_only.dropna(subset=this_call_only.columns[~this_call_only.isnull().all()], how='any')
                .groupby(categories_to_score, as_index=False, dropna=False).size()
            )
            total_calls_to_this_mpi_func = unique_calls_to_this['size'].sum()

            for _, row in unique_calls_to_this.iterrows():
                score = this_call_weight * float(maximum_call_score) * float(row['size']) / float(
                    total_calls_to_this_mpi_func)
                scoring_table.loc[len(scoring_table)] = [call] + row[categories_to_score].tolist() + [score]

    return scoring_table


def score_row(row, df_to_score):
    matching_selection = df_to_score[df_to_score["call"] == row["call"]]
    for c in categories_to_score:
        if not (pd.isna(row[c]) or row[c] == "other"):
            matching_selection = matching_selection[matching_selection[c] == row[c]]

    if len(matching_selection) > 0:
        row["achieved_score"] = row["score"]
    else:
        row["achieved_score"] = 0

    return row


def use_scoring_table(df_to_score, scoring_table):
    return scoring_table.progress_apply(score_row, axis=1, args=(df_to_score,))


def score_row_reverse(row, scoring_table):
    matching_selection = scoring_table[scoring_table["call"] == row["call"]]
    for c in categories_to_score:
        if not (pd.isna(row[c]) or row[c] == "other"):
            matching_selection = matching_selection[
                (matching_selection[c] == row[c]) | (matching_selection[c] == "other")]

    if len(matching_selection) == 1:
        row["achieved_score"] = matching_selection["score"].iloc[0]
    elif len(matching_selection) == 0:
        row["achieved_score"] = pd.NA
    else:
        # TODO one should use the most specific match
        # but for our analysis, we dont care about the correct score, we rather care about the rows not scored
        # the correct score is given in the non-reverse mode
        row["achieved_score"] = matching_selection["score"].iloc[0]
    return row


def use_scoring_table_reverse(df_to_score, scoring_table):
    return df_to_score.progress_apply(score_row_reverse, axis=1, args=(scoring_table,))
