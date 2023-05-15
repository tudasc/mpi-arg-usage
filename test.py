import os.path
import subprocess
import re
import json
import pytest

from AnalysisModule.helper import get_call_with_parmeters
from AnalysisModule.MPIAnalysisModule.CallAnalysis import SingleMPICallAnalysis

from AnalysisModule.MPIAnalysisModule.MPIAPIParameters import mpi_api_dict

from AnalysisModule.repository import Repository


@pytest.mark.parametrize("input,num_params",
                         [("MPI_Barrier(MPI_COMM_WORLD);", 2),
                          (
                                  "MPI_Irecv( u + INDEX(i_min[MACSIO_MAIN_Rank] - 1, 1), N, MPI_DOUBLE, left_proc[MACSIO_MAIN_Rank], 0, MACSIO_MAIN_Comm, request + requests++ );",
                                  8),
                          (
                                  "if (MPI_SUCCESS != MPI_Allgather(&netNum, 1, MPI_UNSIGNED_LONG, netNums, 1, MPI_UNSIGNED_LONG, MPI_COMM_WORLD)) {",
                                  8)])
def test_get_call_with_params(input, num_params):
    # print(input)
    res = get_call_with_parmeters(input)
    # print(res)
    assert len(res) == num_params


def test_openmp_normalization():
    file = "repositories/Enzo/src/enzo/ffte4X.F90"
    if not os.path.isfile(file):
        pytest.skip(f" Test code file is not present: {file}")

    repo = Repository(repoName="Enzo", repoPath='repositories/Enzo')
    normalized = repo.get_normalized_file_content(file)

    assert 'OMP' in normalized


def get_analysis_for(call):
    info = mpi_api_dict[call]
    return SingleMPICallAnalysis(call, info[0], info[1])


def test_multiple_param_count():
    analysis = get_analysis_for('MPI_Init_thread')

    input = "MPI_Init_thread(NULL,NULL,MPI_THREAD_MULTIPLE,&provided);"
    # print(input)
    call = get_call_with_parmeters(input)

    res = analysis.analyze_call("test", 0, call)
    # print(res)
    assert res['analysis_successful'].all()
    assert res['THREAD_LEVEL'][0] == "MPI_THREAD_MULTIPLE"
    assert res['ARGUMENT_COUNT'][0] == "NULL"

    input = "MPI_INIT_THREAD(MPI_THREAD_MULTIPLE,provided,ierr);"
    # print(input)
    call = get_call_with_parmeters(input)

    res = analysis.analyze_call("test", 0, call)
    # print(res)
    assert res['analysis_successful'].all()

    input = "MPI_Init_thread(MPI_THREAD_MULTIPLE,provided);"
    # print(input)
    call = get_call_with_parmeters(input)

    res = analysis.analyze_call("test", 0, call)
    # print(res)
    assert res['analysis_successful'].all()


def test_c_declaration():
    analysis = get_analysis_for('MPI_Send')
    input = 'int MPI_Send(const void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)'
    call = get_call_with_parmeters(input)
    assert call == []


@pytest.mark.skip(reason="no testcase yet, need to create a file with only fortran decls")
def test_fortran_declaration():
    # TODO implement a test for it!
    assert False


@pytest.mark.parametrize("input", [
    'MPI_Pcontrol(LEVEL)', 'MPI_Pcontrol(LEVEL, vararg1)',
    'MPI_Pcontrol(LEVEL, vararg1, vararg2)'])
def test_vararg(input):
    analysis = get_analysis_for('MPI_Pcontrol')
    call = get_call_with_parmeters(input)
    if analysis.is_call_matching(call[0]):
        res = analysis.analyze_call("test", 0, call)
        print(res)
        assert res['analysis_successful'].all()
