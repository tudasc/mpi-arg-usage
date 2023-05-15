import pandas
import pandas as pd
import tqdm
import traceback

import multiprocessing as mp

import os

from AnalysisModule.repository import Repository


# This dummy class shows the Properties an analysis object must have to serve as a reference
class DummyAnalysis:

    # def __init__(self):
    # one may need a constructor

    # the call method will be invoked by the analysis manager to run the ananlysis on the given repo
    # returns a pandas dataframe with the resulting data for this repo
    # the index of the dataframe is not important and will be ignored anyway
    def __call__(self, repo):
        return pd.DataFrame(columns=["Dummy_Metric1", "Dummy_Metric2"], data=[[0, 0], [1, 1]])


# helper for running an analysis
def run_analysis_on_repo_single_arg(args):
    return run_analysis_on_repo(args[0], args[1], args[2], args[3], args[4], args[5])


def run_analysis_on_repo(index, row, repopath, refresh_repos, analyses, keep_repo=True):
    output_df = pandas.DataFrame()
    repo = Repository(repoName=row['Code'], repoUrl=row['URL'], repo_type=row['Type'],
                      repoPath=repopath + '/' + row['Code'], keep_repo=keep_repo)
    this_repo_result_file = repopath + '/' + row['Code'] + '.csv'
    repo.cloneRepo(refresh_repos)
    if (not refresh_repos) and os.path.isfile(this_repo_result_file):
        output_df = pd.read_csv(this_repo_result_file, header=0)
    else:
        if repo.is_supported:
            for analysis in analyses:
                analysis_result = analysis(repo)
                analysis_result['Code'] = row['Code']
                output_df = pd.concat((output_df, analysis_result), axis=0, ignore_index=True)
            # finished analysis
            output_df.to_csv(this_repo_result_file)
        else:
            pass
            # no analysis
    return output_df


# manages all analysis done for a repo
class AnalysisManager:
    __slots__ = ('_analyses', '_outfile', '_keep_repos', '_repopath', '_refresh_repos')

    def __init__(self, outfile, repopath, refresh_repos=False, keep_repos=True, analyses=[]):
        self._analyses = analyses
        self._outfile = outfile
        assert os.path.isdir(repopath) and "The path where the repositories should be downloaded to must exist"
        self._repopath = repopath
        self._refresh_repos = refresh_repos
        self._keep_repos = keep_repos

    def register_analysis(self, analysis):
        self._analyses.append(analysis)

    # perform the analyses
    def __call__(self, input_df):
        output_df = pandas.DataFrame()

        with mp.Pool() as pool:
            param_list = [(index, row, self._repopath, self._refresh_repos, self._analyses, self._keep_repos) for
                          index, row in
                          input_df.iterrows()]
            output_dfs = list(tqdm.tqdm(pool.imap_unordered(run_analysis_on_repo_single_arg, param_list),
                                        total=len(param_list)))

            for o in output_dfs:
                output_df = pd.concat((output_df, o), axis=0, ignore_index=True)

        output_df.to_csv(self._outfile, index=False)

        return output_df.infer_objects()
