#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import argparse
import os

import matplotlib.pyplot as plt

from AnalysisModule.MPIAnalysisModule.MPIAPICategories import *

FONT_SIZE_LARGE = 16
FONT_SIZE_SMALLER = 14

# plt.style.use('seaborn-v0_8-notebook')
# plt.style.use('seaborn-v0_8-colorblind')
plt.style.use('seaborn-v0_8')

plt.rc('font', size=FONT_SIZE_LARGE)  # controls default text sizes
plt.rc('axes', labelsize=FONT_SIZE_SMALLER)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=FONT_SIZE_SMALLER)  # fontsize of the tick labels
plt.rc('ytick', labelsize=FONT_SIZE_SMALLER)  # fontsize of the tick labels

plt.rcParams['axes.facecolor'] = 'white'


def is_series_same(s):
    a = s.to_numpy()  # s.values (pandas<0.24)
    return (a[0] == a).all()


def get_num_type_usage_category_plots(df, output_dir):
    fig = plt.figure()

    num_type_uses = df[df['DATATYPE'].isin(mpi_type_creation_funcs + ['inconclusive'])]

    pivot_df_type_use_type = pd.pivot_table(num_type_uses, values='src_location', index='Code',
                                            columns='DATATYPE',
                                            aggfunc='count', fill_value=0)

    plt.clf()
    pivot_df_type_use_type.plot.bar(width=1, stacked=True, ax=fig.gca())
    plt.title(f'Number of calls using derived datatypes', color='black')
    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), title="Type was created by")
    plt.ylabel("Num Calls")
    plt.savefig(output_dir + "/num_types_used_by_type.pdf", bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.clf()

    pivot_df_type_use_call = pd.pivot_table(num_type_uses, values='src_location', index='Code',
                                            columns='call',
                                            aggfunc='count', fill_value=0)
    pivot_df_type_use_call.plot.bar(width=1, stacked=True, ax=fig.gca())
    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), title="Type was used in")
    plt.title(f'Number of calls using derived datatypes', color='black')
    plt.ylabel("Num Calls")
    plt.savefig(output_dir + "/num_types_used_by_call.pdf", bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.clf()

    num_type_creates = df[df['call'].isin(mpi_type_creation_funcs)]
    pivot_df_type_create = pd.pivot_table(num_type_creates, values='src_location', index='Code',
                                          columns='call',
                                          aggfunc='count', fill_value=0)

    pivot_df_type_create.plot.bar(width=1, stacked=True, ax=fig.gca())
    plt.title(f'Number of calls creating derived datatypes', color='black')
    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.ylabel("Num Calls")
    plt.savefig(output_dir + "/num_types_created_stacked.pdf", bbox_extra_artists=(lgd,), bbox_inches='tight')
    # TODO pandas warning here?
    num_type_uses = df[~df['DATATYPE'].isin(predefined_mpi_dtype_consants)].copy()
    num_type_uses['DATATYPE'].loc[
        ~num_type_uses['DATATYPE'].isin(mpi_type_creation_funcs + ['inconclusive'])] = 'indecidable-non-mpi'

    pivot_df_type_use_type = pd.pivot_table(num_type_uses, values='src_location', index='Code',
                                            columns='DATATYPE',
                                            aggfunc='count', fill_value=0)

    plt.clf()
    pivot_df_type_use_type.plot.bar(width=1, stacked=True, ax=fig.gca())
    plt.title(f'Number of calls using derived datatypes', color='black')
    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), title="Type was created by")
    plt.ylabel("Num Calls")
    plt.savefig(output_dir + "/num_types_used_by_type_with_undefined.pdf", bbox_extra_artists=(lgd,),
                bbox_inches='tight')
    plt.clf()


def plot_df(df, title, output_dir, angle=0, order=None, counter_clockwise=True, col_to_plot='plot_labels',
            use_pie=False):
    pivot_df = df.pivot_table(values='Code', index=col_to_plot, columns='call', aggfunc='count', fill_value=0)
    pivot_df_per_project = df.pivot_table(values='Code', index=col_to_plot, columns='call', aggfunc='nunique',
                                          fill_value=0)
    if order is None:
        order = pivot_df.index
    pivot_df = pivot_df.reindex(order)
    pivot_df_agg = pivot_df.agg("sum")
    pivot_df['overall'] = pivot_df.sum(axis=1)
    num_calls = pivot_df_agg.sum()
    pivot_df_per_project['overall'] = pivot_df_per_project.sum(axis=1)
    counter_clockwise_default = True
    angle_default = 0

    if use_pie:
        generate_pie_plot(pivot_df, 'overall', f'overall usage of {title} ({num_calls} calls)',
                          f"{output_dir}/overall_{title}.pdf",
                          angle,
                          counter_clockwise)
    else:
        generate_bar_plot(pivot_df, 'overall', f'overall usage of {title} ({num_calls} calls)',
                          f"{output_dir}/overall_{title}.pdf")

    print('overall')
    pivot_df['percent'] = 100 * pivot_df['overall'] / num_calls
    print(pivot_df['percent'])

    for cat, member in mpi_categories.items():
        members_used = [m for m in member if m in pivot_df.columns]
        # sometimes there is no function call that have the given argument
        if len(members_used) > 0:
            num_calls = pivot_df_agg[members_used].sum()
            pivot_df[cat] = pivot_df[members_used].sum(axis=1)

            print(cat)
            pivot_df['percent'] = 100 * pivot_df[cat] / num_calls
            print(pivot_df['percent'])

            if use_pie:
                generate_pie_plot(pivot_df, cat, f'usage of {title} in {cat} ({num_calls} calls)',
                                  f"{output_dir}/{cat}_{title}.pdf",
                                  angle,
                                  counter_clockwise)
            else:
                generate_bar_plot(pivot_df, cat, f'usage of {title} in {cat} ({num_calls} calls)',
                                  f"{output_dir}/{cat}_{title}.pdf")

            for call in members_used:
                num_calls = pivot_df_agg[call]
                if use_pie:
                    generate_pie_plot(pivot_df, call, f'usage of {title} in {call} ({num_calls} calls)',
                                      f"{output_dir}/{cat}/{call}_{title}.pdf", angle, counter_clockwise)
                else:
                    generate_bar_plot(pivot_df, call, f'usage of {title} in {call} ({num_calls} calls)',
                                      f"{output_dir}/{cat}/{call}_{title}.pdf")
    plt.close('all')


