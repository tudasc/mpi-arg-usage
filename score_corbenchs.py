#!/usr/bin/env python3
# coding: utf-8

from ScoringModule.ScoringTable import get_scoring_table
from ScoringModule.ScoringTable import use_scoring_table
from ScoringModule.ScoringTable import calls_to_exclude
from AnalysisModule.MPIAnalysisModule.MPIAPICategories import mpi_categories_for_scoring
from AnalysisModule.MPIAnalysisModule.MPIAPICategories import mpi_all_mpi
from AnalysisModule.PostProcessModule.post_process import post_process_data

import argparse
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

sns.set_theme()
plt.rcParams['axes.facecolor'] = 'white'
plt.rc('pdf', fonttype=42)


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_prefix', default='./',
                        help='prefix (Path) for all the resulting plots')
    parser.add_argument('--input', default='output.csv',
                        help='name of the input data')
    parser.add_argument('--cobe', default='merged_cobe.csv',
                        help='data for MPI-Corrbench')
    parser.add_argument('--mbi', default='merged_mbi.csv',
                        help='data for MpiBugsInitiative')
    parser.add_argument('--mbb', default='mbb.csv',
                        help='data for MpiBugBench')

    return parser.parse_args()


def get_scoresheet_overview_plot(score_table, prefix):
    cat_to_use = mpi_categories_for_scoring.copy()

    cat_to_use.pop('Persistent', None)
    cat_to_use.pop('Process-Mgmt', None)

    scored_so_far = set(item for sublist in cat_to_use.values() for item in sublist)
    cat_to_use['Other'] = mpi_all_mpi - scored_so_far

    # custom order for better readability of the plotr
    custom_order = [
        'Other',
        'RMA',
        'Comm Group',
        'Types',
        'Topology',
        'File',
        'blocking\nPtP',
        'non-blocking\nPtP',
        'Reduction',
        'Collective',
    ]

    scores_per_cat = pd.DataFrame()
    for cat in custom_order:
        # for cat, members in cat_to_use.items():
        members = cat_to_use[cat]
        scores_per_cat[cat] = score_table[score_table["call"].isin(members)].sum(numeric_only=True)

    print(scores_per_cat.loc["score"].sum())
    above = False
    y_sep_list = [0.05, 0.05, 0.20, 0.2]
    i = 0
    ax = pd.DataFrame(scores_per_cat.loc["score"]).T.plot.barh(stacked=True, figsize=(8, 2), legend=False,
                                                               edgecolor="black")
    ax.set_ylabel('')
    ax.set_yticklabels([])
    ax.set_xlabel('% Score Contribution')
    for bar in ax.containers:
        label = bar.get_label()
        for rect in bar.patches:
            if rect.get_width() > 0:
                if label == "coll":
                    label = "other Collectives"
                if label == "blocking\nPtP":
                    label = "blocking\n    PtP"
                if label == "nonblocking\nPtP":
                    label = "nonblocking\n       PtP"
                txt = ax.text(rect.get_x(), rect.get_y() + 0.2, label, weight='bold')
                # as datsa coordinates
                text_coords = ax.transData.inverted().transform(txt.get_window_extent())
                txt_width = text_coords[1][0] - text_coords[0][0]
                txt_height = text_coords[1][1] - text_coords[0][1]
                center_y = rect.get_y() + rect.get_height() / 2 - txt_height / 2
                center_x = rect.get_x() + rect.get_width() / 2 - txt_width / 2
                if rect.get_width() > txt_width:
                    # text fits'
                    txt.set_position((center_x, center_y))
                else:
                    y_sep = y_sep_list[i % len(y_sep_list)]
                    if label == "nonblocking\n       PtP":
                        y_sep = 0.05
                    if above:
                        y = rect.get_y() + rect.get_height() + y_sep
                        ax.plot([center_x + txt_width / 2, rect.get_x() + rect.get_width() / 2],
                                [y, rect.get_y() + rect.get_height()], color='gray', linestyle='-', linewidth=2)
                    else:
                        y = rect.get_y() - y_sep - txt_height
                        ax.plot([center_x + txt_width / 2, center_x + txt_width / 2], [y + txt_height, rect.get_y()],
                                color='gray',
                                linestyle='-', linewidth=2)
                    above = not above
                    i = i + 1
                    txt.set_position((center_x, y))
                pass

    ax.grid(which='major', axis='x', color='gray', linestyle='--', linewidth=1)
    plt.savefig(prefix + "category_scores.pdf", bbox_inches='tight')


