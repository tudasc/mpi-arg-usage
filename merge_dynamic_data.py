#!/usr/bin/env python3
# coding: utf-8
import warnings

from tqdm.auto import tqdm

from AnalysisModule.analysismanager import AnalysisManager

from AnalysisModule.MPIAnalysisModule.CallAnalysis import MPICallAnalysis
from AnalysisModule.DefineAnalysis import DefineAnalysis
from AnalysisModule.HybridAnalysisModule.OpenMPAnalysis import OpenmpAnalysis
from AnalysisModule.HybridAnalysisModule.OpenACCAnalysis import OpenaccAnalysis
from AnalysisModule.HybridAnalysisModule.CudaAnalysis import CudaAnalysis
from AnalysisModule.HybridAnalysisModule.CudaAnalysis import OpenCLAnalysis

from AnalysisModule.PostProcessModule.post_process import post_process_data

from ScoringModule.ScoringTable import get_scoring_table

import argparse
import pandas as pd
import os

dynamic_csv_header = ["call", "RANK", "TAG", "POLYXFER_NUM_ELEM_NNI", "DATATYPE", "COMMUNICATOR", "OPERATION",
                      "newCOMMUNICATOR", "newDATATYPE", "src_location", "target-function", "src_location_line_number"]


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='merged.csv',
                        help='result data')
    parser.add_argument('--input_static', default='output_static.csv',
                        help='name of the input data')
    parser.add_argument('--input_dynamic', default='output_dynamic.csv',
                        help='name of the input data')

    return parser.parse_args()


def read_dynamic_data(filename):
    df = pd.read_csv(filename, header=None, names=dynamic_csv_header, low_memory=False).drop_duplicates()
    return df


def get_canonical_src_loc(loc, remove_prefixes=[]):
    if pd.isna(loc):
        return loc

    for prefix in remove_prefixes:
        if loc.startswith(prefix):
            return loc[len(prefix) + 1:]

    return loc


def merge_static_with_dynamic(df_static, df_dynamic):
    with warnings.catch_warnings():
        # suppress the FutoreWarning when concatenating a Dataframe
        warnings.simplefilter(action='ignore', category=FutureWarning)
        result_df = pd.DataFrame(columns=df_static.columns)
        # TODO parallelize
        for index, row in tqdm(df_static.iterrows(), total=df_static.shape[0]):
            mask = ((df_dynamic['call'].str.strip() == row['call'].strip()) & (
                    df_dynamic['src_location'].str.strip() == row['src_location'].strip()) & (
                            df_dynamic['src_location_line_number'] == row['src_location_line_number']))
            matching = df_dynamic[mask]
            # row["matching_len"]=len(matching)
            if len(matching) > 0:
                df_static.loc[index, "merged"] = 1
                df_dynamic.loc[mask, "merged"] = 1
                all_same = pd.Series(data=False,
                                     index=["RANK", "TAG", "POLYXFER_NUM_ELEM_NNI", "DATATYPE", "COMMUNICATOR",
                                            "OPERATION"])
                for c in ["RANK", "TAG", "POLYXFER_NUM_ELEM_NNI", "DATATYPE", "COMMUNICATOR", "OPERATION"]:
                    val = matching[c].iloc[0]
                    if (matching[c] == val).all():
                        all_same[c] = True
                for _, matched_row in matching.iterrows():
                    new_row = row.copy()
                    for c in ["RANK", "TAG", "POLYXFER_NUM_ELEM_NNI", "DATATYPE", "COMMUNICATOR", "OPERATION"]:
                        c_cat = c + "_CATEGORY"
                        new_row[c] = matched_row[c]
                        if all_same[c]:
                            new_row[c_cat] = new_row[c_cat] + ",RUNTIME_VALUE"
                        else:
                            new_row[c_cat] = new_row[c_cat] + ",RUNTIME_DIFFERENT_VALS"
                    result_df.loc[len(result_df)] = new_row
            else:
                result_df.loc[len(result_df)] = row

        print(("Static: %d of %d" % (df_static["merged"].sum(), len(df_static))))
        print(("Dynamic: %d of %d" % (df_dynamic["merged"].sum(), len(df_dynamic))))
        # for debugging to check which lines have not matched
        # df_static.to_csv("merging_static_debug.csv")
        # df_dynamic.to_csv("merging_dynamic_debug.csv")

        return result_df


def main():
    args = parseArgs()

    # df_static = pd.read_csv(args.input_static, header=0)
    df_static = post_process_data(pd.read_csv(args.input_static, header=0))
    df_dynamic = read_dynamic_data(args.input_dynamic)

    remove_prefixes = sorted([os.path.commonpath(df_static['src_location'].tolist()),
                              os.path.commonpath(df_dynamic['src_location'].tolist())], key=len, reverse=True)

    print("Path prefixes:")
    print(remove_prefixes)

    # TODO better path matching?
    remove_prefixes = [r.replace("/gencodes", "") for r in remove_prefixes]
    print("Patched Path prefixes:")
    print(remove_prefixes)

    df_static["src_location"] = df_static["src_location"].transform(get_canonical_src_loc,
                                                                    remove_prefixes=remove_prefixes)
    df_dynamic["src_location"] = df_dynamic["src_location"].transform(get_canonical_src_loc,
                                                                      remove_prefixes=remove_prefixes)

    df_dynamic["merged"] = 0
    df_static["merged"] = 0

    print("Merging")
    df_merged = merge_static_with_dynamic(df_static, df_dynamic)

    df_merged.to_csv(args.output)


if __name__ == "__main__":
    main()