def generate_pie_plot(pivot_df, col, title, fname, angle, counter_clockwise):
    plt.clf()
    fig = plt.figure()
    plt.title(title, color='black')
    # plot = pivot_df.plot.pie(y=col, legend=False, startangle=angle, counterclock=counter_clockwise)
    # plot.set_ylabel("")
    sum = pivot_df[col].sum()
    plot = (
        pivot_df.assign(plot_this=lambda df_: 100 * df_[col] / sum)['plot_this']
        .plot.pie(ax=fig.gca())
    )
    # plot.set_legend(loc='center left', bbox_to_anchor=(1.0, 0.85))
    plt.savefig(fname, bbox_inches='tight')
    plt.close(fig)


def generate_bar_plot(pivot_df, col, title, fname):
    plt.clf()
    fig = plt.figure(figsize=(16, 3))
    ax = fig.gca()
    ax.set_xlim(0.0, 100.0)
    # plt.title(title, color='black')
    # plot = pivot_df.plot.pie(y=col, legend=False, startangle=angle, counterclock=counter_clockwise)
    # plot.set_ylabel("")
    sum = pivot_df[col].sum()

    plot_df = pd.DataFrame(
        pivot_df.assign(plot_this=lambda df_: 100 * df_[col] / sum)['plot_this'].rename('')).transpose()

    plot = plot_df.plot.barh(stacked=True, ax=ax, legend=False, edgecolor="black")
    ax.set_ylabel('')
    ax.set_xlabel('% Distribution')
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.65))

    y_sep = 0.1
    above = True
    for bar in ax.containers:
        label = bar.get_label()

        for rect in bar.patches:
            if rect.get_width() > 0:
                txt = ax.text(rect.get_x(), rect.get_y() + 0.2, label, weight='bold')
                # as datsa coordinates
                text_coords = ax.transData.inverted().transform(txt.get_window_extent())
                txt_width = text_coords[1][0] - text_coords[0][0]
                txt_height = text_coords[1][1] - text_coords[0][1]
                center_y = rect.get_y() + rect.get_height() / 2 - txt_height / 2
                center_x = rect.get_x() + rect.get_width() / 2 - txt_width / 2
                if rect.get_width() > txt_width:
                    # text fits
                    txt.set_position((center_x, center_y))
                else:
                    if above:
                        y = rect.get_y() + rect.get_height() + y_sep
                        # manual placement for better redability
                        if label == "Binary or Logical Op":
                            y = y + y_sep / 2
                            center_x = center_x + 10
                        ax.plot([center_x + txt_width / 2, rect.get_x() + rect.get_width() / 2],
                                [y, rect.get_y() + rect.get_height()], color='gray', linestyle='-', linewidth=2)
                    else:
                        y = rect.get_y() - y_sep - txt_height
                        ax.plot([center_x + txt_width / 2, center_x + txt_width / 2], [y + txt_height, rect.get_y()],
                                color='gray',
                                linestyle='-', linewidth=2)
                    above = not above
                    txt.set_position((center_x, y))
                pass

    ax.grid(which='major', axis='x', color='gray', linestyle='--', linewidth=1)

    plt.savefig(fname, bbox_inches='tight')
    plt.close(fig)