def get_radar_plot(series_lapel_list, title, prefix):
    sns.set_style("whitegrid")
    from numpy import pi
    plt.clf()

    # ------- PART 1: Create background
    # number of variable
    categories = list(series_lapel_list[0][0].index)
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True, )

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories, color='black')
    for lab, rot in zip(ax.get_xticklabels(), angles[:-1]):
        if rot <= pi:
            lab.set_horizontalalignment("left")
        else:
            lab.set_horizontalalignment("right")

    # ax.tick_params(axis='x', rotation=5.5)
    # ax.tick_params(pad=123)

    # Draw ylabels
    ax.set_rlabel_position(0)
    ax.set_yticklabels([])
    plt.ylim(0, 1)

    # ------- PART 2: Add plots
    # Plot each individual = each line of the data
    # I don't make a loop, because plotting more than 3 groups makes the chart unreadable

    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    c1 = "#DD8452"
    c2 = "#4C72B0"
    c3 = "#228833"

    for (series, label), color in zip(series_lapel_list, [c1, c2, c3]):
        values = series.tolist()
        values += values[:1]
        ax.plot(angles, values, color=color, linewidth=1, linestyle='solid', label=label)
        ax.fill(angles, values, color=color, alpha=0.1)

    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.2, 1.15))
    plt.title = (title)

    plt.tight_layout()

    # Show the graph
    plt.savefig(prefix + title + ".pdf", bbox_inches='tight')


def get_scores_per_cat(df):
    mpi_categories_for_plotting = mpi_categories_for_scoring.copy()
    mpi_categories_for_plotting.pop('File', None)
    mpi_categories_for_plotting.pop('Process-Mgmt', None)

    scored_so_far = set(item for sublist in mpi_categories_for_plotting.values() for item in sublist)
    mpi_categories_for_plotting['Other'] = mpi_all_mpi - scored_so_far

    scores_per_call = df.groupby("call").sum(['score', 'achieved_score'])
    scores_per_cat = pd.DataFrame()
    for cat, members in mpi_categories_for_plotting.items():
        members_to_use = [m for m in members if m in scores_per_call.index]
        scores_per_cat[cat] = scores_per_call.loc[members_to_use].sum(numeric_only=True)
    return scores_per_cat


def get_missed_per_category(df):
    mpi_categories_for_plotting = mpi_categories_for_scoring.copy()
    # mpi_categories_for_plotting.pop('io', None)
    # mpi_categories_for_plotting.pop('processmgmt', None)

    scored_so_far = set(item for sublist in mpi_categories_for_plotting.values() for item in sublist)
    mpi_categories_for_plotting['Other'] = mpi_all_mpi - scored_so_far

    scores_per_call = df.groupby("call").sum(['score', 'achieved_score'])
    scores_per_call["not_covered"] = scores_per_call["achieved_score"] == 0
    result = pd.DataFrame(columns=["acheived_score", "partially_covered_score", "not_covered_score"])
    mpi_categories_for_plotting = mpi_categories_for_scoring.copy()
    scored_so_far = set(item for sublist in mpi_categories_for_plotting.values() for item in sublist)
    mpi_categories_for_plotting['Other'] = mpi_all_mpi - scored_so_far
    for cat, members in mpi_categories_for_plotting.items():
        members_to_use = [m for m in members if m in scores_per_call.index]

        sum_score = 0.0
        sum_not_covered_score = 0.0
        sum_partly_covered_score = 0.0
        for m in members_to_use:
            this_call = scores_per_call.loc[m]
            if this_call["not_covered"]:
                sum_not_covered_score += this_call["score"]
            else:
                sum_score += this_call["achieved_score"]
                sum_partly_covered_score += (this_call["score"] - this_call["achieved_score"])
        result.loc[cat] = [sum_score, sum_partly_covered_score, sum_not_covered_score]
    return result


def plot_missed_score(df_correct, df_faulty, fname):
    df_correct = get_missed_per_category(df_correct)
    df_faulty = get_missed_per_category(df_faulty)
    # scale to 100% per cat and plot
    sum_per_cat_f = df_faulty.sum(axis=1)
    sum_per_cat_c = df_correct.sum(axis=1)

    df_faulty.iloc[:, :] = df_faulty.iloc[:, :].div(sum_per_cat_f, axis=0)
    df_correct.iloc[:, :] = df_correct.iloc[:, :].div(sum_per_cat_c, axis=0)

    index_to_use = [i.replace("\n", " ") for i in df_faulty.index]

    width = 0.2
    sep = 0.6
    index_to_use = df_correct.index
    fig, ax = plt.subplots(figsize=(8, 4))
    pos_list = []
    label_list = []
    # colors = sns.color_palette("tab10").as_hex()
    # colors = list(reversed(colors[0:3]))
    colors = ["#55A868", "#DD8452", "#4C72B0"]
    for i, label in enumerate(index_to_use):
        v = df_faulty.loc[label].values
        assert len(v) == 3
        pos = sep * i
        ax.bar(x=pos, height=v[0], width=width, bottom=0, color=colors[0])
        ax.bar(x=pos, height=v[1], width=width, bottom=v[0], color=colors[1])
        ax.bar(x=pos, height=v[2], width=width, bottom=v[0] + v[1], color=colors[2])
        v = df_correct.loc[label].values
        assert len(v) == 3
        ax.bar(x=pos + width, height=v[0], width=width, bottom=0, color=colors[0])
        ax.bar(x=pos + width, height=v[1], width=width, bottom=v[0], color=colors[1])
        ax.bar(x=pos + width, height=v[2], width=width, bottom=v[0] + v[1], color=colors[2])  #
        pos_list.append(pos + width / 2)
        label_list.append(label.replace("\n", " "))

    # dummy for legend
    ax.bar(0, 0, color=colors[0], label="achieved score")
    ax.bar(0, 0, color=colors[1], label="partially missed")
    ax.bar(0, 0, color=colors[2], label="not covered")
    ax.set_xticks(pos_list, label_list, rotation=45, ha='right', rotation_mode='anchor')
    ax.grid(which='major', axis='y', color='gray', linestyle='--', linewidth=1)
    plt.legend(loc="upper left", bbox_to_anchor=(0.95, 1))

    plt.savefig(fname + ".pdf", bbox_inches='tight')


