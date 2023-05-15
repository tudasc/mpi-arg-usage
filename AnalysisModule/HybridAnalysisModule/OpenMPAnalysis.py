import pandas as pd

from AnalysisModule.helper import get_preliminary_grep


class OpenmpAnalysis:
    # __slots__ = ('_query', '_type_arg_nun')

    def __init__(self):
        pass

    def __call__(self, repo):
        repoPath = repo.repoPath

        results = pd.DataFrame(
            columns=['src_location', 'src_location_line_number', 'call', 'openmp_pragma_used'])

        grep_res = get_preliminary_grep(repoPath, "omp")

        # set comprehension: remove duplicate filenames
        files = {r[0] for r in grep_res}
        for f in files:
            try:
                normalized = repo.get_normalized_file_content(f)
                for i, l in enumerate(normalized.splitlines()):
                    if l.startswith("#pragma omp"):
                        row = [f, i, "openmp", l[11:]]
                        results.loc[len(results)] = row
                    if l.startswith("!$OMP") or l.startswith("!$omp"):
                        row = [f, i, "openmp", l[5:]]
                        results.loc[len(results)] = row

            except Exception as e:
                pass

        return results