def get_type_usage_bar_plot(df, output_dir):
    def get_plot_label_overview(row):
        dtype = row['DATATYPE']
        category = row['DATATYPE_CATEGORY']
        if not pd.isna(dtype) and (category == 'MPI_constant'):
            return "Predefined"
        elif (category == 'handle'):
            return 'Derived'
        elif (category == 'by_define'):
            return 'Define'
        elif (category == 'function_call'):
            return 'Function'
        elif category == 'literal_constant' or category == 'arith_expression' or category == 'other_variable':
            return 'VarP'
        elif category == "other_variable_creation_func_exist":
            return 'VarU'
        else:
            return category

    def get_plot_label_predefined(row, other_detail=False):
        dtype = row['DATATYPE']
        category = row['DATATYPE_CATEGORY']
        if not pd.isna(dtype) and category == 'MPI_constant':
            if dtype == 'MPI_INT' or dtype == 'MPI_INTEGER' or dtype == 'MPI_INTEGER4' or dtype == 'MPI_UNSIGNED':
                return 'INT'
            elif dtype == 'MPI_DOUBLE' or dtype == 'MPI_DOUBLE_PRECISION' or dtype == 'MPI_REAL8' or dtype == 'MPI_LONG_DOUBLE':
                return 'DOUBLE'
            elif dtype == 'MPI_REAL' or dtype == 'MPI_REAL4' or dtype == 'MPI_FLOAT':
                return 'FLOAT'
            elif dtype == 'MPI_LONG' or dtype == 'MPI_LONG_INT' or dtype == 'MPI_LONG_LONG_INT' or dtype == 'MPI_LONG_LONG' or dtype == 'MPI_UNSIGNED_LONG' or dtype == 'MPI_UNSIGNED_LONG_LONG' or dtype == 'MPI_INTEGER8' or dtype == 'MPI_UINT64_T':
                return 'LONG_INT'
            elif dtype == 'MPI_CHAR' or dtype == 'MPI_CHARACTER' or dtype == 'MPI_UNSIGNED_CHAR':
                return 'CHAR'
            elif dtype == 'MPI_BYTE':
                return 'BYTE'
            elif dtype == 'MPI_2INT' or dtype == 'MPI_2INTEGER' or dtype == 'MPI_2REAL' or dtype == 'MPI_2DOUBLE_PRECISION' or dtype == 'MPI_DOUBLE_INT' or dtype == 'MPI_FLOAT_INT' or dtype == 'MPI_COMPLEX' or dtype == 'MPI_DOUBLE_COMPLEX':
                return 'Composed'
            else:
                if other_detail:
                    return dtype.replace("MPI_", "")
                else:
                    if dtype == 'MPI_2INT' or dtype == 'MPI_2INTEGER' or dtype == 'MPI_2REAL' or dtype == 'MPI_2DOUBLE_PRECISION' or dtype == 'MPI_DOUBLE_INT' or dtype == 'MPI_FLOAT_INT' or dtype == 'MPI_COMPLEX' or dtype == 'MPI_DOUBLE_COMPLEX':
                        return 'Composed'
                    else:
                        return "Other"
        else:
            return pd.NA

    def get_plot_label_derived(row, other_detail=False):
        dtype = row['DATATYPE']
        category = row['DATATYPE_CATEGORY']
        if not pd.isna(dtype) and (category == 'handle'):
            striped_type = dtype.replace("MPI_Type_", "").replace("create_", "").capitalize()
            if striped_type in ['Inconclusive', 'Dup', 'Contiguous', 'Hvector', 'Indexed',
                                'Struct', 'Subarray', 'Vector']:
                return striped_type
            if other_detail:
                return striped_type
            else:
                return 'Other'
        else:
            return pd.NA

    other_detail = False
    # print(pivot_df.head(10))
    df_1 = (df
            .assign(plot_label_overview=lambda df_: df_.apply(get_plot_label_overview, axis=1))
            .assign(
        plot_label_predefined=lambda df_: df_.apply(get_plot_label_predefined, axis=1, args=(other_detail,)))
            .assign(plot_label_derived=lambda df_: df_.apply(get_plot_label_derived, axis=1))
            )

    for cat, member in mpi_categories.items():
        if cat == 'coll':
            generate_multi_bar_pot(df_1, member, cat, f"{output_dir}/{cat}_datatypes.pdf", use_manual_positioning=1)
        elif cat == 'pt2pt':
            generate_multi_bar_pot(df_1, member, cat, f"{output_dir}/{cat}_datatypes.pdf", use_manual_positioning=2)
        else:
            generate_multi_bar_pot(df_1, member, cat, f"{output_dir}/{cat}_datatypes.pdf")
        for m in member:
            generate_multi_bar_pot(df_1, [m], m, f"{output_dir}/{cat}/{m}_datatypes.pdf")


