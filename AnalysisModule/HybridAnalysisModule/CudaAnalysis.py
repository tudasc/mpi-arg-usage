import pandas as pd

from AnalysisModule.helper import get_preliminary_grep
import re


# regex from laguna paper
class CudaAnalysis:
    # __slots__ = ('_query', '_type_arg_nun')
    def __init__(self):
        pass

    def __call__(self, repo):
        repoPath = repo.repoPath

        results = pd.DataFrame(
            columns=['src_location', 'call', 'num_occurrences'])

        grep_res1 = get_preliminary_grep(repoPath, "__global__")
        grep_res2 = get_preliminary_grep(repoPath, "__device__")

        # set comprehension: remove duplicate filenames
        files = {r[0] for r in grep_res1 + grep_res2}
        for f in files:
            try:
                normalized = repo.get_normalized_file_content(f)
                cuda_global_kernel_re = re.compile(r"(?P<cuda_kernel>(__global__)[\s]+)")
                num_matches = len(re.findall(cuda_global_kernel_re, normalized))
                if num_matches > 0:
                    row = [f, "cuda_global_kernel", num_matches]
                    results.loc[len(results)] = row
                cuda_device_kernel_re = re.compile(r"(?P<cuda_kernel>(__device__)[\s]+)")
                num_matches = len(re.findall(cuda_device_kernel_re, normalized))
                if num_matches > 0:
                    row = [f, "cuda_device_kernel", num_matches]
                    results.loc[len(results)] = row

            except Exception as e:
                pass

        return results

    def get_count_for_call(self, call_with_params):
        # not found
        return pd.NA


class OpenCLAnalysis:
    # __slots__ = ('_query', '_type_arg_nun')
    def __init__(self):
        pass

    def __call__(self, repo):
        repoPath = repo.repoPath

        results = pd.DataFrame(
            columns=['src_location', 'call', 'num_occurrences'])

        grep_res1 = get_preliminary_grep(repoPath, "__global")
        grep_res2 = get_preliminary_grep(repoPath, "__kernel")

        # set comprehension: remove duplicate filenames
        files = {r[0] for r in grep_res1 + grep_res2}
        for f in files:
            try:
                normalized = repo.get_normalized_file_content(f)
                opencl_global_re = re.compile(r"(?P<opencl_global>(__global)[\s]+)")
                num_matches = len(re.findall(opencl_global_re, normalized))
                if num_matches > 0:
                    row = [f, "opencl_global", num_matches]
                    results.loc[len(results)] = row

                opencl_kernel_re = re.compile(r"(?P<cuda_kernel>(__kernel)[\s]+)")
                num_matches = len(re.findall(opencl_global_re, normalized))
                if num_matches > 0:
                    row = [f, "opencl_kernel", num_matches]
                    results.loc[len(results)] = row


            except Exception as e:
                pass

        return results