def main():
    args = parseArgs()

    df_full = pd.read_csv(args.input, header=0, low_memory=False)
    df_cobe = pd.read_csv(args.cobe, header=0, low_memory=False)
    df_mbi = pd.read_csv(args.mbi, header=0, low_memory=False)
    df_mbb_raw = pd.read_csv(args.mbb, header=0, low_memory=False)
    df_mbb = post_process_data(df_mbb_raw, True)

    # in the mbi repo, there are other codes (e.g. the tools or the blueprints to generate the gencodes)
    # but only the gencodes are testcases
    df_mbi = df_mbi[df_mbi["src_location"].str.contains("gencodes")]

    # we exclude some calls like MPI init form scoring as they are of no relevancy for our purpose
    df_mbi = df_mbi[~df_mbi["call"].isin(calls_to_exclude)]
    df_cobe = df_cobe[~df_cobe["call"].isin(calls_to_exclude)]

    print("build scoring table")
    score_table = get_scoring_table(df_full)
    get_scoresheet_overview_plot(score_table, args.output_prefix)

    print("score corrbenchs (9 different configs)")
    result_cobe_correct = use_scoring_table(df_cobe[df_cobe["src_location"].str.contains("correct")], score_table)
    result_cobe_faulty = use_scoring_table(df_cobe[~df_cobe["src_location"].str.contains("correct")], score_table)
    result_mbi_correct = use_scoring_table(df_mbi[df_mbi["src_location"].str.contains("ok.c")], score_table)
    result_mbi_faulty = use_scoring_table(df_mbi[df_mbi["src_location"].str.contains("nok.c")], score_table)

    result_mbb_faulty = use_scoring_table(~df_mbb[df_mbb["src_location"].str.contains("Correct-")], score_table)
    result_mbb_correct = use_scoring_table(df_mbb[df_mbb["src_location"].str.contains("Correct-")], score_table)

    result_cobe_full = use_scoring_table(df_cobe, score_table)
    result_mbi_full = use_scoring_table(df_mbi, score_table)
    result_mbb_full = use_scoring_table(df_mbb, score_table)

    print("Final Scores:")
    print("\tfaulty\tcorrect\tall")
    print("MBB\t%.2f\t%.2f\t%.2f" % (
        result_cobe_faulty["achieved_score"].sum(), result_cobe_correct["achieved_score"].sum(),
        result_cobe_full["achieved_score"].sum()))
    print("MBI\t%.2f\t%.2f\t%.2f" % (
        result_mbi_faulty["achieved_score"].sum(), result_mbi_correct["achieved_score"].sum(),
        result_mbi_full["achieved_score"].sum()))
    print("MBB\t%.2f\t%.2f\t%.2f" % (
    result_mbb_faulty["achieved_score"].sum(), result_mbb_correct["achieved_score"].sum(),
    result_mbb_full["achieved_score"].sum()))
    print("of %.2f maximum" % score_table["score"].sum())

    plot_missed_score(result_cobe_correct, result_cobe_faulty, "missed_score_cobe")
    plot_missed_score(result_mbi_correct, result_mbi_faulty, "missed_score_mbi")

    # aggregate per category
    result_cobe_correct = get_scores_per_cat(result_cobe_correct)
    result_cobe_faulty = get_scores_per_cat(result_cobe_faulty)
    result_mbi_correct = get_scores_per_cat(result_mbi_correct)
    result_mbi_faulty = get_scores_per_cat(result_mbi_faulty)
    result_mbb_correct = get_scores_per_cat(result_mbb_correct)
    result_mbb_faulty = get_scores_per_cat(result_mbb_faulty)

    get_radar_plot([(result_mbi_correct.loc["achieved_score"] / result_mbi_correct.loc["score"], "MBI"),
                    (result_cobe_correct.loc["achieved_score"] / result_cobe_correct.loc["score"], "COBE"),
                    (result_mbb_correct.loc["achieved_score"] / result_mbb_correct.loc["score"], "MBB")],
                   "Correct_testcases", args.output_prefix)

    get_radar_plot([(result_mbi_faulty.loc["achieved_score"] / result_mbi_faulty.loc["score"], "MBI"),
                    (result_cobe_faulty.loc["achieved_score"] / result_cobe_faulty.loc["score"], "COBE"),
                    (result_mbb_faulty.loc["achieved_score"] / result_mbb_faulty.loc["score"], "MBB")],
                   "Faulty_testcases", args.output_prefix)


if __name__ == "__main__":
    main()