def generate_multi_bar_pot(df, funcs_to_use, name, fname, use_manual_positioning=False):
    pivot_df_overview = df.pivot_table(values='Code', index='plot_label_overview', columns='call', aggfunc='count',
                                       fill_value=0)
    funcs_to_use = [f for f in funcs_to_use if f in pivot_df_overview.columns]
    if len(funcs_to_use) == 0:
        return
    pivot_df_predefined = df.pivot_table(values='Code', index='plot_label_predefined', columns='call',
                                         aggfunc='count', fill_value=0)
    pivot_df_derived = df.pivot_table(values='Code', index='plot_label_derived', columns='call', aggfunc='count',
                                      fill_value=0)

    # ordering of the for better redability
    desired_order = ['BYTE', 'CHAR', 'DOUBLE', 'FLOAT', 'LONG_INT', 'INT', 'Composed', 'Other']
    new_index = [i for i in desired_order if i in pivot_df_predefined.index]
    assert len(new_index) == len(pivot_df_predefined.index)
    pivot_df_predefined = pivot_df_predefined.reindex(new_index)

    desired_order = ['Derived', 'VarU', 'Function', 'Define', 'VarP', 'Predefined']
    new_index = [i for i in desired_order if i in pivot_df_overview.index]
    # dont drop data
    assert len(new_index) == len(pivot_df_overview.index)
    pivot_df_overview = pivot_df_overview.reindex(new_index)

    desired_order = ['Inconclusive', 'Dup']
    new_index = [i for i in desired_order if i in pivot_df_derived.index] + [i for i in pivot_df_derived.index if
                                                                             i not in desired_order]
    assert len(new_index) == len(pivot_df_derived.index)
    pivot_df_derived = pivot_df_derived.reindex(new_index)

    fig = plt.figure(figsize=(16, 4))
    fig.clf()

    ax = fig.gca()

    def get_percentage(pivot_df, cols):
        cols = [c for c in cols if c in pivot_df.columns]
        if len(cols) == 1:
            sum = pivot_df[cols].sum()
            return pivot_df.assign(percentage=lambda df_: 100 * df_[cols] / sum)['percentage']
        else:
            sum = pivot_df[cols].sum(axis=1).sum()
            return pivot_df.assign(percentage=lambda df_: 100 * df_[cols].sum(axis=1) / sum)['percentage']

    df_plot = pd.DataFrame([get_percentage(pivot_df_derived, funcs_to_use).rename("Derived Types"),
                            get_percentage(pivot_df_overview, funcs_to_use).rename("Overall"),
                            get_percentage(pivot_df_predefined, funcs_to_use).rename("Predefined Types")])
    plot = df_plot.plot.barh(stacked=True, ax=ax, legend=False, edgecolor="black")
    ax.set_ylabel('')
    ax.set_xlabel('% Distribution')
    ax.set_xlim(0.0, 100.0)
    # ax.set_title(f'dtype Usage in {name}')
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.65))
    # ax.grid(axis='y',color='red', linestyle='dashed', linewidth=3)

    label = ax.get_yticklabels()[1]
    label.set_weight("bold")

    # get the corresponding colors
    color_pre = None
    color_deriv = None

    for bar in ax.containers:
        label = bar.get_label()
        if label == "Derived":
            for rect in bar.patches:
                if rect.get_width() > 0:
                    color_deriv = rect.get_facecolor()
        elif label == "Predefined":
            for rect in bar.patches:
                if rect.get_width() > 0:
                    color_pre = rect.get_facecolor()

    pos_derived_end = get_percentage(pivot_df_overview, funcs_to_use)['Derived']
    # ax.plot([pos_derived_end, 100], [0.75, 0.25], color='black', linestyle='-', linewidth=1,alpha=0.5)
    # ax.plot([0, 0], [0.75, 0.25], color='black', linestyle='-', linewidth=1,alpha=0.5)
    poly_x = [0, pos_derived_end, 100, 0]
    poly_y = [0.75, 0.75, 0.25, 0.25]
    ax.fill(poly_x, poly_y, color=color_deriv, alpha=0.5)

    pos_predefined_end = 100 - get_percentage(pivot_df_overview, funcs_to_use)['Predefined']
    # ax.plot([pos_predefined_end, 0], [1.25, 1.75], color='black', linestyle='-', linewidth=1,alpha=0.5)
    # ax.plot([100, 100], [1.25, 1.75], color='black', linestyle='-', linewidth=1,alpha=0.5)
    poly_x = [0, pos_predefined_end, 100, 100]
    poly_y = [1.75, 1.25, 1.25, 1.75]
    ax.fill(poly_x, poly_y, color=color_pre, alpha=0.5)

    above = False
    y_sep = 0.1
    for bar in ax.containers:
        label = bar.get_label()

        for rect in bar.patches:
            if rect.get_width() > 0:
                txt = ax.text(rect.get_x(), rect.get_y() + 0.2, label, weight='bold')
                # as data coordinates
                text_coords = ax.transData.inverted().transform(txt.get_window_extent())
                txt_width = text_coords[1][0] - text_coords[0][0]
                txt_height = text_coords[1][1] - text_coords[0][1]
                center_y = rect.get_y() + rect.get_height() / 2 - txt_height / 2
                center_x = rect.get_x() + rect.get_width() / 2 - txt_width / 2
                if rect.get_width() > txt_width:
                    # text fits
                    txt.set_position((center_x, center_y))
                else:
                    if above:
                        y = rect.get_y() + rect.get_height() + y_sep
                        if use_manual_positioning == 1 and label == "Other":
                            # manual adjustment for better redability
                            center_x = center_x - 1
                        ax.plot([center_x + txt_width / 2, rect.get_x() + rect.get_width() / 2],
                                [y, rect.get_y() + rect.get_height()], color='gray', linestyle='-', linewidth=2)
                    else:
                        y = rect.get_y() - y_sep - txt_height
                        if use_manual_positioning == 2 and label == "Struct":
                            # manual adjustment for better redability
                            center_x = center_x - 2
                        ax.plot([center_x + txt_width / 2, rect.get_x() + rect.get_width() / 2],
                                [y + txt_height, rect.get_y()],
                                color='gray', linestyle='-', linewidth=2)

                    txt.set_position((center_x, y))
                above = not above
                pass
    ax.grid(which='major', axis='x', color='gray', linestyle='--', linewidth=1)
    plt.savefig(fname, bbox_inches='tight')
    plt.close(fig)


def get_feature_usage_per_category(df, output_dir):
    pivot_df_per_project = df.pivot_table(values='Code', columns='call', aggfunc='nunique',
                                          fill_value=0)
    num_codes = df['Code'].nunique()
    fig = plt.figure()
    # ax=fig.gca()

    cat_to_use = mpi_categories
    cat_to_use['comm_creation'] = mpi_comm_creator_funcs
    cat_to_use['type_creation'] = mpi_type_creation_funcs
    cat_to_use['group_creation'] = mpi_group_creator_funcs
    for cat, member in cat_to_use.items():
        fig.clf()
        members_used = [m for m in member if m in pivot_df_per_project.columns]
        plot = (pivot_df_per_project[members_used]
                .iloc[0]
                .sort_values()
                .apply(lambda x: 100.0 * x / num_codes)
                # select top 20
        [-20:]
                .plot
                .bar(
            xlabel="MPI Call",
            ylabel="% of Total Applications",
            ax=fig.gca()
        )
        )
        for p in plot.patches:
            plot.annotate(f"{p.get_height():.0f}%", (p.get_x() * 1.005, p.get_height() * 1.005))

        fname = f"{output_dir}/{cat}_usage.pdf"
        plt.savefig(fname, bbox_inches='tight')
        plt.close(fig)


