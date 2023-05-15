#!/usr/bin/env python3
# coding: utf-8

# updates the code versions used

from AnalysisModule.repository import Repository

import argparse

import pandas as pd


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='output.csv',
                        help='resulting file with the versions')
    parser.add_argument('--code_locations', default='code_locations.csv',
                        help='name of the csv file, where the repository urls are located')

    return parser.parse_args()


def main():
    args = parseArgs()

    df = pd.read_csv(args.code_locations, header=0)

    df['SHA'] = df.apply(lambda row: Repository(repoName=row['Code'], repoUrl=row['URL'], repo_type=row['Type'],
                                                repoPath=args.repo_path + '/' + row['Code']).get_SHA(),
                         axis=1
                         )

    df.to_csv(args.output, index=False)

    print("Result file written")


if __name__ == "__main__":
    main()
