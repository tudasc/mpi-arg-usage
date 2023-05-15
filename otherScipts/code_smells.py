import pandas as pd

from AnalysisModule.MPIAnalysisModule.MPIAPICategories import *

# setup:
input_file = "output.csv"


def get_code_with_smell(df, has_call_list, has_not_call_list):
    mask_smell = df.groupby('Code')['call'].apply(
        lambda x: (x.isin(has_call_list)).any() and not (x.isin(has_not_call_list)).any())
    mask_correct = df.groupby('Code')['call'].apply(
        lambda x: (x.isin(has_call_list)).any() and (x.isin(has_not_call_list)).any())

    print(f"{mask_smell.sum()} wrong and {mask_correct.sum()} correct")

    bad_codes = mask_smell.index[mask_smell == True].tolist()

    print(bad_codes)
    call_to_search_for = has_not_call_list[0]
    import subprocess
    for c in bad_codes:
        grep_command = f'grep -Ri "{call_to_search_for}" repositories/{c}'
        print(grep_command)
        subprocess.run(grep_command, shell=True)

        input("")


def main():
    df = pd.read_csv(input_file, low_memory=False)

    print("Type Commit without Free")
    get_code_with_smell(df, ["MPI_Type_commit"], ["MPI_Type_free"])
    print("Communicator creation without Free")
    get_code_with_smell(df, mpi_comm_creator_funcs, ["MPI_Comm_free"])
    print("MPI_Op_create creation without Free")
    get_code_with_smell(df, ['MPI_Op_create'], ["MPI_Op_free"])
    print("Persistent Operation creation without Free")
    get_code_with_smell(df, mpi_persistent_funcs, ["MPI_Request_free"])
    print("win_Create Operation creation without Free")
    get_code_with_smell(df, ['MPI_Win_create',
                             'MPI_Win_allocate',
                             'MPI_Win_allocate_shared',
                             'MPI_Win_create_dynamic', ], ["MPI_Win_free"])

    print("Type_create_h without mpi_address")
    get_code_with_smell(df, [
        'MPI_Type_create_hvector',
        'MPI_Type_create_hindexed',
        'MPI_Type_create_hindexed_block'], ["MPI_Get_address"])

    print("one sided operation without syncronization")
    get_code_with_smell(df,
                        ['MPI_Get',
                         'MPI_Put',
                         'MPI_Rget',
                         'MPI_Rput',
                         'MPI_Accumulate',
                         'MPI_Get_accumulate',
                         'MPI_Fetch_and_op',
                         'MPI_Compare_and_swap'],

                        ['MPI_Win_start',
                         'MPI_Win_complete',
                         'MPI_Win_post',
                         'MPI_Win_wait',

                         'MPI_Win_lock',
                         'MPI_Win_unlock',
                         'MPI_Win_lock_all',
                         'MPI_Win_unlock_all',

                         'MPI_Win_fence'])

    pass


if __name__ == '__main__':
    main()