def get_comm_usage_mix_plots(df, output_dir):
    def get_plot_label(row):
        creator = row['call']
        if not pd.isna(creator) and creator in mpi_comm_creator_funcs:
            if creator == 'MPI_Comm_dup_with_info' or creator == 'MPI_Comm_idup':
                return 'Variants of MPI_Comm_dup'
            return creator
        else:
            return "ERROR"

    select_df = df[df['call'].isin(mpi_comm_creator_funcs)].assign(
        plot_labels=lambda df_: df_.apply(get_plot_label, axis=1))

    fig = plt.figure()
    plt.clf()
    num_calls = len(select_df)
    plt.title(f'usage of MPI communicator creation functions ({num_calls} calls)', color='black')
    select_df.groupby('plot_labels').size().plot.pie(ax=fig.gca())
    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.1))

    plt.savefig(f"{output_dir}/CommCreation.pdf", bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.close(fig)

    def get_plot_label(row):
        comm = row['COMMUNICATOR']
        category = row['COMMUNICATOR_CATEGORY']
        if not pd.isna(comm) and (
                comm in predefined_mpi_communicator_consants or comm in mpi_comm_creator_funcs) or category == 'handle':
            if comm == 'MPI_Comm_split_type':
                return 'Comm_split'
            elif comm == 'MPI_COMM_NULL':
                # com null is basically not used anywas, so there is nothing meaningful to see in the plots
                return pd.NA
            return comm.replace("MPI_", "").capitalize()
        else:
            if category == 'other_variable':
                return 'VarP'
            else:
                return 'VarU'
            return category

    plot_df(df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "comm", output_dir)


def get_rank_usage_mix_plots(df, output_dir):
    def get_plot_label(row):
        rank = row['RANK']
        category = row['RANK_CATEGORY']
        if not pd.isna(rank) and (rank in predefined_mpi_constants):
            return rank
        elif rank == "0":
            return "Literal_0"
        else:
            return category

    plot_df(df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "rank", output_dir)


def get_info_usage_mix_plots(df, output_dir):
    def get_plot_label(row):
        info = row['INFO']
        category = row['INFO_CATEGORY']

        if not pd.isna(info) and (info in predefined_mpi_constants):
            return info
        else:
            return category

    plot_df(df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "info", output_dir)


def get_tag_usage_mix_plots(df, output_dir):
    def get_plot_label(row):
        tag = row['TAG']
        category = row['TAG_CATEGORY']
        if not pd.isna(tag) and (tag in predefined_mpi_constants):
            return tag
        elif category == "literal_constant":
            # if tag in ['0','1','10','20','30','50','2','40']:
            if tag in ['0', '1', '42']:
                return tag
            else:
                return "other literal constant"
        else:
            return category

    # pivot_df = (
    #    df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1))
    #    .pivot_table(values='Code', index='plot_labels', columns='call', aggfunc='count',
    #                 fill_value=0)
    # )
    # print(pivot_df.sum(axis=1).nlargest(25))

    plot_df(df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "tag", output_dir)


def get_status_usage_mix_plots(df, output_dir):
    def get_plot_label(row):
        status = row['STATUS']
        category = row['STATUS_CATEGORY']
        if not pd.isna(status) and (status in predefined_mpi_constants):
            return status
        else:
            return 'other_variable'
            # return category

    plot_df(df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "status", output_dir)


def get_errhandler_mix_plots(df, output_dir):
    df = df[df['call'].isin(['MPI_File_set_errhandler', 'MPI_Comm_set_errhandler', 'MPI_Win_set_errhandler',
                             'MPI_Session_set_errhandler', ])]

    def get_plot_label(row):
        handler = row['ERRHANDLER']
        category = row['ERRHANDLER_CATEGORY']
        if not pd.isna(handler) and (handler in predefined_mpi_constants):
            return handler
        else:
            return category

    plot_df(df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "errhandler", output_dir)


def get_const_count_usage_plots(df, output_dir):
    col_to_use = 'POLYXFER_NUM_ELEM_NNI'

    # first pass: elimiate all calls that do not have a count arg and transforme everything else to number
    count_df = df[df[col_to_use].notnull()].copy()
    count_df[col_to_use] = pd.to_numeric(count_df[col_to_use], errors='coerce')

    na_count = count_df[col_to_use].isna().sum()
    num_calls = len(count_df)
    percent = na_count * 100.0 / num_calls

    # drop nan and convert to int (better histogram)
    count_df = count_df[count_df[col_to_use].notnull()]
    count_df[col_to_use] = count_df[col_to_use].astype(int)

    print("Constants used as count argument")
    print(count_df[col_to_use].value_counts())
    y_max = count_df[col_to_use].value_counts().nlargest(2).iloc[1] * 2

    max_c_to_show = 128

    fig = plt.figure()
    plt.clf()
    (count_df
     .loc[count_df[col_to_use].notnull()]  # boolean mask
     .astype({col_to_use: int})
     .query(f"{col_to_use} <= {max_c_to_show}")
     .loc[:, col_to_use]  # select column
     .plot
     .hist(
        bins=max_c_to_show, ax=fig.gca(),
        xlabel="count", ylabel="num of usage",
        title=f"Overall usage of constant count arguments {percent:.2f}% has non-constant value",
        ylim=(0, y_max),
    ))
    plt.savefig(f"{output_dir}/count_usage.pdf")
    plt.close(fig)

    def get_plot_label(row):
        value = row['POLYXFER_NUM_ELEM_NNI']
        category = row['POLYXFER_NUM_ELEM_NNI_CATEGORY']
        if not pd.isna(value) and (value in predefined_mpi_constants):
            return value
        # elif value in ['0', '1', '2', '3', '4']:
        #    return value
        else:
            return category

    print("with handle as dtype")
    plot_df(df[df['DATATYPE_CATEGORY'] == 'handle'].assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)),
            "count", output_dir)

    print("with float as dtype")
    plot_df(df[df['DATATYPE'].isin(
        ['MPI_FLOAT', 'MPI_REAL', 'MPI_DOUBLE', 'MPI_DOUBLE_PRECISION', 'MPI_REAL8', 'MPI_LONG_DOUBLE'])].assign(
        plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "count", output_dir)

    print("with BYTE as dtype")
    plot_df(df[df['DATATYPE'].isin(
        ['MPI_BYTE', 'MPI_CHAR', 'MPI_CHARACTER'])].assign(
        plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "count", output_dir)

    print("with int as dtype")
    plot_df(df[df['DATATYPE'].isin(
        ['MPI_INT', 'MPI_INTEGER', 'MPI_UNSIGNED', 'MPI_LONG', 'MPI_LONG_INT', 'MPI_LONG_LONG_INT', 'MPI_LONG_LONG',
         'MPI_UNSIGNED_LONG', 'MPI_UNSIGNED_LONG_LONG', 'MPI_INTEGER8', 'MPI_UINT64_T'])].assign(
        plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "count", output_dir)

    # plot_df(df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1)), "count", output_dir)


def get_reduce_op_usage_plots(df, output_dir):
    def get_plot_label(row):
        value = row['OPERATION']
        category = row['OPERATION_CATEGORY']
        if not pd.isna(value) and (value in predefined_mpi_constants):
            if value.startswith('MPI_B') or value.startswith('MPI_L'):
                return "Binary or Logical Op"
            if value == 'MPI_MINLOC' or value == 'MPI_MAXLOC':
                return "MIN/MAXLOC"
            # if value == 'MPI_PROD':
            #    return 'other_variable'
            return value.replace("MPI_", "").capitalize()
        else:
            if category == "other_variable_creation_func_exist" or category == "function_call":
                return 'VarU'
            elif category == 'other_variable':
                return 'VarP'
            return category

    new_df = df.assign(plot_labels=lambda df_: df_.apply(get_plot_label, axis=1))

    print("total number of MPI_PROD")
    print(len(df[df['OPERATION'] == 'MPI_PROD']))

    plot_df(new_df, "op", output_dir)

    print("Are Operations created commutative?:")
    print(df[df['call'] == 'MPI_Op_create']['LOGICAL'].value_counts())


def get_num_defines_resolved(df, output_dir):
    print("Parameters given by preprocessor Define")
    # some_params_defined=df[df['params_by_define'] != "[]"]
    print(df['params_by_define'].value_counts())
    pass


def get_converter_funcs(df, output_dir):
    print("Are f2c or c2f funcs used:")
    print(df[df['call'].isin(mpi_converter_funcs)]['call'].value_counts())
    pass


def get_codes_per_feature(df, output_dir):
    to_plot = ['collective', 'pt2pt', 'comm_group', 'datatype', 'error', 'file', 'info', 'arrt_cache', 'persistent',
               'one_sided', 'process_mgmt', 'tool_iface', 'topology', 'dtype_constr', 'p2p_noreq']
    fig = plt.figure()
    fig.clf()
    table = (
        pd.pivot_table(df, values='src_location', index='Code', columns='call',
                       aggfunc='count', fill_value=0)
        # onl sum up hte columns that are there (unused MPI funcs are not there)
        .assign(collective=lambda df_: df_[df_.columns.intersection(mpi_coll)].sum(axis=1))
        .assign(pt2pt=lambda df_: df_[df_.columns.intersection(mpi_p2p)].sum(axis=1))
        .assign(
            p2p_noreq=lambda df_: df_[df_.columns.intersection(set(mpi_scorep_p2p) - mpi_persistent - mpi_request)].sum(
                axis=1))
        .assign(comm_group=lambda df_: df_[df_.columns.intersection(mpi_comm_group)].sum(axis=1))
        .assign(
            datatype=lambda df_: df_[df_.columns.intersection(mpi_types)].sum(axis=1))
        .assign(error=lambda df_: df_[df_.columns.intersection(mpi_error)].sum(axis=1))
        .assign(file=lambda df_: df_[df_.columns.intersection(mpi_io)].sum(axis=1))
        .assign(info=lambda df_: df_[df_.columns.intersection(mpi_info)].sum(axis=1))
        .assign(arrt_cache=lambda df_: df_[df_.columns.intersection(mpi_attrib)].sum(axis=1))
        .assign(persistent=lambda df_: df_[df_.columns.intersection(mpi_persistent)].sum(axis=1))
        .assign(one_sided=lambda df_: df_[df_.columns.intersection(mpi_rma)].sum(axis=1))
        .assign(process_mgmt=lambda df_: df_[df_.columns.intersection(mpi_processm)].sum(axis=1))
        .assign(tool_iface=lambda df_: df_[df_.columns.intersection(mpi_tools)].sum(axis=1))
        .assign(topology=lambda df_: df_[df_.columns.intersection(mpi_topo)].sum(axis=1))
        .assign(requests=lambda df_: df_[df_.columns.intersection(mpi_request)].sum(axis=1))
        .assign(misc=lambda df_: df_[df_.columns.intersection(mpi_misc)].sum(axis=1))
        .assign(dtype_constr=lambda df_: df_[df_.columns.intersection(mpi_types_constructor_only)].sum(axis=1))
        [to_plot]
    )

    plot = (table
    # count values larger 0
    .agg(lambda col: 100.0 * (col > 0).sum() / len(col))
    .sort_values(axis=0)
    .plot
    .bar(
        xlabel="Unique MPI Feature",
        ylabel="% of Total Applications",
        ax=fig.gca()
    )
    )
    for p in plot.patches:
        plot.annotate(f"{p.get_height():.0f}%", (p.get_x() * 1.005, p.get_height() * 1.005))

    # plt.show()

    plt.savefig(f"{output_dir}/Features_By_code.pdf", bbox_extra_artists=(plot,), bbox_inches='tight')
    plt.close(fig)
    pass


def get_hybrid_codes(df, output_dir):
    fig = plt.figure()
    fig.clf()
    indicators = ['openmp', 'openacc', 'cuda_device_kernel', 'cuda_global_kernel', 'opencl_global', 'opencl_kernel']
    indicators = ['openmp', 'openacc', 'cuda', 'opencl']
    to_plot_labels = ['OpenMP', 'None', 'CUDA\nOpenMP', 'CUDA\nOpenCL', 'OpenMP\nOpenACC', 'CUDA', 'CUDA\nOpenACC']
    to_plot = ['OpenMP', 'No', 'OpenMP_CUDA', 'CUDA_OpenCL', 'OpenMP_OpenACC', 'CUDA', 'CUDA_OpenACC',
               'OpenMP_OpenCL', 'OpenMP_CUDA_OpenACC', 'OpenMP_CUDA_OpenCL']

    table = (
        pd.pivot_table(df, values='src_location', index='Code', columns='call',
                       aggfunc='count', fill_value=0)
        .assign(cuda=lambda df_: df_[['cuda_device_kernel', 'cuda_global_kernel']].sum(axis=1))
        .assign(opencl=lambda df_: df_[['opencl_global', 'opencl_kernel']].sum(axis=1))
        # used for the plots
        .assign(No=lambda df_: df_[indicators].sum(axis=1) == 0)
        .assign(OpenMP=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] > 0 and row['cuda'] == 0 and row['openacc'] == 0 and row[
                'opencl'] == 0 else 0, axis=1))
        .assign(OpenMP_OpenACC=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] > 0 and row['cuda'] == 0 and row['openacc'] > 0 and row[
                'opencl'] == 0 else 0, axis=1))
        .assign(OpenMP_CUDA=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] > 0 and row['cuda'] > 0 and row['openacc'] == 0 and row[
                'opencl'] == 0 else 0, axis=1))
        .assign(CUDA=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] == 0 and row['cuda'] > 0 and row['openacc'] == 0 and row[
                'opencl'] == 0 else 0, axis=1))
        .assign(CUDA_OpenCL=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] == 0 and row['cuda'] > 0 and row['openacc'] == 0 and row[
                'opencl'] > 0 else 0, axis=1))
        .assign(CUDA_OpenACC=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] == 0 and row['cuda'] > 0 and row['openacc'] > 0 and row[
                'opencl'] == 0 else 0, axis=1))
        .assign(OpenMP_OpenCL=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] > 0 and row['cuda'] == 0 and row['openacc'] == 0 and row[
                'opencl'] > 0 else 0, axis=1))
        .assign(OpenMP_CUDA_OpenACC=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] > 0 and row['cuda'] > 0 and row['openacc'] > 0 and row[
                'opencl'] == 0 else 0, axis=1))
        .assign(OpenMP_CUDA_OpenCL=lambda df_: df_.apply(
            lambda row: 1 if row['openmp'] > 0 and row['cuda'] > 0 and row['openacc'] == 0 and row[
                'opencl'] > 0 else 0, axis=1))
    )

    plot = (table
    [to_plot]
    .agg(lambda col: 100.0 * (col == True).sum() / len(col))
    .sort_values(axis=0)
    .plot
    .bar(
        xlabel="X in MPI+X",
        ylabel="% of Total Applications",
        ax=fig.gca(),
    )
    )
    for p in plot.patches:
        plot.annotate(f"{p.get_height():.0f}%", (p.get_x() * 1.005, p.get_height() * 1.005))

    # does not work with sorting:
    # fig.gca().set_xticklabels(to_plot_labels)

    plt.savefig(f"{output_dir}/HybridUsage.pdf", bbox_extra_artists=(plot,), bbox_inches='tight')
    plt.close(fig)

    pass


