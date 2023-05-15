#!/usr/bin/env python3
# coding: utf-8

from AnalysisModule.analysismanager import AnalysisManager

from AnalysisModule.MPIAnalysisModule.CallAnalysis import MPICallAnalysis
from AnalysisModule.DefineAnalysis import DefineAnalysis
from AnalysisModule.HybridAnalysisModule.OpenMPAnalysis import OpenmpAnalysis
from AnalysisModule.HybridAnalysisModule.OpenACCAnalysis import OpenaccAnalysis
from AnalysisModule.HybridAnalysisModule.CudaAnalysis import CudaAnalysis
from AnalysisModule.HybridAnalysisModule.CudaAnalysis import OpenCLAnalysis

from AnalysisModule.PostProcessModule.post_process import post_process_data

import argparse
import pandas as pd
import os


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='output.csv',
                        help='result data')
    parser.add_argument('--intermediate', default='intermediate.csv',
                        help='intermediate "raw" data before cross-referencing')
    parser.add_argument('--code_locations', default='code_locations.csv',
                        help='name of the csv file, where the repository urls are located')
    parser.add_argument('--repo_path', default='repositories',
                        help='Path where all the repositories should be downloaded to')
    parser.add_argument('--refresh_repos', action='store_true',
                        help='Re download all repositories and re-fresh their analysis results')
    parser.add_argument('--delete_repos', action='store_true',
                        help='Delete all repositories after analysis')

    return parser.parse_args()


def main():
    args = parseArgs()

    # create dir where the repositories will bbe downloaded to
    if not os.path.isdir(args.repo_path):
        os.mkdir(args.repo_path)

    # set up the Analysis Manager handeling all the analysis
    repoAnalyzer = AnalysisManager(args.intermediate, args.repo_path, args.refresh_repos, not args.delete_repos)

    repoAnalyzer.register_analysis(MPICallAnalysis())
    repoAnalyzer.register_analysis(DefineAnalysis())
    repoAnalyzer.register_analysis(OpenmpAnalysis())
    repoAnalyzer.register_analysis(OpenaccAnalysis())
    repoAnalyzer.register_analysis(OpenCLAnalysis())
    repoAnalyzer.register_analysis(CudaAnalysis())

    # read in the code location information
    df = pd.read_csv(args.code_locations, header=0)

    # run Analysis
    intermediate_result_df = repoAnalyzer(df)
    # intermediate results will be written by the analysis Manager

    print("Repository Analysis Complete")

    result_df = post_process_data(intermediate_result_df)
    result_df.to_csv(args.output, index=False)

    print(f"Result file written: {args.output}")


if __name__ == "__main__":
    main()
