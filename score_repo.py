#!/usr/bin/env python3
# coding: utf-8

from ScoringModule.ScoringTable import get_scoring_table
from ScoringModule.ScoringTable import use_scoring_table

import argparse
import pandas as pd
import os


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='output_scores.csv',
                        help='result data')
    parser.add_argument('--input', default='output.csv',
                        help='name of the input data')
    parser.add_argument('--to_score', default='merged.csv',
                        help='file with data for project to score')

    return parser.parse_args()


def main():
    args = parseArgs()

    df_full = pd.read_csv(args.input, header=0, low_memory=False)

    df_to_score = pd.read_csv(args.to_score, header=0, low_memory=False)
    print("build scoring table")
    score_table = get_scoring_table(df_full)
    print("allpy scoring table")
    result = use_scoring_table(df_to_score, score_table)

    result.to_csv(args.output)

    sum = result["achieved_score"].sum()
    max_sum = result["score"].sum()

    print("Total Score Acheived: {:.2f} (of {:.2f})".format(sum,max_sum))


if __name__ == "__main__":
    main()