def get_thread_level(df, output_dir):
    def maximum_thread_level(column):
        set_to_check = column.unique()
        if 'MPI_THREAD_MULTIPLE' in set_to_check:
            return 'MULTIPLE'
        elif 'MPI_THREAD_SERIALIZED' in set_to_check:
            return 'SERIALIZED'
        elif 'MPI_THREAD_FUNNELED' in set_to_check:
            return 'FUNNELED'
        elif 'MPI_THREAD_SINGLE' in set_to_check:
            return 'SINGLE'
        else:
            # pd.NA
            return 'other_variable'

    plot = (df
            .query(f'call=="MPI_Init_thread"')
            .groupby('Code')['THREAD_LEVEL']
            .agg(maximum_thread_level)
            .value_counts(normalize=True, sort=True)
            .apply(lambda x: 100 * x)
            .plot
            .bar())

    for p in plot.patches:
        plot.annotate(f"{p.get_height():.0f}%", (p.get_x() * 1.005, p.get_height() * 1.005))

    plot.set_xlabel("Maximum Required Thread Level")
    plot.set_ylabel("Percentage of Applications using MPI_Init_thread")
    plt.savefig(f"{output_dir}/thread_level.pdf", bbox_extra_artists=(plot,), bbox_inches='tight')


def get_version_per_code(df, output_dir):
    fig = plt.figure()
    fig.clf()

    plot = (
        df
        .groupby('Code')
        ['version']
        .max()
        .plot
        .hist(
            ax=fig.gca(),
            # does not work for histogram?
            xlabel="Mimimum Required MPI version",
            ylabel="Application Count",
        )
    )

    print("classified as 4.0:")
    print(df[df['version'] == 4.0]['call'].value_counts())

    plot.set_xlabel("Mimimum Required MPI version")
    plot.set_ylabel("Application Count")

    plt.savefig(f"{output_dir}/versions_by_code.pdf", bbox_extra_artists=(plot,), bbox_inches='tight')
    plt.close(fig)


