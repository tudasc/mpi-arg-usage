import pandas as pd
import numpy as np

from AnalysisModule.MPIAnalysisModule.MPIAPICategories import *

# setup:
real_world_file = "output.csv"
corrbench_file = "repositories/MPI-Corrbench.csv"
mbi_file = "repositories/MpiBugsInitiative.csv"


def get_codes_for_call(df, call):
    return len(df[df['call'] == call]['Code'].unique())


def get_row(category_members, real_world_all, cobe_all, mbi_all):
    real_world_filtered = [m for m in real_world_all if m in category_members]
    cobe_filtered = [m for m in cobe_all if m in category_members]
    mbi_filtered = [m for m in mbi_all if m in category_members]

    # print("Top:")
    # top = real_world_filtered[0]
    # print(top)
    # print((top in cobe_filtered, top in mbi_filtered))

    cobeX = 0
    mbiX = 0
    for func in real_world_filtered[:len(real_world_filtered) // 2]:
        if func in cobe_filtered:
            cobeX = cobeX + 1
        if func in mbi_filtered:
            mbiX = mbiX + 1

    # in percent
    cobeX = 100 * cobeX / (len(real_world_filtered) // 2)
    mbiX = 100 * mbiX / (len(real_world_filtered) // 2)

    return [len(np.intersect1d(real_world_filtered, cobe_filtered)),
            len(np.setdiff1d(real_world_filtered, cobe_filtered)),
            len(np.setdiff1d(cobe_filtered, real_world_filtered)), -1, cobeX,
            len(np.intersect1d(real_world_filtered, mbi_filtered)),
            len(np.setdiff1d(real_world_filtered, mbi_filtered)),
            len(np.setdiff1d(mbi_filtered, real_world_filtered)), -1, mbiX]


def print_stats(real_world, cobe, mbi):
    df = pd.DataFrame(columns=[
        'COBE_real_covered', 'COBE_real_not_covered', 'COBE_not_real_covered', 'COBE_not_real_not_covered',
        'COBE_top_half',
        'MBI_real_covered', 'MBI_real_not_covered', 'MBI_not_real_covered', 'MBI_not_real_not_covered', 'MBI_top_half'
    ])

    # are the top x elements included?
    cobeX = 0
    while cobeX < len(real_world) and real_world[cobeX] in cobe:
        cobeX = cobeX + 1

    mbiX = 0
    while mbiX < len(real_world) and real_world[mbiX] in mbi:
        mbiX = mbiX + 1

    # print("Top:")
    # top = real_world[0]
    # print(top)
    # print((top in cobe, top in mbi))

    df.loc['overall'] = [len(np.intersect1d(real_world, cobe)), len(np.setdiff1d(real_world, cobe)),
                         len(np.setdiff1d(cobe, real_world)), -1, cobeX,
                         len(np.intersect1d(real_world, mbi)), len(np.setdiff1d(real_world, mbi)),
                         len(np.setdiff1d(mbi, real_world)), -1, mbiX]
    for cat, members in mpi_categories.items():
        df.loc[cat] = get_row(members, real_world, cobe, mbi)

    print(df.drop('COBE_not_real_not_covered', axis=1).drop('MBI_not_real_not_covered', axis=1))


def main():
    real_world_df = pd.read_csv(real_world_file, low_memory=False)
    real_world_df[real_world_df['analysis_successful'] == True]
    # real_world_ranking = real_world_df['call'].value_counts().sort_values(ascending=False).index
    real_world_unsorted = real_world_df[real_world_df['call'].isin(mpi_all_mpi)]['call'].unique()
    num_apps = [get_codes_for_call(real_world_df, c) for c in real_world_unsorted]
    real_world = pd.Series(num_apps, index=real_world_unsorted).sort_values(
        ascending=False).index

    # real_world = real_world_df['call'].unique()
    cobe_df = pd.read_csv(corrbench_file, low_memory=False)
    cobe_df[cobe_df['analysis_successful'] == True]
    mbi_df = pd.read_csv(mbi_file, low_memory=False)
    mbi_df[mbi_df['analysis_successful'] == True]

    cobe_correct = cobe_df[cobe_df['src_location'].str.contains("correct/")]['call'].unique()
    cobe_faulty = cobe_df[~cobe_df['src_location'].str.contains("correct/")]['call'].unique()

    mbi_correct = mbi_df[mbi_df['src_location'].str.contains("no-error-")]['call'].unique()
    mbi_faulty = mbi_df[~mbi_df['src_location'].str.contains("no-error-")]['call'].unique()

    print("ALL Testcases:")
    print_stats(real_world, cobe_df['call'].unique(), mbi_df['call'].unique())
    print("")
    print("Faulty Testcases:")
    print_stats(real_world, cobe_faulty, mbi_faulty)
    print("Correct Testcases:")
    print_stats(real_world, cobe_correct, mbi_correct)


if __name__ == '__main__':
    main()
