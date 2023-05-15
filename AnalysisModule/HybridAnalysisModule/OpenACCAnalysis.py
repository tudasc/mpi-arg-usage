import pandas as pd

from AnalysisModule.helper import get_preliminary_grep


class OpenaccAnalysis:
    # __slots__ = ('_query', '_type_arg_nun')

    def __init__(self):
        pass

    def __call__(self, repo):
        repoPath = repo.repoPath

        results = pd.DataFrame(
            columns=['src_location', 'src_location_line_number', 'call', 'openacc_pragma_used'])

        grep_res = get_preliminary_grep(repoPath, "acc")

        # set comprehension: remove duplicate filenames
        files = {r[0] for r in grep_res}
        for f in files:
            try:
                normalized = repo.get_normalized_file_content(f)
                for i, l in enumerate(normalized.splitlines()):
                    if l.startswith("#pragma acc"):
                        row = [f, i, "openacc", l[11:]]
                        results.loc[len(results)] = row
                    if l.startswith("!$ACC") or l.startswith("!$acc"):
                        row = [f, i, "openacc", l[5:]]
                        results.loc[len(results)] = row

            except Exception as e:
                pass

        return results