def get_creation_base_types(df, output_dir):
    def get_plot_label_overview(row):
        dtype = row['DATATYPE']
        category = row['DATATYPE_CATEGORY']
        if not pd.isna(dtype) and (category == 'MPI_constant' or category == 'handle'):
            if dtype == 'MPI_INT' or dtype == 'MPI_INTEGER' or dtype == 'MPI_UNSIGNED':
                return 'INT'
            elif dtype == 'MPI_DOUBLE' or dtype == 'MPI_DOUBLE_PRECISION' or dtype == 'MPI_REAL8' or dtype == 'MPI_LONG_DOUBLE':
                return 'DOUBLE'
            elif dtype == 'MPI_REAL' or dtype == 'MPI_FLOAT':
                return 'FLOAT'
            elif dtype == 'MPI_LONG' or dtype == 'MPI_LONG_INT' or dtype == 'MPI_LONG_LONG_INT' or dtype == 'MPI_LONG_LONG' or dtype == 'MPI_UNSIGNED_LONG' or dtype == 'MPI_UNSIGNED_LONG_LONG' or dtype == 'MPI_INTEGER8' or dtype == 'MPI_UINT64_T':
                return 'LONG_INT'
            elif dtype == 'MPI_CHAR' or dtype == 'MPI_CHARACTER' or dtype == 'MPI_UNSIGNED_CHAR':
                return 'CHAR'
            elif dtype == 'MPI_BYTE':
                return 'MPI_BYTE'
            elif dtype.startswith("MPI_Type") or dtype == 'inconclusive':
                # return dtype
                return 'Derived'
            # elif dtype == 'MPI_2INT' or dtype == 'MPI_2INTEGER' or dtype == 'MPI_2REAL' or dtype=='MPI_2DOUBLE_PRECISION' or dtype == 'MPI_DOUBLE_INT'or dtype == 'MPI_FLOAT_INT' or dtype == 'MPI_COMPLEX'or dtype == 'MPI_DOUBLE_COMPLEX':
            #    return 'Predefined "composed" types'
            else:
                return "other predefined type"
        else:
            if category == 'literal_constant' or category == 'function_call':
                return 'other_variable'
            return category

    def get_plot_label_detail(row):
        dtype = row['DATATYPE']
        category = row['DATATYPE_CATEGORY']
        if not pd.isna(dtype) and (category == 'MPI_constant' or category == 'handle'):
            if dtype.startswith("MPI_Type") or dtype == 'inconclusive':
                return dtype
                # return 'Derived'
            else:
                return "predefined MPI type"
        else:
            if category == 'literal_constant' or category == 'function_call':
                return 'other_variable'
            return category

    overview_table = (df[df['call'].isin(mpi_type_creation_funcs)]
                      .assign(plot_labels=lambda df_: df_.apply(get_plot_label_overview, axis=1))
                      .pivot_table(values='Code', index='call', columns='plot_labels', aggfunc='count', fill_value=0)
                      .reset_index()
                      )
    print(overview_table.to_string())
    fig = plt.figure()
    fig.clf()
    plot = (df[df['call'].isin(mpi_type_creation_funcs)]
            .assign(plot_labels=lambda df_: df_.apply(get_plot_label_overview, axis=1))
            .pivot_table(values='Code', index='call', columns='plot_labels', aggfunc='count', fill_value=0)
            .plot.bar(stacked=True, ax=fig.gca())
            )
    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.85))
    plt.savefig(f"{output_dir}/basetypes_overview.pdf", bbox_extra_artists=(lgd,), bbox_inches='tight')

    base_table = (df[df['call'].isin(mpi_type_creation_funcs)]
                  .assign(plot_labels=lambda df_: df_.apply(get_plot_label_detail, axis=1))
                  .pivot_table(values='Code', index='call', columns='plot_labels', aggfunc='count', fill_value=0)
                  .reset_index()
                  )
    print(base_table.to_string())
    fig.clf()
    plot = (df[df['call'].isin(mpi_type_creation_funcs)]
            .assign(plot_labels=lambda df_: df_.apply(get_plot_label_detail, axis=1))
            .pivot_table(values='Code', index='call', columns='plot_labels', aggfunc='count', fill_value=0)
            .plot.bar(stacked=True, ax=fig.gca())
            )

    lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.85))
    plt.savefig(f"{output_dir}/basetypes_detail.pdf", bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='output.csv',
                        help='the result data to visualize')
    parser.add_argument('--output_dir', default='visualization',
                        help='directory where all the plots will be created')

    args = parser.parse_args()
    df = pd.read_csv(args.input, low_memory=False)

    # make dirs to organize all the plots
    for cat in mpi_categories:
        os.makedirs(args.output_dir + "/" + cat, exist_ok=True)

    print("Percentage of calls, where analysis completely failed: (e.g. wrong formatting)")
    all_calls = len(df)
    failed_calls = len(df[df['analysis_successful'] == False])
    percent = 100.0 * failed_calls / all_calls
    print("%.2f%%" % percent)
    df = df[df['analysis_successful'] != False]
    # if col is missing (e.g. openmp pragma we still keep this record)

    get_type_usage_bar_plot(df, args.output_dir)
    get_creation_base_types(df, args.output_dir)
    get_num_type_usage_category_plots(df, args.output_dir)
    get_reduce_op_usage_plots(df, args.output_dir)
    get_const_count_usage_plots(df, args.output_dir)
    get_num_type_usage_category_plots(df, args.output_dir)
    get_comm_usage_mix_plots(df, args.output_dir)
    get_rank_usage_mix_plots(df, args.output_dir)
    get_tag_usage_mix_plots(df, args.output_dir)
    get_info_usage_mix_plots(df, args.output_dir)
    get_errhandler_mix_plots(df, args.output_dir)
    get_status_usage_mix_plots(df, args.output_dir)
    get_num_defines_resolved(df, args.output_dir)

    get_codes_per_feature(df, args.output_dir)
    get_version_per_code(df, args.output_dir)
    get_hybrid_codes(df, args.output_dir)
    get_converter_funcs(df, args.output_dir)
    get_thread_level(df, args.output_dir)

    get_feature_usage_per_category(df, args.output_dir)


if __name__ == "__main__":
    main()
