import os
import subprocess

import pandas as pd
import json

from AnalysisModule.helper import get_call_with_parmeters
from AnalysisModule.helper import is_filetype_supported
from AnalysisModule.helper import is_fortran_file

from AnalysisModule.MPIAnalysisModule.MPIAPIParameters import mpi_api_dict

# basically everything where new is in the parameter names
# meaning functions where new mpi handles are created
duplicates_allowed = ["DATATYPE", "COMMUNICATOR", "GROUP", "RANK"]

# suppresions to consider:
suppression_set = ['DUMMY_ITEM_NOTHING_IS_SUPPRESSED', 'f08_parameter', 'f90_parameter', 'c_parameter', 'lis_parameter']


# clöass that analyzes a single mpi call
class SingleMPICallAnalysis:
    __slots__ = ('_mpi_func', '_allowed_num_params', '_is_vararg')

    def __init__(self, func, is_vararg, allowed_num_params):
        self._mpi_func = func
        self._is_vararg = is_vararg
        self._allowed_num_params = allowed_num_params

    def is_call_matching(self, call):
        # fortran will be normalized to all upeprcase
        return call == self._mpi_func or call == self._mpi_func.upper() or call == self._mpi_func + "_c"

    def analyze_call(self, src_location, src_location_line, call_with_params):
        assert self.is_call_matching(call_with_params[0])
        # pos 0 is the call
        params = call_with_params[1:]

        num_params = len(params)
        try:
            if num_params not in self._allowed_num_params:
                if self._is_vararg:
                    min_non_vararg = min(self._allowed_num_params)
                    if num_params < min_non_vararg:
                        raise Exception("Unexpected number of parameters", call_with_params[0])
                    else:
                        # dont record the varargs
                        num_params = min_non_vararg
                else:
                    raise Exception("Unexpected number of parameters", call_with_params[0])

            bool_mask = self._allowed_num_params[num_params][0]
            df_columns = self._allowed_num_params[num_params][1]

            used_params = [p for i, p in enumerate(params) if len(bool_mask) > i and bool_mask[i]]

            results = pd.DataFrame(
                columns=['src_location', 'src_location_line_number', 'call', 'analysis_successful'] + df_columns)
            field = [src_location, src_location_line, self._mpi_func, True] + used_params
            results.loc[len(results)] = field

        except Exception as e:
            # failed Analysis: skip results
            # print("error during analysis")
            # traceback.print_exc()
            results = pd.DataFrame(
                columns=['src_location', 'src_location_line_number', 'call', 'analysis_successful'])
            field = [src_location, src_location_line, self._mpi_func, False]
            results.loc[len(results)] = field
        return results


# class that manages the analysis of all mpi calls
class MPICallAnalysis:
    __slots__ = ('_call_analyses')

    def __init__(self):

        self._call_analyses = []

        for mpi_func, info in mpi_api_dict.items():
            a = SingleMPICallAnalysis(mpi_func, info[0], info[1])
            self._call_analyses.append(a)

    def __call__(self, repo):
        repoPath = repo.repoPath
        results = pd.DataFrame()

        for root, dirs, files in os.walk(repoPath):
            for name in files:
                this_file = os.path.join(root, name)

                pre_processed = ""
                if is_filetype_supported(this_file):
                    try:
                        grep_res = subprocess.check_output(f'grep -I -m 1 ".*MPI.*" {this_file}', shell=True, text=True)
                        # grep returns with an error code, if no match ws found
                        pre_processed = repo.get_normalized_file_content(this_file)
                    except subprocess.SubprocessError as e:
                        pass
                is_fortran = is_fortran_file(this_file)
                lines = [l.strip() for l in pre_processed.splitlines()]
                for i, l in enumerate(lines):
                    try:
                        if not is_fortran or 'CALL' in l.upper():
                            # otherwise it is a fortran declaration
                            call_with_params = get_call_with_parmeters(l)
                            if call_with_params:
                                for analysis in self._call_analyses:
                                    if analysis.is_call_matching(call_with_params[0]):
                                        analysis_result = analysis.analyze_call(this_file, i, call_with_params)
                                        results = pd.concat((results, analysis_result), axis=0, ignore_index=True)
                    except Exception:
                        # skip if non-correct call was found
                        pass

        return results
