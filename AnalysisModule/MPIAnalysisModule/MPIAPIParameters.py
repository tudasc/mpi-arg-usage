# for each function we have a tuple
# first entry indicates it this function is VARARg (like MPI_Pcontrol)
# second entry is a dict
# with the allowed number of arguments a keys
# and for each key, a boolean mask on which arguments we save for later analysis and the classification of those parameters

mpi_api_dict = {
    'MPI_Abort': (False, {3: ([True, True, False], ['COMMUNICATOR', 'ERROR_CODE']),
                          2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE'])}),
    'MPI_Accumulate': (False, {10: ([True, True, True, True, True, False, False, True, True, True],
                                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI',
                                     'OPERATION', 'WINDOW', 'ERROR_CODE']), 9: (
        [True, True, True, True, True, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'OPERATION', 'WINDOW'])}),
    'MPI_Add_error_class': (False, {2: ([True, True], ['ERROR_CLASS', 'ERROR_CODE']), 1: ([True], ['ERROR_CLASS'])}),
    'MPI_Add_error_code': (
        False,
        {3: ([True, True, False], ['ERROR_CLASS', 'ERROR_CODE']), 2: ([True, True], ['ERROR_CLASS', 'ERROR_CODE'])}),
    'MPI_Add_error_string': (
        False, {3: ([True, True, False], ['ERROR_CODE', 'STRING']), 2: ([True, True], ['ERROR_CODE', 'STRING'])}),
    'MPI_Aint_add': (False, {2: ([True, True], ['LOCATION_SMALL', 'DISPLACEMENT'])}),
    'MPI_Aint_diff': (False, {2: ([True, False], ['LOCATION_SMALL'])}), 'MPI_Allgather': (False, {8: (
        [True, True, True, False, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'ERROR_CODE']), 7: (
        [True, True, True, False, False, False, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Allgather_init': (False, {10: ([True, True, True, False, False, False, True, True, True, True],
                                        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO',
                                         'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, False, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Allgatherv': (False, {
        9: ([True, True, True, False, False, True, False, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR', 'ERROR_CODE']), 8: (
            [True, True, True, False, False, True, False, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR'])}),
    'MPI_Allgatherv_init': (
        False, {11: ([True, True, True, False, False, True, False, True, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR', 'INFO',
                      'REQUEST',
                      'ERROR_CODE']), 10: ([True, True, True, False, False, True, False, True, True, True],
                                           ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT',
                                            'COMMUNICATOR', 'INFO', 'REQUEST'])}), 'MPI_Alloc_mem': (False, {
        4: ([True, True, True, True], ['ALLOC_MEM_NUM_BYTES', 'INFO', 'C_BUFFER', 'ERROR_CODE']),
        3: ([True, True, True], ['ALLOC_MEM_NUM_BYTES', 'INFO', 'C_BUFFER'])}), 'MPI_Allreduce': (False, {7: (
        [True, False, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'ERROR_CODE']), 6: (
        [True, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR'])}),
    'MPI_Allreduce_init': (False, {9: (
        [True, False, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']),
        8: (
            [True, False, True, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Alltoall': (False, {8: ([True, True, True, False, False, False, True, True],
                                 ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'ERROR_CODE']), 7: (
        [True, True, True, False, False, False, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Alltoall_init': (False, {10: ([True, True, True, False, False, False, True, True, True, True],
                                       ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO',
                                        'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, False, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Alltoallv': (False, {
        10: ([True, True, True, True, False, False, False, False, True, True],
             ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'ERROR_CODE']), 9: (
            [True, True, True, True, False, False, False, False, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Alltoallv_init': (
        False, {12: ([True, True, True, True, False, False, False, False, True, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'INFO',
                      'REQUEST',
                      'ERROR_CODE']), 11: ([True, True, True, True, False, False, False, False, True, True, True],
                                           ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE',
                                            'COMMUNICATOR', 'INFO', 'REQUEST'])}), 'MPI_Alltoallw': (False, {10: (
        [True, True, True, True, False, False, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'ERROR_CODE']), 9: (
        [True, True, True, True, False, False, False, False, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR'])}), 'MPI_Alltoallw_init': (
        False, {12: ([True, True, True, True, False, False, False, False, True, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'INFO',
                      'REQUEST',
                      'ERROR_CODE']), 11: ([True, True, True, True, False, False, False, False, True, True, True],
                                           ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE',
                                            'COMMUNICATOR', 'INFO', 'REQUEST'])}), 'MPI_Attr_delete': (False, {
        3: ([True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ERROR_CODE']),
        2: ([True, True], ['COMMUNICATOR', 'KEYVAL'])}), 'MPI_Attr_get': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10', 'LOGICAL', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10', 'LOGICAL'])}), 'MPI_Attr_put': (
        False, {4: ([True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10', 'ERROR_CODE']),
                3: ([True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10'])}),
    'MPI_Barrier': (False, {2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE']), 1: ([True], ['COMMUNICATOR'])}),
    'MPI_Barrier_init': (False, {4: ([True, True, True, True], ['COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']),
                                 3: ([True, True, True], ['COMMUNICATOR', 'INFO', 'REQUEST'])}), 'MPI_Bcast': (False, {
        6: ([True, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'ERROR_CODE']),
        5: ([True, True, True, True, True], ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR'])}),
    'MPI_Bcast_init': (False, {8: ([True, True, True, True, True, True, True, True],
                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'INFO',
                                    'REQUEST', 'ERROR_CODE']), 7: ([True, True, True, True, True, True, True],
                                                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE',
                                                                    'RANK', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Bsend': (False, {7: ([True, True, True, True, True, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                               'ERROR_CODE']), 6: ([True, True, True, True, True, True],
                                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG',
                                                    'COMMUNICATOR'])}), 'MPI_Bsend_init': (False, {8: (
        [True, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Buffer_attach': (
        False, {3: ([True, True, True], ['BUFFER', 'POLYNUM_BYTES_NNI', 'ERROR_CODE']),
                2: ([True, True], ['BUFFER', 'POLYNUM_BYTES_NNI'])}), 'MPI_Buffer_detach': (False, {
        3: ([True, True, True], ['C_BUFFER2', 'POLYNUM_BYTES', 'ERROR_CODE']),
        2: ([True, True], ['C_BUFFER2', 'POLYNUM_BYTES'])}),
    'MPI_Cancel': (False, {2: ([True, True], ['REQUEST', 'ERROR_CODE']), 1: ([True], ['REQUEST'])}),
    'MPI_Cart_coords': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'RANK', 'ARRAY_LENGTH', 'COORDINATE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'RANK', 'ARRAY_LENGTH', 'COORDINATE'])}), 'MPI_Cart_create': (
        False, {7: (
            [True, True, True, True, False, False, True],
            ['COMMUNICATOR', 'NUM_DIMS', 'DIMENSION', 'LOGICAL', 'ERROR_CODE']),
            6: ([True, True, True, True, False, False], ['COMMUNICATOR', 'NUM_DIMS', 'DIMENSION', 'LOGICAL'])}),
    'MPI_Cart_get': (False, {6: ([True, True, True, True, True, True],
                                 ['COMMUNICATOR', 'ARRAY_LENGTH', 'DIMENSION', 'LOGICAL', 'COORDINATE', 'ERROR_CODE']),
                             5: ([True, True, True, True, True],
                                 ['COMMUNICATOR', 'ARRAY_LENGTH', 'DIMENSION', 'LOGICAL', 'COORDINATE'])}),
    'MPI_Cart_map': (False, {6: ([True, True, True, True, True, True],
                                 ['COMMUNICATOR', 'NUM_DIMS', 'DIMENSION', 'LOGICAL', 'newRANK', 'ERROR_CODE']), 5: (
        [True, True, True, True, True], ['COMMUNICATOR', 'NUM_DIMS', 'DIMENSION', 'LOGICAL', 'newRANK'])}),
    'MPI_Cart_rank': (False, {4: ([True, True, True, True], ['COMMUNICATOR', 'COORDINATE', 'RANK', 'ERROR_CODE']),
                              3: ([True, True, True], ['COMMUNICATOR', 'COORDINATE', 'RANK'])}), 'MPI_Cart_shift': (
        False,
        {6: ([True, True, True, True, False, True], ['COMMUNICATOR', 'INDEX', 'DIMENSION', 'RANK', 'ERROR_CODE']),
         5: ([True, True, True, True, False], ['COMMUNICATOR', 'INDEX', 'DIMENSION', 'RANK'])}), 'MPI_Cart_sub': (
        False, {4: ([True, True, True, True], ['COMMUNICATOR', 'LOGICAL', 'newCOMMUNICATOR', 'ERROR_CODE']),
                3: ([True, True, True], ['COMMUNICATOR', 'LOGICAL', 'newCOMMUNICATOR'])}), 'MPI_Cartdim_get': (False, {
        3: ([True, True, True], ['COMMUNICATOR', 'NUM_DIMS', 'ERROR_CODE']),
        2: ([True, True], ['COMMUNICATOR', 'NUM_DIMS'])}),
    'MPI_Close_port': (False, {2: ([True, True], ['STRING', 'ERROR_CODE']), 1: ([True], ['STRING'])}),
    'MPI_Comm_accept': (False, {6: (
        [True, True, True, True, True, True],
        ['STRING', 'INFO', 'RANK', 'COMMUNICATOR', 'newCOMMUNICATOR', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['STRING', 'INFO', 'RANK', 'COMMUNICATOR', 'newCOMMUNICATOR'])}),
    'MPI_Comm_c2f': (False, {2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE']), 1: ([True], ['COMMUNICATOR'])}),
    'MPI_Comm_call_errhandler': (False, {3: ([True, True, False], ['COMMUNICATOR', 'ERROR_CODE']),
                                         2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE'])}), 'MPI_Comm_compare': (
        False, {4: ([True, False, True, True], ['COMMUNICATOR', 'COMM_COMPARISON', 'ERROR_CODE']),
                3: ([True, False, True], ['COMMUNICATOR', 'COMM_COMPARISON'])}), 'MPI_Comm_connect': (False, {6: (
        [True, True, True, True, True, True],
        ['STRING', 'INFO', 'RANK', 'COMMUNICATOR', 'newCOMMUNICATOR', 'ERROR_CODE']),
        5: (
            [True, True,
             True, True,
             True],
            ['STRING',
             'INFO',
             'RANK',
             'COMMUNICATOR',
             'newCOMMUNICATOR'])}),
    'MPI_Comm_copy_attr_function': (False, {7: ([True, True, True, True, False, True, True],
                                                ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL',
                                                 'ERROR_CODE']), 6: (
        [True, True, True, True, False, True], ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_Comm_create': (False,
                        {4: ([True, True, True, True], ['COMMUNICATOR', 'GROUP', 'newCOMMUNICATOR', 'ERROR_CODE']),
                         3: ([True, True, True], ['COMMUNICATOR', 'GROUP', 'newCOMMUNICATOR'])}),
    'MPI_Comm_create_errhandler': (False, {3: ([True, True, True], ['FUNCTION', 'ERRHANDLER', 'ERROR_CODE']),
                                           2: ([True, True], ['FUNCTION', 'ERRHANDLER'])}),
    'MPI_Comm_create_from_group': (False, {6: (
        [True, True, True, True, True, True],
        ['GROUP', 'STRING', 'INFO', 'ERRHANDLER', 'newCOMMUNICATOR', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['GROUP', 'STRING', 'INFO', 'ERRHANDLER', 'newCOMMUNICATOR'])}),
    'MPI_Comm_create_group': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'GROUP', 'TAG', 'newCOMMUNICATOR', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'GROUP', 'TAG', 'newCOMMUNICATOR'])}),
    'MPI_Comm_create_keyval': (False, {
        5: ([True, False, True, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE', 'ERROR_CODE']),
        4: ([True, False, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE'])}), 'MPI_Comm_delete_attr': (False, {
        3: ([True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ERROR_CODE']),
        2: ([True, True], ['COMMUNICATOR', 'KEYVAL'])}), 'MPI_Comm_delete_attr_function': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE'])}),
    'MPI_Comm_disconnect': (False, {2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE']), 1: ([True], ['COMMUNICATOR'])}),
    'MPI_Comm_dup': (False, {3: ([True, True, True], ['COMMUNICATOR', 'newCOMMUNICATOR', 'ERROR_CODE']),
                             2: ([True, True], ['COMMUNICATOR', 'newCOMMUNICATOR'])}), 'MPI_COMM_DUP_FN': (False, {7: (
        [True, True, True, True, False, True, True],
        ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']), 6: (
        [True, True, True, True, False, True], ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_Comm_dup_with_info': (False, {
        4: ([True, True, True, True], ['COMMUNICATOR', 'INFO', 'newCOMMUNICATOR', 'ERROR_CODE']),
        3: ([True, True, True], ['COMMUNICATOR', 'INFO', 'newCOMMUNICATOR'])}),
    'MPI_Comm_errhandler_function': (True, {2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE'])}),
    'MPI_Comm_f2c': (False, {2: ([True, True], ['F90_COMM', 'ERROR_CODE']), 1: ([True], ['F90_COMM'])}),
    'MPI_Comm_free': (False, {2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE']), 1: ([True], ['COMMUNICATOR'])}),
    'MPI_Comm_free_keyval': (False, {2: ([True, True], ['KEYVAL', 'ERROR_CODE']), 1: ([True], ['KEYVAL'])}),
    'MPI_Comm_get_attr': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_Comm_get_errhandler': (False, {3: ([True, True, True], ['COMMUNICATOR', 'ERRHANDLER', 'ERROR_CODE']),
                                        2: ([True, True], ['COMMUNICATOR', 'ERRHANDLER'])}), 'MPI_Comm_get_info': (
        False,
        {3: ([True, True, True], ['COMMUNICATOR', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['COMMUNICATOR', 'INFO'])}),
    'MPI_Comm_get_name': (False,
                          {4: ([True, True, True, True], ['COMMUNICATOR', 'STRING', 'STRING_LENGTH', 'ERROR_CODE']),
                           3: ([True, True, True], ['COMMUNICATOR', 'STRING', 'STRING_LENGTH'])}),
    'MPI_Comm_get_parent': (False, {2: ([True, True], ['COMMUNICATOR', 'ERROR_CODE']), 1: ([True], ['COMMUNICATOR'])}),
    'MPI_Comm_group': (False, {3: ([True, True, True], ['COMMUNICATOR', 'GROUP', 'ERROR_CODE']),
                               2: ([True, True], ['COMMUNICATOR', 'GROUP'])}), 'MPI_Comm_idup': (False, {
        4: ([True, True, True, True], ['COMMUNICATOR', 'newCOMMUNICATOR', 'REQUEST', 'ERROR_CODE']),
        3: ([True, True, True], ['COMMUNICATOR', 'newCOMMUNICATOR', 'REQUEST'])}), 'MPI_Comm_idup_with_info': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'INFO', 'newCOMMUNICATOR', 'REQUEST', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'INFO', 'newCOMMUNICATOR', 'REQUEST'])}), 'MPI_Comm_join': (
        False, {3: ([True, True, True], ['FILE_DESCRIPTOR', 'COMMUNICATOR', 'ERROR_CODE']),
                2: ([True, True], ['FILE_DESCRIPTOR', 'COMMUNICATOR'])}), 'MPI_COMM_NULL_COPY_FN': (False, {7: (
        [True, True, True, True, False, True, True],
        ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']), 6: (
        [True, True, True, True, False, True], ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_COMM_NULL_DELETE_FN': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE'])}), 'MPI_Comm_rank': (
        False,
        {3: ([True, True, True], ['COMMUNICATOR', 'RANK', 'ERROR_CODE']), 2: ([True, True], ['COMMUNICATOR', 'RANK'])}),
    'MPI_Comm_remote_group': (False, {3: ([True, True, True], ['COMMUNICATOR', 'GROUP', 'ERROR_CODE']),
                                      2: ([True, True], ['COMMUNICATOR', 'GROUP'])}), 'MPI_Comm_remote_size': (False, {
        3: ([True, True, True], ['COMMUNICATOR', 'COMM_SIZE', 'ERROR_CODE']),
        2: ([True, True], ['COMMUNICATOR', 'COMM_SIZE'])}), 'MPI_Comm_set_attr': (False, {
        4: ([True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL', 'ERROR_CODE']),
        3: ([True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL'])}), 'MPI_Comm_set_errhandler': (False, {
        3: ([True, True, True], ['COMMUNICATOR', 'ERRHANDLER', 'ERROR_CODE']),
        2: ([True, True], ['COMMUNICATOR', 'ERRHANDLER'])}), 'MPI_Comm_set_info': (False, {
        3: ([True, True, True], ['COMMUNICATOR', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['COMMUNICATOR', 'INFO'])}),
    'MPI_Comm_set_name': (False, {3: ([True, True, True], ['COMMUNICATOR', 'STRING', 'ERROR_CODE']),
                                  2: ([True, True], ['COMMUNICATOR', 'STRING'])}), 'MPI_Comm_size': (False, {
        3: ([True, True, True], ['COMMUNICATOR', 'COMM_SIZE', 'ERROR_CODE']),
        2: ([True, True], ['COMMUNICATOR', 'COMM_SIZE'])}), 'MPI_Comm_spawn': (False, {9: (
        [True, True, True, True, True, True, False, True, False],
        ['STRING', 'STRING_ARRAY', 'COMM_SIZE', 'INFO', 'RANK', 'COMMUNICATOR', 'ERROR_CODE']), 8: (
        [True, True, True, True, True, True, False, True],
        ['STRING', 'STRING_ARRAY', 'COMM_SIZE', 'INFO', 'RANK', 'COMMUNICATOR', 'ERROR_CODE'])}),
    'MPI_Comm_spawn_multiple': (False, {10: ([True, True, True, True, True, True, True, False, True, False],
                                             ['ARRAY_LENGTH_PI', 'STRING_ARRAY', 'STRING_2DARRAY', 'COMM_SIZE', 'INFO',
                                              'RANK', 'COMMUNICATOR', 'ERROR_CODE']), 9: (
        [True, True, True, True, True, True, True, False, True],
        ['ARRAY_LENGTH_PI', 'STRING_ARRAY', 'STRING_2DARRAY', 'COMM_SIZE', 'INFO', 'RANK', 'COMMUNICATOR',
         'ERROR_CODE'])}),
    'MPI_Comm_split': (False, {
        5: ([True, True, True, True, True], ['COMMUNICATOR', 'COLOR', 'KEY', 'newCOMMUNICATOR', 'ERROR_CODE']),
        4: ([True, True, True, True], ['COMMUNICATOR', 'COLOR', 'KEY', 'newCOMMUNICATOR'])}), 'MPI_Comm_split_type': (
        False, {6: ([True, True, True, True, True, True],
                    ['COMMUNICATOR', 'SPLIT_TYPE', 'KEY', 'INFO', 'newCOMMUNICATOR', 'ERROR_CODE']),
                5: ([True, True, True, True, True], ['COMMUNICATOR', 'SPLIT_TYPE', 'KEY', 'INFO', 'newCOMMUNICATOR'])}),
    'MPI_Comm_test_inter': (False, {3: ([True, True, True], ['COMMUNICATOR', 'LOGICAL', 'ERROR_CODE']),
                                    2: ([True, True], ['COMMUNICATOR', 'LOGICAL'])}), 'MPI_Compare_and_swap': (False, {
        8: ([True, False, False, True, True, True, True, True],
            ['BUFFER', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'WINDOW', 'ERROR_CODE']), 7: (
            [True, False, False, True, True, True, True],
            ['BUFFER', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'WINDOW'])}),
    'MPI_CONVERSION_FN_NULL': (False, {7: (
        [True, True, True, False, True, True, True],
        ['C_BUFFER3', 'DATATYPE', 'POLYXFER_NUM_ELEM', 'OFFSET', 'EXTRA_STATE', 'ERROR_CODE']), 6: (
        [True, True, True, False, True, True],
        ['C_BUFFER3', 'DATATYPE', 'POLYXFER_NUM_ELEM', 'OFFSET', 'EXTRA_STATE'])}),
    'MPI_Copy_function': (False, {7: ([True, True, True, True, False, True, True],
                                      ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE2', 'ATTRIBUTE_VAL_10', 'LOGICAL',
                                       'ERROR_CODE']), 6: (
        [True, True, True, True, False, True],
        ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE2', 'ATTRIBUTE_VAL_10', 'LOGICAL'])}),
    'MPI_Datarep_conversion_function': (False, {7: ([True, True, True, False, True, True, True],
                                                    ['C_BUFFER3', 'DATATYPE', 'POLYXFER_NUM_ELEM', 'OFFSET',
                                                     'EXTRA_STATE', 'ERROR_CODE']), 6: (
        [True, True, True, False, True, True],
        ['C_BUFFER3', 'DATATYPE', 'POLYXFER_NUM_ELEM', 'OFFSET', 'EXTRA_STATE'])}),
    'MPI_Datarep_extent_function': (False, {
        4: ([True, True, True, True], ['DATATYPE', 'DISPOFFSET_SMALL', 'EXTRA_STATE', 'ERROR_CODE']),
        3: ([True, True, True], ['DATATYPE', 'DISPOFFSET_SMALL', 'EXTRA_STATE'])}), 'MPI_Delete_function': (False, {5: (
        [True, True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10', 'EXTRA_STATE2', 'ERROR_CODE']),
        4: (
            [True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10', 'EXTRA_STATE2'])}),
    'MPI_Dims_create': (
        False, {4: ([True, True, True, True], ['COMM_SIZE', 'NUM_DIMS', 'DIMENSION', 'ERROR_CODE']),
                3: ([True, True, True], ['COMM_SIZE', 'NUM_DIMS', 'DIMENSION'])}),
    'MPI_Dist_graph_create': (False, {10: (
        [True, True, True, True, False, True, True, True, False, True],
        ['COMMUNICATOR', 'ARRAY_LENGTH_NNI', 'RANK_NNI', 'DEGREE', 'WEIGHT', 'INFO', 'LOGICAL', 'ERROR_CODE']), 9: (
        [True, True, True, True, False, True, True, True, False],
        ['COMMUNICATOR', 'ARRAY_LENGTH_NNI', 'RANK_NNI', 'DEGREE', 'WEIGHT', 'INFO', 'LOGICAL'])}),
    'MPI_Dist_graph_create_adjacent': (False, {11: (
        [True, True, True, True, False, False, False, True, True, False, True],
        ['COMMUNICATOR', 'DEGREE', 'RANK_NNI', 'WEIGHT', 'INFO', 'LOGICAL', 'ERROR_CODE']), 10: (
        [True, True, True, True, False, False, False, True, True, False],
        ['COMMUNICATOR', 'DEGREE', 'RANK_NNI', 'WEIGHT', 'INFO', 'LOGICAL'])}),
    'MPI_Dist_graph_neighbors': (False, {8: (
        [True, True, True, True, False, False, False, True],
        ['COMMUNICATOR', 'ARRAY_LENGTH_NNI', 'RANK_NNI', 'WEIGHT', 'ERROR_CODE']), 7: (
        [True, True, True, True, False, False, False], ['COMMUNICATOR', 'ARRAY_LENGTH_NNI', 'RANK_NNI', 'WEIGHT'])}),
    'MPI_Dist_graph_neighbors_count': (False, {
        5: ([True, True, False, True, True], ['COMMUNICATOR', 'DEGREE', 'LOGICAL', 'ERROR_CODE']),
        4: ([True, True, False, True], ['COMMUNICATOR', 'DEGREE', 'LOGICAL'])}), 'MPI_DUP_FN': (False, {7: (
        [True, True, True, True, False, True, True],
        ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE2', 'ATTRIBUTE_VAL_10', 'LOGICAL', 'ERROR_CODE']), 6: (
        [True, True, True, True, False, True],
        ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE2', 'ATTRIBUTE_VAL_10', 'LOGICAL'])}),
    'MPI_Errhandler_c2f': (False, {2: ([True, True], ['ERRHANDLER', 'ERROR_CODE']), 1: ([True], ['ERRHANDLER'])}),
    'MPI_Errhandler_f2c': (
        False, {2: ([True, True], ['F90_ERRHANDLER', 'ERROR_CODE']), 1: ([True], ['F90_ERRHANDLER'])}),
    'MPI_Errhandler_free': (False, {2: ([True, True], ['ERRHANDLER', 'ERROR_CODE']), 1: ([True], ['ERRHANDLER'])}),
    'MPI_Error_class': (
        False,
        {3: ([True, True, False], ['ERROR_CODE', 'ERROR_CLASS']), 2: ([True, True], ['ERROR_CODE', 'ERROR_CLASS'])}),
    'MPI_Error_string': (False, {4: ([True, True, True, False], ['ERROR_CODE', 'STRING', 'STRING_LENGTH']),
                                 3: ([True, True, True], ['ERROR_CODE', 'STRING', 'STRING_LENGTH'])}), 'MPI_Exscan': (
        False, {7: ([True, False, True, True, True, True, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'ERROR_CODE']), 6: (
            [True, False, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR'])}),
    'MPI_Exscan_init': (False, {9: (
        [True, False, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']),
        8: (
            [True, False, True, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_F_sync_reg': (False, {1: ([True], ['BUFFER'])}), 'MPI_Fetch_and_op': (False, {8: (
        [True, False, True, True, True, True, True, True],
        ['BUFFER', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'OPERATION', 'WINDOW', 'ERROR_CODE']), 7: (
        [True, False, True, True, True, True, True],
        ['BUFFER', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'OPERATION', 'WINDOW'])}),
    'MPI_File_c2f': (False, {2: ([True, True], ['FILE', 'ERROR_CODE']), 1: ([True], ['FILE'])}),
    'MPI_File_call_errhandler': (
        False, {3: ([True, True, False], ['FILE', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'ERROR_CODE'])}),
    'MPI_File_close': (False, {2: ([True, True], ['FILE', 'ERROR_CODE']), 1: ([True], ['FILE'])}),
    'MPI_File_create_errhandler': (False, {3: ([True, True, True], ['FUNCTION', 'ERRHANDLER', 'ERROR_CODE']),
                                           2: ([True, True], ['FUNCTION', 'ERRHANDLER'])}), 'MPI_File_delete': (
        False, {3: ([True, True, True], ['STRING', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['STRING', 'INFO'])}),
    'MPI_File_errhandler_function': (True, {2: ([True, True], ['FILE', 'ERROR_CODE'])}),
    'MPI_File_f2c': (False, {2: ([True, True], ['F90_FILE', 'ERROR_CODE']), 1: ([True], ['F90_FILE'])}),
    'MPI_File_get_amode': (False, {3: ([True, True, True], ['FILE', 'ACCESS_MODE', 'ERROR_CODE']),
                                   2: ([True, True], ['FILE', 'ACCESS_MODE'])}), 'MPI_File_get_atomicity': (
        False, {3: ([True, True, True], ['FILE', 'LOGICAL', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'LOGICAL'])}),
    'MPI_File_get_byte_offset': (False, {4: ([True, True, False, True], ['FILE', 'OFFSET', 'ERROR_CODE']),
                                         3: ([True, True, False], ['FILE', 'OFFSET'])}), 'MPI_File_get_errhandler': (
        False,
        {3: ([True, True, True], ['FILE', 'ERRHANDLER', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'ERRHANDLER'])}),
    'MPI_File_get_group': (
        False, {3: ([True, True, True], ['FILE', 'GROUP', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'GROUP'])}),
    'MPI_File_get_info': (
        False, {3: ([True, True, True], ['FILE', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'INFO'])}),
    'MPI_File_get_position': (
        False, {3: ([True, True, True], ['FILE', 'OFFSET', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'OFFSET'])}),
    'MPI_File_get_position_shared': (
        False, {3: ([True, True, True], ['FILE', 'OFFSET', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'OFFSET'])}),
    'MPI_File_get_size': (
        False, {3: ([True, True, True], ['FILE', 'OFFSET', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'OFFSET'])}),
    'MPI_File_get_type_extent': (False,
                                 {4: ([True, True, True, True], ['FILE', 'DATATYPE', 'POLYDISPOFFSET', 'ERROR_CODE']),
                                  3: ([True, True, True], ['FILE', 'DATATYPE', 'POLYDISPOFFSET'])}),
    'MPI_File_get_view': (False, {
        6: ([True, True, True, False, True, True], ['FILE', 'OFFSET', 'DATATYPE', 'STRING', 'ERROR_CODE']),
        5: ([True, True, True, False, True], ['FILE', 'OFFSET', 'DATATYPE', 'STRING'])}), 'MPI_File_iread': (False, {
        6: ([True, True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST', 'ERROR_CODE']),
        5: ([True, True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iread_all': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iread_at': (False, {7: ([True, True, True, True, True, True, True],
                                      ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST',
                                       'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iread_at_all': (False, {7: ([True, True, True, True, True, True, True],
                                          ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST',
                                           'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iread_shared': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iwrite': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iwrite_all': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iwrite_at': (False, {7: ([True, True, True, True, True, True, True],
                                       ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST',
                                        'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iwrite_at_all': (False, {7: ([True, True, True, True, True, True, True],
                                           ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST',
                                            'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_iwrite_shared': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'REQUEST'])}),
    'MPI_File_open': (False, {6: (
        [True, True, True, True, True, True], ['COMMUNICATOR', 'STRING', 'ACCESS_MODE', 'INFO', 'FILE', 'ERROR_CODE']),
        5: (
            [True, True, True, True, True], ['COMMUNICATOR', 'STRING', 'ACCESS_MODE', 'INFO', 'FILE'])}),
    'MPI_File_preallocate': (
        False, {3: ([True, True, True], ['FILE', 'OFFSET', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'OFFSET'])}),
    'MPI_File_read': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_read_all': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_read_all_begin': (False, {
        5: ([True, True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE'])}), 'MPI_File_read_all_end': (
        False, {4: ([True, True, True, True], ['FILE', 'BUFFER', 'STATUS', 'ERROR_CODE']),
                3: ([True, True, True], ['FILE', 'BUFFER', 'STATUS'])}), 'MPI_File_read_at': (False, {7: (
        [True, True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_read_at_all': (False, {7: ([True, True, True, True, True, True, True],
                                         ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS',
                                          'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_read_at_all_begin': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE'])}),
    'MPI_File_read_at_all_end': (False, {4: ([True, True, True, True], ['FILE', 'BUFFER', 'STATUS', 'ERROR_CODE']),
                                         3: ([True, True, True], ['FILE', 'BUFFER', 'STATUS'])}),
    'MPI_File_read_ordered': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_read_ordered_begin': (False, {
        5: ([True, True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE'])}),
    'MPI_File_read_ordered_end': (False, {4: ([True, True, True, True], ['FILE', 'BUFFER', 'STATUS', 'ERROR_CODE']),
                                          3: ([True, True, True], ['FILE', 'BUFFER', 'STATUS'])}),
    'MPI_File_read_shared': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_seek': (False, {4: ([True, True, True, True], ['FILE', 'OFFSET', 'UPDATE_MODE', 'ERROR_CODE']),
                              3: ([True, True, True], ['FILE', 'OFFSET', 'UPDATE_MODE'])}), 'MPI_File_seek_shared': (
        False, {4: ([True, True, True, True], ['FILE', 'OFFSET', 'UPDATE_MODE', 'ERROR_CODE']),
                3: ([True, True, True], ['FILE', 'OFFSET', 'UPDATE_MODE'])}), 'MPI_File_set_atomicity': (
        False, {3: ([True, True, True], ['FILE', 'LOGICAL', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'LOGICAL'])}),
    'MPI_File_set_errhandler': (
        False,
        {3: ([True, True, True], ['FILE', 'ERRHANDLER', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'ERRHANDLER'])}),
    'MPI_File_set_info': (
        False, {3: ([True, True, True], ['FILE', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'INFO'])}),
    'MPI_File_set_size': (
        False, {3: ([True, True, True], ['FILE', 'OFFSET', 'ERROR_CODE']), 2: ([True, True], ['FILE', 'OFFSET'])}),
    'MPI_File_set_view': (False, {7: (
        [True, True, True, False, True, True, True], ['FILE', 'OFFSET', 'DATATYPE', 'STRING', 'INFO', 'ERROR_CODE']),
        6: (
            [True, True, True, False, True, True], ['FILE', 'OFFSET', 'DATATYPE', 'STRING', 'INFO'])}),
    'MPI_File_sync': (False, {2: ([True, True], ['FILE', 'ERROR_CODE']), 1: ([True], ['FILE'])}), 'MPI_File_write': (
        False, {6: (
            [True, True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
            5: ([True, True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_write_all': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_write_all_begin': (False, {
        5: ([True, True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE'])}),
    'MPI_File_write_all_end': (False, {4: ([True, True, True, True], ['FILE', 'BUFFER', 'STATUS', 'ERROR_CODE']),
                                       3: ([True, True, True], ['FILE', 'BUFFER', 'STATUS'])}), 'MPI_File_write_at': (
        False, {7: ([True, True, True, True, True, True, True],
                    ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']), 6: (
            [True, True, True, True, True, True],
            ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_write_at_all': (False, {7: ([True, True, True, True, True, True, True],
                                          ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS',
                                           'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_write_at_all_begin': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'OFFSET', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE'])}),
    'MPI_File_write_at_all_end': (False, {4: ([True, True, True, True], ['FILE', 'BUFFER', 'STATUS', 'ERROR_CODE']),
                                          3: ([True, True, True], ['FILE', 'BUFFER', 'STATUS'])}),
    'MPI_File_write_ordered': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_File_write_ordered_begin': (False, {
        5: ([True, True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE'])}),
    'MPI_File_write_ordered_end': (False, {4: ([True, True, True, True], ['FILE', 'BUFFER', 'STATUS', 'ERROR_CODE']),
                                           3: ([True, True, True], ['FILE', 'BUFFER', 'STATUS'])}),
    'MPI_File_write_shared': (False, {6: (
        [True, True, True, True, True, True],
        ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True],
            ['FILE', 'BUFFER', 'POLYXFER_NUM_ELEM', 'DATATYPE', 'STATUS'])}),
    'MPI_Finalize': (False, {1: ([True], ['ERROR_CODE']), 0: ([], [])}),
    'MPI_Finalized': (False, {2: ([True, True], ['LOGICAL', 'ERROR_CODE']), 1: ([True], ['LOGICAL'])}),
    'MPI_Free_mem': (False, {2: ([True, True], ['BUFFER', 'ERROR_CODE']), 1: ([True], ['BUFFER'])}), 'MPI_Gather': (
        False, {9: ([True, True, True, False, False, False, True, True, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'ERROR_CODE']), 8: (
            [True, True, True, False, False, False, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR'])}),
    'MPI_Gather_init': (False, {11: (
        [True, True, True, False, False, False, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']), 10: (
        [True, True, True, False, False, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'INFO', 'REQUEST'])}), 'MPI_Gatherv': (
        False, {10: ([True, True, True, False, False, True, False, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'RANK', 'COMMUNICATOR',
                      'ERROR_CODE']), 9: ([True, True, True, False, False, True, False, True, True],
                                          ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'RANK',
                                           'COMMUNICATOR'])}), 'MPI_Gatherv_init': (False, {12: (
        [True, True, True, False, False, True, False, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'RANK', 'COMMUNICATOR', 'INFO', 'REQUEST',
         'ERROR_CODE']), 11: ([True, True, True, False, False, True, False, True, True, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'RANK',
                               'COMMUNICATOR',
                               'INFO', 'REQUEST'])}), 'MPI_Get': (False, {9: (
        [True, True, True, True, True, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'WINDOW', 'ERROR_CODE']),
        8: (
            [True, True, True, True, True, False, False, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'WINDOW'])}),
    'MPI_Get_accumulate': (False, {13: (
        [True, True, True, False, False, False, True, True, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'OPERATION', 'WINDOW',
         'ERROR_CODE']), 12: ([True, True, True, False, False, False, True, True, False, False, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI',
                               'OPERATION', 'WINDOW'])}), 'MPI_Get_address': (False, {
        3: ([True, True, True], ['BUFFER', 'DISPLACEMENT', 'ERROR_CODE']),
        2: ([True, True], ['BUFFER', 'DISPLACEMENT'])}), 'MPI_Get_count': (False, {
        4: ([True, True, True, True], ['STATUS', 'DATATYPE', 'POLYXFER_NUM_ELEM', 'ERROR_CODE']),
        3: ([True, True, True], ['STATUS', 'DATATYPE', 'POLYXFER_NUM_ELEM'])}), 'MPI_Get_elements': (False, {
        4: ([True, True, True, True], ['STATUS', 'DATATYPE', 'POLYDTYPE_NUM_ELEM', 'ERROR_CODE']),
        3: ([True, True, True], ['STATUS', 'DATATYPE', 'POLYDTYPE_NUM_ELEM'])}), 'MPI_Get_elements_x': (False, {
        4: ([True, True, True, True], ['STATUS', 'DATATYPE', 'NUM_BYTES', 'ERROR_CODE']),
        3: ([True, True, True], ['STATUS', 'DATATYPE', 'NUM_BYTES'])}), 'MPI_Get_library_version': (False, {
        3: ([True, True, True], ['STRING', 'STRING_LENGTH', 'ERROR_CODE']),
        2: ([True, True], ['STRING', 'STRING_LENGTH'])}), 'MPI_Get_processor_name': (False, {
        3: ([True, True, True], ['STRING', 'STRING_LENGTH', 'ERROR_CODE']),
        2: ([True, True], ['STRING', 'STRING_LENGTH'])}),
    'MPI_Get_version': (False, {3: ([True, False, True], ['VERSION', 'ERROR_CODE']), 2: ([True, False], ['VERSION'])}),
    'MPI_Graph_create': (False, {7: ([True, True, True, True, True, False, True],
                                     ['COMMUNICATOR', 'COMM_SIZE', 'INDEX', 'RANK', 'LOGICAL', 'ERROR_CODE']), 6: (
        [True, True, True, True, True, False], ['COMMUNICATOR', 'COMM_SIZE', 'INDEX', 'RANK', 'LOGICAL'])}),
    'MPI_Graph_get': (False, {
        6: ([True, True, False, True, True, True], ['COMMUNICATOR', 'ARRAY_LENGTH', 'INDEX', 'RANK', 'ERROR_CODE']),
        5: ([True, True, False, True, True], ['COMMUNICATOR', 'ARRAY_LENGTH', 'INDEX', 'RANK'])}), 'MPI_Graph_map': (
        False, {6: (
            [True, True, True, True, True, True],
            ['COMMUNICATOR', 'ARRAY_LENGTH', 'INDEX', 'RANK', 'newRANK', 'ERROR_CODE']),
            5: ([True, True, True, True, True], ['COMMUNICATOR', 'ARRAY_LENGTH', 'INDEX', 'RANK', 'newRANK'])}),
    'MPI_Graph_neighbors': (False, {
        5: ([True, True, True, False, True], ['COMMUNICATOR', 'RANK', 'ARRAY_LENGTH', 'ERROR_CODE']),
        4: ([True, True, True, False], ['COMMUNICATOR', 'RANK', 'ARRAY_LENGTH'])}), 'MPI_Graph_neighbors_count': (False,
                                                                                                                  {4: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'COMMUNICATOR',
                                                                                                                          'RANK',
                                                                                                                          'ARRAY_LENGTH',
                                                                                                                          'ERROR_CODE']),
                                                                                                                      3: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'COMMUNICATOR',
                                                                                                                          'RANK',
                                                                                                                          'ARRAY_LENGTH'])}),
    'MPI_Graphdims_get': (False, {4: ([True, True, False, True], ['COMMUNICATOR', 'ARRAY_LENGTH', 'ERROR_CODE']),
                                  3: ([True, True, False], ['COMMUNICATOR', 'ARRAY_LENGTH'])}),
    'MPI_Grequest_cancel_function': (False, {3: ([True, True, True], ['EXTRA_STATE', 'LOGICAL', 'ERROR_CODE']),
                                             2: ([True, True], ['EXTRA_STATE', 'LOGICAL'])}),
    'MPI_Grequest_complete': (False, {2: ([True, True], ['REQUEST', 'ERROR_CODE']), 1: ([True], ['REQUEST'])}),
    'MPI_Grequest_free_function': (
        False, {2: ([True, True], ['EXTRA_STATE', 'ERROR_CODE']), 1: ([True], ['EXTRA_STATE'])}),
    'MPI_Grequest_query_function': (False, {3: ([True, True, True], ['EXTRA_STATE', 'STATUS', 'ERROR_CODE']),
                                            2: ([True, True], ['EXTRA_STATE', 'STATUS'])}), 'MPI_Grequest_start': (
        False, {6: ([True, False, False, True, True, True], ['FUNCTION', 'EXTRA_STATE', 'REQUEST', 'ERROR_CODE']),
                5: ([True, False, False, True, True], ['FUNCTION', 'EXTRA_STATE', 'REQUEST'])}),
    'MPI_Group_c2f': (False, {2: ([True, True], ['GROUP', 'ERROR_CODE']), 1: ([True], ['GROUP'])}),
    'MPI_Group_compare': (False, {4: ([True, False, True, True], ['GROUP', 'GROUP_COMPARISON', 'ERROR_CODE']),
                                  3: ([True, False, True], ['GROUP', 'GROUP_COMPARISON'])}), 'MPI_Group_difference': (
        False, {4: ([True, False, True, True], ['GROUP', 'newGROUP', 'ERROR_CODE']),
                3: ([True, False, True], ['GROUP', 'newGROUP'])}), 'MPI_Group_excl': (False, {
        5: ([True, True, True, True, True], ['GROUP', 'ARRAY_LENGTH', 'RANK', 'newGROUP', 'ERROR_CODE']),
        4: ([True, True, True, True], ['GROUP', 'ARRAY_LENGTH', 'RANK', 'newGROUP'])}),
    'MPI_Group_f2c': (False, {2: ([True, True], ['F90_GROUP', 'ERROR_CODE']), 1: ([True], ['F90_GROUP'])}),
    'MPI_Group_free': (False, {2: ([True, True], ['GROUP', 'ERROR_CODE']), 1: ([True], ['GROUP'])}),
    'MPI_Group_from_session_pset': (False,
                                    {4: ([True, True, True, True], ['SESSION', 'STRING', 'newGROUP', 'ERROR_CODE']),
                                     3: ([True, True, True], ['SESSION', 'STRING', 'newGROUP'])}), 'MPI_Group_incl': (
        False, {5: ([True, True, True, True, True], ['GROUP', 'ARRAY_LENGTH', 'RANK', 'newGROUP', 'ERROR_CODE']),
                4: ([True, True, True, True], ['GROUP', 'ARRAY_LENGTH', 'RANK', 'newGROUP'])}),
    'MPI_Group_intersection': (
        False, {4: ([True, False, True, True], ['GROUP', 'newGROUP', 'ERROR_CODE']),
                3: ([True, False, True], ['GROUP', 'newGROUP'])}), 'MPI_Group_range_excl': (False, {
        5: ([True, True, True, True, True], ['GROUP', 'ARRAY_LENGTH', 'RANK', 'newGROUP', 'ERROR_CODE']),
        4: ([True, True, True, True], ['GROUP', 'ARRAY_LENGTH', 'RANK', 'newGROUP'])}), 'MPI_Group_range_incl': (False,
                                                                                                                 {5: (
                                                                                                                     [
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         True],
                                                                                                                     [
                                                                                                                         'GROUP',
                                                                                                                         'ARRAY_LENGTH',
                                                                                                                         'RANK',
                                                                                                                         'newGROUP',
                                                                                                                         'ERROR_CODE']),
                                                                                                                     4: (
                                                                                                                         [
                                                                                                                             True,
                                                                                                                             True,
                                                                                                                             True,
                                                                                                                             True],
                                                                                                                         [
                                                                                                                             'GROUP',
                                                                                                                             'ARRAY_LENGTH',
                                                                                                                             'RANK',
                                                                                                                             'newGROUP'])}),
    'MPI_Group_rank': (
        False, {3: ([True, True, True], ['GROUP', 'RANK', 'ERROR_CODE']), 2: ([True, True], ['GROUP', 'RANK'])}),
    'MPI_Group_size': (
        False,
        {3: ([True, True, True], ['GROUP', 'COMM_SIZE', 'ERROR_CODE']), 2: ([True, True], ['GROUP', 'COMM_SIZE'])}),
    'MPI_Group_translate_ranks': (False, {
        6: ([True, True, True, False, False, True], ['GROUP', 'ARRAY_LENGTH', 'RANK', 'ERROR_CODE']),
        5: ([True, True, True, False, False], ['GROUP', 'ARRAY_LENGTH', 'RANK'])}), 'MPI_Group_union': (False, {
        4: ([True, False, True, True], ['GROUP', 'newGROUP', 'ERROR_CODE']),
        3: ([True, False, True], ['GROUP', 'newGROUP'])}), 'MPI_Iallgather': (False, {9: (
        [True, True, True, False, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 8: (
        [True, True, True, False, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'REQUEST'])}), 'MPI_Iallgatherv': (False, {10: (
        [True, True, True, False, False, True, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']),
        9: (
            [True, True, True, False, False, True, False, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Iallreduce': (False, {8: ([True, False, True, True, True, True, True, True],
                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR',
                                    'REQUEST', 'ERROR_CODE']), 7: ([True, False, True, True, True, True, True],
                                                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE',
                                                                    'OPERATION', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ialltoall': (False, {9: ([True, True, True, False, False, False, True, True, True],
                                  ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'REQUEST',
                                   'ERROR_CODE']), 8: ([True, True, True, False, False, False, True, True],
                                                       ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR',
                                                        'REQUEST'])}), 'MPI_Ialltoallv': (False, {11: (
        [True, True, True, True, False, False, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']),
        10: (
            [True, True, True, True, False, False, False, False, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ialltoallw': (False, {11: ([True, True, True, True, False, False, False, False, True, True, True],
                                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR',
                                     'REQUEST', 'ERROR_CODE']), 10: (
        [True, True, True, True, False, False, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ibarrier': (
        False, {3: ([True, True, True], ['COMMUNICATOR', 'REQUEST', 'ERROR_CODE']),
                2: ([True, True], ['COMMUNICATOR', 'REQUEST'])}), 'MPI_Ibcast': (False, {7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ibsend': (False, {8: (
        [True, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Iexscan': (False,
                    {8: (
                        [True,
                         False,
                         True,
                         True,
                         True,
                         True,
                         True,
                         True],
                        [
                            'BUFFER',
                            'POLYXFER_NUM_ELEM_NNI',
                            'DATATYPE',
                            'OPERATION',
                            'COMMUNICATOR',
                            'REQUEST',
                            'ERROR_CODE']),
                        7: ([
                                True,
                                False,
                                True,
                                True,
                                True,
                                True,
                                True],
                            [
                                'BUFFER',
                                'POLYXFER_NUM_ELEM_NNI',
                                'DATATYPE',
                                'OPERATION',
                                'COMMUNICATOR',
                                'REQUEST'])}),
    'MPI_Igather': (False, {10: ([True, True, True, False, False, False, True, True, True, True],
                                 ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'REQUEST',
                                  'ERROR_CODE']), 9: ([True, True, True, False, False, False, True, True, True],
                                                      ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK',
                                                       'COMMUNICATOR', 'REQUEST'])}), 'MPI_Igatherv': (False, {11: (
        [True, True, True, False, False, True, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'RANK', 'COMMUNICATOR', 'REQUEST',
         'ERROR_CODE']), 10: ([True, True, True, False, False, True, False, True, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'RANK',
                               'COMMUNICATOR',
                               'REQUEST'])}), 'MPI_Improbe': (False, {7: ([True, True, True, True, True, True, True],
                                                                          ['RANK', 'TAG', 'COMMUNICATOR', 'LOGICAL',
                                                                           'MESSAGE', 'STATUS', 'ERROR_CODE']), 6: (
        [True, True, True, True, True, True], ['RANK', 'TAG', 'COMMUNICATOR', 'LOGICAL', 'MESSAGE', 'STATUS'])}),
    'MPI_Imrecv': (False, {6: ([True, True, True, True, True, True],
                               ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'MESSAGE', 'REQUEST', 'ERROR_CODE']),
                           5: ([True, True, True, True, True],
                               ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'MESSAGE', 'REQUEST'])}),
    'MPI_Ineighbor_allgather': (False, {9: ([True, True, True, False, False, False, True, True, True],
                                            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'REQUEST',
                                             'ERROR_CODE']), 8: ([True, True, True, False, False, False, True, True],
                                                                 ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE',
                                                                  'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ineighbor_allgatherv': (False, {10: ([True, True, True, False, False, True, False, True, True, True],
                                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT',
                                               'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, False, False, True, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ineighbor_alltoall': (False, {9: ([True, True, True, False, False, False, True, True, True],
                                           ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'REQUEST',
                                            'ERROR_CODE']), 8: ([True, True, True, False, False, False, True, True],
                                                                ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE',
                                                                 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ineighbor_alltoallv': (False, {11: ([True, True, True, True, False, False, False, False, True, True, True],
                                             ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE',
                                              'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 10: (
        [True, True, True, True, False, False, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ineighbor_alltoallw': (False, {11: ([True, True, True, True, False, False, False, False, True, True, True],
                                             ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DISPLACEMENT', 'DATATYPE',
                                              'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 10: (
        [True, True, True, True, False, False, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Info_c2f': (False, {2: ([True, True], ['INFO', 'ERROR_CODE']), 1: ([True], ['INFO'])}),
    'MPI_Info_create': (False, {2: ([True, True], ['INFO', 'ERROR_CODE']), 1: ([True], ['INFO'])}),
    'MPI_Info_create_env': (False,
                            {4: ([True, True, True, True], ['ARGUMENT_COUNT', 'ARGUMENT_LIST', 'INFO', 'ERROR_CODE']),
                             2: ([True, True], ['INFO', 'ERROR_CODE']),
                             3: ([True, True, True], ['ARGUMENT_COUNT', 'ARGUMENT_LIST', 'INFO']),
                             1: ([True], ['INFO'])}), 'MPI_Info_delete': (
        False, {3: ([True, True, True], ['INFO', 'STRING', 'ERROR_CODE']), 2: ([True, True], ['INFO', 'STRING'])}),
    'MPI_Info_dup': (
        False, {3: ([True, True, True], ['INFO', 'newINFO', 'ERROR_CODE']), 2: ([True, True], ['INFO', 'newINFO'])}),
    'MPI_Info_f2c': (False, {2: ([True, True], ['F90_INFO', 'ERROR_CODE']), 1: ([True], ['F90_INFO'])}),
    'MPI_Info_free': (False, {2: ([True, True], ['INFO', 'ERROR_CODE']), 1: ([True], ['INFO'])}), 'MPI_Info_get': (
        False,
        {6: ([True, True, True, False, True, True], ['INFO', 'STRING', 'INFO_VALUE_LENGTH', 'LOGICAL', 'ERROR_CODE']),
         5: ([True, True, True, False, True], ['INFO', 'STRING', 'INFO_VALUE_LENGTH', 'LOGICAL'])}),
    'MPI_Info_get_nkeys': (
        False,
        {3: ([True, True, True], ['INFO', 'KEY_INDEX', 'ERROR_CODE']), 2: ([True, True], ['INFO', 'KEY_INDEX'])}),
    'MPI_Info_get_nthkey': (False, {4: ([True, True, True, True], ['INFO', 'KEY_INDEX', 'STRING', 'ERROR_CODE']),
                                    3: ([True, True, True], ['INFO', 'KEY_INDEX', 'STRING'])}), 'MPI_Info_get_string': (
        False,
        {6: ([True, True, True, False, True, True], ['INFO', 'STRING', 'INFO_VALUE_LENGTH', 'LOGICAL', 'ERROR_CODE']),
         5: ([True, True, True, False, True], ['INFO', 'STRING', 'INFO_VALUE_LENGTH', 'LOGICAL'])}),
    'MPI_Info_get_valuelen': (False, {
        5: ([True, True, True, True, True], ['INFO', 'STRING', 'INFO_VALUE_LENGTH', 'LOGICAL', 'ERROR_CODE']),
        4: ([True, True, True, True], ['INFO', 'STRING', 'INFO_VALUE_LENGTH', 'LOGICAL'])}), 'MPI_Info_set': (False, {
        4: ([True, True, False, True], ['INFO', 'STRING', 'ERROR_CODE']),
        3: ([True, True, False], ['INFO', 'STRING'])}), 'MPI_Init': (False, {
        3: ([True, True, True], ['ARGUMENT_COUNT', 'ARGUMENT_LIST', 'ERROR_CODE']), 1: ([True], ['ERROR_CODE']),
        2: ([True, True], ['ARGUMENT_COUNT', 'ARGUMENT_LIST']), 0: ([], [])}), 'MPI_Init_thread': (False, {
        5: ([True, True, True, False, True], ['ARGUMENT_COUNT', 'ARGUMENT_LIST', 'THREAD_LEVEL', 'ERROR_CODE']),
        3: ([True, False, True], ['THREAD_LEVEL', 'ERROR_CODE']),
        4: ([True, True, True, False], ['ARGUMENT_COUNT', 'ARGUMENT_LIST', 'THREAD_LEVEL']),
        2: ([True, False], ['THREAD_LEVEL'])}),
    'MPI_Initialized': (False, {2: ([True, True], ['LOGICAL', 'ERROR_CODE']), 1: ([True], ['LOGICAL'])}),
    'MPI_Intercomm_create': (False, {7: (
        [True, True, False, False, True, True, True], ['COMMUNICATOR', 'RANK', 'TAG', 'newCOMMUNICATOR', 'ERROR_CODE']),
        6: ([True, True, False, False, True, True],
            ['COMMUNICATOR', 'RANK', 'TAG', 'newCOMMUNICATOR'])}),
    'MPI_Intercomm_create_from_groups': (False, {9: ([True, True, False, False, True, True, True, True, True],
                                                     ['GROUP', 'RANK', 'STRING', 'INFO', 'ERRHANDLER',
                                                      'newCOMMUNICATOR', 'ERROR_CODE']), 8: (
        [True, True, False, False, True, True, True, True],
        ['GROUP', 'RANK', 'STRING', 'INFO', 'ERRHANDLER', 'newCOMMUNICATOR'])}), 'MPI_Intercomm_merge': (False, {
        4: ([True, True, True, True], ['COMMUNICATOR', 'LOGICAL', 'newCOMMUNICATOR', 'ERROR_CODE']),
        3: ([True, True, True], ['COMMUNICATOR', 'LOGICAL', 'newCOMMUNICATOR'])}), 'MPI_Iprobe': (False, {
        6: ([True, True, True, True, True, True], ['RANK', 'TAG', 'COMMUNICATOR', 'LOGICAL', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True], ['RANK', 'TAG', 'COMMUNICATOR', 'LOGICAL', 'STATUS'])}), 'MPI_Irecv': (
        False, {8: ([True, True, True, True, True, True, True, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST',
                     'ERROR_CODE']), 7: ([True, True, True, True, True, True, True],
                                         ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                                          'REQUEST'])}), 'MPI_Ireduce': (False, {9: (
        [True, False, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'RANK', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']),
        8: (
            [True, False, True, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'RANK', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ireduce_scatter': (False, {8: ([True, False, True, True, True, True, True, True],
                                        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR',
                                         'REQUEST', 'ERROR_CODE']), 7: ([True, False, True, True, True, True, True],
                                                                        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE',
                                                                         'OPERATION', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Ireduce_scatter_block': (False, {8: ([True, False, True, True, True, True, True, True],
                                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION',
                                               'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 7: (
        [True, False, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Irsend': (False, {
        8: ([True, True, True, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']),
        7: ([True, True, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Is_thread_main': (False, {2: ([True, True], ['LOGICAL', 'ERROR_CODE']), 1: ([True], ['LOGICAL'])}),
    'MPI_Iscan': (False, {8: ([True, False, True, True, True, True, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'REQUEST',
                               'ERROR_CODE']), 7: ([True, False, True, True, True, True, True],
                                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION',
                                                    'COMMUNICATOR', 'REQUEST'])}), 'MPI_Iscatter': (False, {10: (
        [True, True, True, False, False, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, False, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Iscatterv': (False, {
        11: ([True, True, True, True, False, False, False, True, True, True, True],
             ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'REQUEST',
              'ERROR_CODE']), 10: ([True, True, True, True, False, False, False, True, True, True],
                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'RANK',
                                    'COMMUNICATOR', 'REQUEST'])}), 'MPI_Isend': (False, {8: (
        [True, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}), 'MPI_Isendrecv': (
        False, {13: ([True, True, True, True, True, False, False, False, False, False, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST',
                      'ERROR_CODE']),
                12: ([True, True, True, True, True, False, False, False, False, False, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                      'REQUEST'])}), 'MPI_Isendrecv_replace': (False, {10: (
        [True, True, True, True, True, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, True, True, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Issend': (False,
                   {8: (
                       [True,
                        True,
                        True,
                        True,
                        True,
                        True,
                        True,
                        True],
                       [
                           'BUFFER',
                           'POLYXFER_NUM_ELEM_NNI',
                           'DATATYPE',
                           'RANK',
                           'TAG',
                           'COMMUNICATOR',
                           'REQUEST',
                           'ERROR_CODE']),
                       7: (
                           [True,
                            True,
                            True,
                            True,
                            True,
                            True,
                            True],
                           [
                               'BUFFER',
                               'POLYXFER_NUM_ELEM_NNI',
                               'DATATYPE',
                               'RANK',
                               'TAG',
                               'COMMUNICATOR',
                               'REQUEST'])}),
    'MPI_Keyval_create': (False,
                          {5: ([True, False, True, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE2', 'ERROR_CODE']),
                           4: ([True, False, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE2'])}),
    'MPI_Keyval_free': (False, {2: ([True, True], ['KEYVAL', 'ERROR_CODE']), 1: ([True], ['KEYVAL'])}),
    'MPI_Lookup_name': (False, {4: ([True, True, False, True], ['STRING', 'INFO', 'ERROR_CODE']),
                                3: ([True, True, False], ['STRING', 'INFO'])}),
    'MPI_Message_c2f': (False, {2: ([True, True], ['MESSAGE', 'ERROR_CODE']), 1: ([True], ['MESSAGE'])}),
    'MPI_Message_f2c': (False, {2: ([True, True], ['F90_MESSAGE', 'ERROR_CODE']), 1: ([True], ['F90_MESSAGE'])}),
    'MPI_Mprobe': (False, {
        6: ([True, True, True, True, True, True], ['RANK', 'TAG', 'COMMUNICATOR', 'MESSAGE', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True], ['RANK', 'TAG', 'COMMUNICATOR', 'MESSAGE', 'STATUS'])}), 'MPI_Mrecv': (
        False, {6: ([True, True, True, True, True, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'MESSAGE', 'STATUS', 'ERROR_CODE']),
                5: (
                [True, True, True, True, True], ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'MESSAGE', 'STATUS'])}),
    'MPI_Neighbor_allgather': (False, {8: ([True, True, True, False, False, False, True, True],
                                           ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR',
                                            'ERROR_CODE']), 7: (
        [True, True, True, False, False, False, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Neighbor_allgather_init': (False, {10: ([True, True, True, False, False, False, True, True, True, True],
                                                 ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO',
                                                  'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, False, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Neighbor_allgatherv': (
        False, {9: ([True, True, True, False, False, True, False, True, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR', 'ERROR_CODE']),
                8: (
                    [True, True, True, False, False, True, False, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR'])}),
    'MPI_Neighbor_allgatherv_init': (False, {11: ([True, True, True, False, False, True, False, True, True, True, True],
                                                  ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT',
                                                   'COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']), 10: (
        [True, True, True, False, False, True, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'POLYDISPLACEMENT', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Neighbor_alltoall': (False, {8: ([True, True, True, False, False, False, True, True],
                                          ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR',
                                           'ERROR_CODE']), 7: (
        [True, True, True, False, False, False, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Neighbor_alltoall_init': (False, {10: ([True, True, True, False, False, False, True, True, True, True],
                                                ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO',
                                                 'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, False, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Neighbor_alltoallv': (
        False, {10: ([True, True, True, True, False, False, False, False, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'ERROR_CODE']),
                9: ([True, True, True, True, False, False, False, False, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Neighbor_alltoallv_init': (False, {12: (
        [True, True, True, True, False, False, False, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'INFO', 'REQUEST',
         'ERROR_CODE']), 11: ([True, True, True, True, False, False, False, False, True, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'COMMUNICATOR',
                               'INFO',
                               'REQUEST'])}), 'MPI_Neighbor_alltoallw': (False, {10: (
        [True, True, True, True, False, False, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'ERROR_CODE']), 9: (
        [True, True, True, True, False, False, False, False, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DISPLACEMENT', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Neighbor_alltoallw_init': (
        False, {12: ([True, True, True, True, False, False, False, False, True, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DISPLACEMENT', 'DATATYPE', 'COMMUNICATOR', 'INFO', 'REQUEST',
                      'ERROR_CODE']), 11: ([True, True, True, True, False, False, False, False, True, True, True],
                                           ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DISPLACEMENT', 'DATATYPE',
                                            'COMMUNICATOR',
                                            'INFO', 'REQUEST'])}), 'MPI_NULL_COPY_FN': (False, {7: (
        [True, True, True, True, False, True, True],
        ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE2', 'ATTRIBUTE_VAL_10', 'LOGICAL', 'ERROR_CODE']), 6: (
        [True, True, True, True, False, True],
        ['COMMUNICATOR', 'KEYVAL', 'EXTRA_STATE2', 'ATTRIBUTE_VAL_10', 'LOGICAL'])}),
    'MPI_NULL_DELETE_FN': (False, {5: (
        [True, True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10', 'EXTRA_STATE2', 'ERROR_CODE']),
        4: (
            [True, True, True, True], ['COMMUNICATOR', 'KEYVAL', 'ATTRIBUTE_VAL_10', 'EXTRA_STATE2'])}),
    'MPI_Op_c2f': (False, {2: ([True, True], ['OPERATION', 'ERROR_CODE']), 1: ([True], ['OPERATION'])}),
    'MPI_Op_commutative': (False, {3: ([True, True, True], ['OPERATION', 'LOGICAL', 'ERROR_CODE']),
                                   2: ([True, True], ['OPERATION', 'LOGICAL'])}), 'MPI_Op_create': (False, {
        4: ([True, True, True, True], ['POLYFUNCTION', 'LOGICAL', 'OPERATION', 'ERROR_CODE']),
        3: ([True, True, True], ['POLYFUNCTION', 'LOGICAL', 'OPERATION'])}),
    'MPI_Op_f2c': (False, {2: ([True, True], ['F90_OP', 'ERROR_CODE']), 1: ([True], ['F90_OP'])}),
    'MPI_Op_free': (False, {2: ([True, True], ['OPERATION', 'ERROR_CODE']), 1: ([True], ['OPERATION'])}),
    'MPI_Open_port': (
        False, {3: ([True, True, True], ['INFO', 'STRING', 'ERROR_CODE']), 2: ([True, True], ['INFO', 'STRING'])}),
    'MPI_Pack': (False, {8: ([True, True, True, False, True, True, True, True],
                             ['BUFFER', 'POLYDTYPE_NUM_ELEM_NNI', 'DATATYPE', 'POLYNUM_BYTES_NNI',
                              'POLYDISPLACEMENT_COUNT', 'COMMUNICATOR', 'ERROR_CODE']), 7: (
        [True, True, True, False, True, True, True],
        ['BUFFER', 'POLYDTYPE_NUM_ELEM_NNI', 'DATATYPE', 'POLYNUM_BYTES_NNI', 'POLYDISPLACEMENT_COUNT',
         'COMMUNICATOR'])}),
    'MPI_Pack_external': (False, {8: ([True, True, True, True, False, True, True, True],
                                      ['STRING', 'BUFFER', 'POLYDTYPE_NUM_ELEM', 'DATATYPE', 'POLYDTYPE_PACK_SIZE',
                                       'POLYLOCATION', 'ERROR_CODE']), 7: ([True, True, True, True, False, True, True],
                                                                           ['STRING', 'BUFFER', 'POLYDTYPE_NUM_ELEM',
                                                                            'DATATYPE', 'POLYDTYPE_PACK_SIZE',
                                                                            'POLYLOCATION'])}),
    'MPI_Pack_external_size': (False, {5: (
        [True, True, True, True, True],
        ['STRING', 'POLYDTYPE_NUM_ELEM', 'DATATYPE', 'POLYDTYPE_PACK_SIZE', 'ERROR_CODE']),
        4: ([True, True, True, True],
            ['STRING', 'POLYDTYPE_NUM_ELEM', 'DATATYPE', 'POLYDTYPE_PACK_SIZE'])}),
    'MPI_Pack_size': (False, {5: ([True, True, True, True, True],
                                  ['POLYDTYPE_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'POLYNUM_BYTES_NNI',
                                   'ERROR_CODE']), 4: (
        [True, True, True, True], ['POLYDTYPE_NUM_ELEM_NNI', 'DATATYPE', 'COMMUNICATOR', 'POLYNUM_BYTES_NNI'])}),
    'MPI_Parrived': (False, {4: ([True, True, True, True], ['REQUEST', 'PARTITION', 'LOGICAL', 'ERROR_CODE']),
                             3: ([True, True, True], ['REQUEST', 'PARTITION', 'LOGICAL'])}),
    'MPI_Pcontrol': (True, {1: ([True], ['PROFILE_LEVEL'])}), 'MPI_Pready': (False, {
        3: ([True, True, True], ['PARTITION', 'REQUEST', 'ERROR_CODE']), 2: ([True, True], ['PARTITION', 'REQUEST'])}),
    'MPI_Pready_list': (False, {4: ([True, True, True, True], ['ARRAY_LENGTH', 'PARTITION', 'REQUEST', 'ERROR_CODE']),
                                3: ([True, True, True], ['ARRAY_LENGTH', 'PARTITION', 'REQUEST'])}),
    'MPI_Pready_range': (False, {4: ([True, False, True, True], ['PARTITION', 'REQUEST', 'ERROR_CODE']),
                                 3: ([True, False, True], ['PARTITION', 'REQUEST'])}), 'MPI_Precv_init': (False, {10: (
        [True, True, True, True, True, True, True, True, True, True],
        ['BUFFER', 'PARTITION', 'XFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'INFO', 'REQUEST',
         'ERROR_CODE']), 9: ([True, True, True, True, True, True, True, True, True],
                             ['BUFFER', 'PARTITION', 'XFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                              'INFO',
                              'REQUEST'])}), 'MPI_Probe': (False, {
        5: ([True, True, True, True, True], ['RANK', 'TAG', 'COMMUNICATOR', 'STATUS', 'ERROR_CODE']),
        4: ([True, True, True, True], ['RANK', 'TAG', 'COMMUNICATOR', 'STATUS'])}), 'MPI_Psend_init': (False, {10: (
        [True, True, True, True, True, True, True, True, True, True],
        ['BUFFER', 'PARTITION', 'XFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'INFO', 'REQUEST',
         'ERROR_CODE']), 9: ([True, True, True, True, True, True, True, True, True],
                             ['BUFFER', 'PARTITION', 'XFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                              'INFO',
                              'REQUEST'])}), 'MPI_Publish_name': (False, {
        4: ([True, True, False, True], ['STRING', 'INFO', 'ERROR_CODE']),
        3: ([True, True, False], ['STRING', 'INFO'])}), 'MPI_Put': (False, {9: (
        [True, True, True, True, True, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'WINDOW', 'ERROR_CODE']),
        8: (
            [True, True, True, True, True, False, False, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'WINDOW'])}),
    'MPI_Query_thread': (False, {2: ([True, True], ['THREAD_LEVEL', 'ERROR_CODE']), 1: ([True], ['THREAD_LEVEL'])}),
    'MPI_Raccumulate': (False, {11: ([True, True, True, True, True, False, False, True, True, True, True],
                                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI',
                                      'OPERATION', 'WINDOW', 'REQUEST', 'ERROR_CODE']), 10: (
        [True, True, True, True, True, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'OPERATION', 'WINDOW',
         'REQUEST'])}), 'MPI_Recv': (False, {8: ([True, True, True, True, True, True, True, True],
                                                 ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG',
                                                  'COMMUNICATOR', 'STATUS', 'ERROR_CODE']), 7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'STATUS'])}), 'MPI_Recv_init': (
        False, {8: ([True, True, True, True, True, True, True, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST',
                     'ERROR_CODE']), 7: ([True, True, True, True, True, True, True],
                                         ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                                          'REQUEST'])}), 'MPI_Reduce': (False, {8: (
        [True, False, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'RANK', 'COMMUNICATOR', 'ERROR_CODE']), 7: (
        [True, False, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'RANK', 'COMMUNICATOR'])}),
    'MPI_Reduce_init': (False,
                        {10: (
                            [True,
                             False,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True],
                            [
                                'BUFFER',
                                'POLYXFER_NUM_ELEM_NNI',
                                'DATATYPE',
                                'OPERATION',
                                'RANK',
                                'COMMUNICATOR',
                                'INFO',
                                'REQUEST',
                                'ERROR_CODE']),
                            9: (
                                [True,
                                 False,
                                 True,
                                 True,
                                 True,
                                 True,
                                 True,
                                 True,
                                 True],
                                [
                                    'BUFFER',
                                    'POLYXFER_NUM_ELEM_NNI',
                                    'DATATYPE',
                                    'OPERATION',
                                    'RANK',
                                    'COMMUNICATOR',
                                    'INFO',
                                    'REQUEST'])}),
    'MPI_Reduce_local': (False, {6: (
        [True, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'ERROR_CODE']),
        5: ([True, False, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION'])}),
    'MPI_Reduce_scatter': (False, {7: ([True, False, True, True, True, True, True],
                                       ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR',
                                        'ERROR_CODE']), 6: ([True, False, True, True, True, True],
                                                            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION',
                                                             'COMMUNICATOR'])}), 'MPI_Reduce_scatter_block': (False, {
        7: ([True, False, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'ERROR_CODE']), 6: (
            [True, False, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR'])}),
    'MPI_Reduce_scatter_block_init': (False, {9: ([True, False, True, True, True, True, True, True, True],
                                                  ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION',
                                                   'COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']), 8: (
        [True, False, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Reduce_scatter_init': (False, {9: ([True, False, True, True, True, True, True, True, True],
                                            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR',
                                             'INFO', 'REQUEST', 'ERROR_CODE']), 8: (
        [True, False, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Register_datarep': (False, {
        6: ([True, True, False, True, True, True], ['STRING', 'POLYFUNCTION', 'FUNCTION', 'EXTRA_STATE', 'ERROR_CODE']),
        5: ([True, True, False, True, True], ['STRING', 'POLYFUNCTION', 'FUNCTION', 'EXTRA_STATE'])}),
    'MPI_Request_c2f': (False, {2: ([True, True], ['REQUEST', 'ERROR_CODE']), 1: ([True], ['REQUEST'])}),
    'MPI_Request_f2c': (False, {2: ([True, True], ['F90_REQUEST', 'ERROR_CODE']), 1: ([True], ['F90_REQUEST'])}),
    'MPI_Request_free': (False, {2: ([True, True], ['REQUEST', 'ERROR_CODE']), 1: ([True], ['REQUEST'])}),
    'MPI_Request_get_status': (False, {4: ([True, True, True, True], ['REQUEST', 'LOGICAL', 'STATUS', 'ERROR_CODE']),
                                       3: ([True, True, True], ['REQUEST', 'LOGICAL', 'STATUS'])}), 'MPI_Rget': (False,
                                                                                                                 {10: (
                                                                                                                     [
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         False,
                                                                                                                         False,
                                                                                                                         True,
                                                                                                                         True,
                                                                                                                         True],
                                                                                                                     [
                                                                                                                         'BUFFER',
                                                                                                                         'POLYXFER_NUM_ELEM_NNI',
                                                                                                                         'DATATYPE',
                                                                                                                         'RANK_NNI',
                                                                                                                         'RMA_DISPLACEMENT_NNI',
                                                                                                                         'WINDOW',
                                                                                                                         'REQUEST',
                                                                                                                         'ERROR_CODE']),
                                                                                                                     9: (
                                                                                                                         [
                                                                                                                             True,
                                                                                                                             True,
                                                                                                                             True,
                                                                                                                             True,
                                                                                                                             True,
                                                                                                                             False,
                                                                                                                             False,
                                                                                                                             True,
                                                                                                                             True],
                                                                                                                         [
                                                                                                                             'BUFFER',
                                                                                                                             'POLYXFER_NUM_ELEM_NNI',
                                                                                                                             'DATATYPE',
                                                                                                                             'RANK_NNI',
                                                                                                                             'RMA_DISPLACEMENT_NNI',
                                                                                                                             'WINDOW',
                                                                                                                             'REQUEST'])}),
    'MPI_Rget_accumulate': (False, {14: (
        [True, True, True, False, False, False, True, True, False, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'OPERATION', 'WINDOW',
         'REQUEST', 'ERROR_CODE']), 13: (
        [True, True, True, False, False, False, True, True, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'OPERATION', 'WINDOW',
         'REQUEST'])}), 'MPI_Rput': (False, {10: ([True, True, True, True, True, False, False, True, True, True],
                                                  ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI',
                                                   'RMA_DISPLACEMENT_NNI', 'WINDOW', 'REQUEST', 'ERROR_CODE']), 9: (
        [True, True, True, True, True, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK_NNI', 'RMA_DISPLACEMENT_NNI', 'WINDOW', 'REQUEST'])}),
    'MPI_Rsend': (False, {7: ([True, True, True, True, True, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                               'ERROR_CODE']), 6: ([True, True, True, True, True, True],
                                                   ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG',
                                                    'COMMUNICATOR'])}), 'MPI_Rsend_init': (False, {8: (
        [True, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Scan': (False, {
        7: ([True, False, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'ERROR_CODE']), 6: (
            [True, False, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR'])}),
    'MPI_Scan_init': (False, {9: (
        [True, False, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']),
        8: (
            [True, False, True, True, True, True, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'OPERATION', 'COMMUNICATOR', 'INFO', 'REQUEST'])}),
    'MPI_Scatter': (
        False, {9: ([True, True, True, False, False, False, True, True, True],
                    ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'ERROR_CODE']), 8: (
            [True, True, True, False, False, False, True, True],
            ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR'])}),
    'MPI_Scatter_init': (False, {11: (
        [True, True, True, False, False, False, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'INFO', 'REQUEST', 'ERROR_CODE']), 10: (
        [True, True, True, False, False, False, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'INFO', 'REQUEST'])}), 'MPI_Scatterv': (
        False, {10: ([True, True, True, True, False, False, False, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'RANK', 'COMMUNICATOR',
                      'ERROR_CODE']), 9: ([True, True, True, True, False, False, False, True, True],
                                          ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'RANK',
                                           'COMMUNICATOR'])}), 'MPI_Scatterv_init': (False, {12: (
        [True, True, True, True, False, False, False, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'RANK', 'COMMUNICATOR', 'INFO', 'REQUEST',
         'ERROR_CODE']), 11: ([True, True, True, True, False, False, False, True, True, True, True],
                              ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'POLYDISPLACEMENT', 'DATATYPE', 'RANK',
                               'COMMUNICATOR',
                               'INFO', 'REQUEST'])}),
    'MPI_Send': (False, {7: ([True, True, True, True, True, True, True],
                             ['BUFFER', 'POLYXFER_NUM_ELEM_NNI',
                              'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                              'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR'])}),
    'MPI_Send_init': (False, {8: (
        [True, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}), 'MPI_Sendrecv': (
        False, {13: ([True, True, True, True, True, False, False, False, False, False, True, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'STATUS',
                      'ERROR_CODE']),
                12: ([True, True, True, True, True, False, False, False, False, False, True, True],
                     ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR',
                      'STATUS'])}), 'MPI_Sendrecv_replace': (False, {10: (
        [True, True, True, True, True, False, False, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'STATUS', 'ERROR_CODE']), 9: (
        [True, True, True, True, True, False, False, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'STATUS'])}),
    'MPI_Session_c2f': (False, {2: ([True, True], ['SESSION', 'ERROR_CODE']), 1: ([True], ['SESSION'])}),
    'MPI_Session_call_errhandler': (
        False, {3: ([True, True, False], ['SESSION', 'ERROR_CODE']), 2: ([True, True], ['SESSION', 'ERROR_CODE'])}),
    'MPI_Session_create_errhandler': (False, {3: ([True, True, True], ['FUNCTION', 'ERRHANDLER', 'ERROR_CODE']),
                                              2: ([True, True], ['FUNCTION', 'ERRHANDLER'])}),
    'MPI_Session_errhandler_function': (True, {2: ([True, True], ['SESSION', 'ERROR_CODE'])}),
    'MPI_Session_f2c': (False, {2: ([True, True], ['F90_SESSION', 'ERROR_CODE']), 1: ([True], ['F90_SESSION'])}),
    'MPI_Session_finalize': (False, {2: ([True, True], ['SESSION', 'ERROR_CODE']), 1: ([True], ['SESSION'])}),
    'MPI_Session_get_errhandler': (False, {3: ([True, True, True], ['SESSION', 'ERRHANDLER', 'ERROR_CODE']),
                                           2: ([True, True], ['SESSION', 'ERRHANDLER'])}), 'MPI_Session_get_info': (
        False, {3: ([True, True, True], ['SESSION', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['SESSION', 'INFO'])}),
    'MPI_Session_get_nth_pset': (False, {6: (
        [True, True, True, True, True, True], ['SESSION', 'INFO', 'INDEX', 'STRING_LENGTH', 'STRING', 'ERROR_CODE']),
        5: (
            [True, True, True, True, True], ['SESSION', 'INFO', 'INDEX', 'STRING_LENGTH', 'STRING'])}),
    'MPI_Session_get_num_psets': (False,
                                  {4: ([True, True, True, True], ['SESSION', 'INFO', 'ARRAY_LENGTH_NNI', 'ERROR_CODE']),
                                   3: ([True, True, True], ['SESSION', 'INFO', 'ARRAY_LENGTH_NNI'])}),
    'MPI_Session_get_pset_info': (False, {4: ([True, True, True, True], ['SESSION', 'STRING', 'INFO', 'ERROR_CODE']),
                                          3: ([True, True, True], ['SESSION', 'STRING', 'INFO'])}),
    'MPI_Session_init': (False, {4: ([True, True, True, True], ['INFO', 'ERRHANDLER', 'SESSION', 'ERROR_CODE']),
                                 3: ([True, True, True], ['INFO', 'ERRHANDLER', 'SESSION'])}),
    'MPI_Session_set_errhandler': (False, {3: ([True, True, True], ['SESSION', 'ERRHANDLER', 'ERROR_CODE']),
                                           2: ([True, True], ['SESSION', 'ERRHANDLER'])}), 'MPI_Sizeof': (False, {
        3: ([True, True, True], ['BUFFER', 'NUM_BYTES_SMALL', 'ERROR_CODE']),
        2: ([True, True], ['BUFFER', 'NUM_BYTES_SMALL'])}), 'MPI_Ssend': (False, {7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'ERROR_CODE']), 6: (
        [True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR'])}),
    'MPI_Ssend_init': (False, {8: (
        [True, True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST', 'ERROR_CODE']), 7: (
        [True, True, True, True, True, True, True],
        ['BUFFER', 'POLYXFER_NUM_ELEM_NNI', 'DATATYPE', 'RANK', 'TAG', 'COMMUNICATOR', 'REQUEST'])}),
    'MPI_Start': (False, {2: ([True, True], ['REQUEST', 'ERROR_CODE']), 1: ([True], ['REQUEST'])}), 'MPI_Startall': (
        False, {3: ([True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'ERROR_CODE']),
                2: ([True, True], ['ARRAY_LENGTH_NNI', 'REQUEST'])}), 'MPI_Status_c2f': (False, {
        3: ([True, True, True], ['STATUS', 'F90_STATUS', 'ERROR_CODE']), 2: ([True, True], ['STATUS', 'F90_STATUS'])}),
    'MPI_Status_c2f08': (False, {3: ([True, True, True], ['STATUS', 'F08_STATUS', 'ERROR_CODE']),
                                 2: ([True, True], ['STATUS', 'F08_STATUS'])}), 'MPI_Status_f082c': (False, {
        3: ([True, True, True], ['F08_STATUS', 'STATUS', 'ERROR_CODE']), 2: ([True, True], ['F08_STATUS', 'STATUS'])}),
    'MPI_Status_f082f': (False, {3: ([True, True, True], ['F08_STATUS', 'F90_STATUS', 'ERROR_CODE']),
                                 2: ([True, True], ['F08_STATUS', 'F90_STATUS'])}), 'MPI_Status_f2c': (False, {
        3: ([True, True, True], ['F90_STATUS', 'STATUS', 'ERROR_CODE']), 2: ([True, True], ['F90_STATUS', 'STATUS'])}),
    'MPI_Status_f2f08': (False, {3: ([True, True, True], ['F90_STATUS', 'F08_STATUS', 'ERROR_CODE']),
                                 2: ([True, True], ['F90_STATUS', 'F08_STATUS'])}), 'MPI_Status_set_cancelled': (
        False,
        {3: ([True, True, True], ['STATUS', 'LOGICAL', 'ERROR_CODE']), 2: ([True, True], ['STATUS', 'LOGICAL'])}),
    'MPI_Status_set_elements': (False, {
        4: ([True, True, True, True], ['STATUS', 'DATATYPE', 'POLYXFER_NUM_ELEM', 'ERROR_CODE']),
        3: ([True, True, True], ['STATUS', 'DATATYPE', 'POLYXFER_NUM_ELEM'])}), 'MPI_Status_set_elements_x': (False, {
        4: ([True, True, True, True], ['STATUS', 'DATATYPE', 'XFER_NUM_ELEM', 'ERROR_CODE']),
        3: ([True, True, True], ['STATUS', 'DATATYPE', 'XFER_NUM_ELEM'])}), 'MPI_T_category_changed': (
        False, {2: ([True, True], ['UPDATE_NUMBER', 'ERROR_CODE']), 1: ([True], ['UPDATE_NUMBER'])}),
    'MPI_T_category_get_categories': (False,
                                      {4: ([True, True, False, True], ['CAT_INDEX', 'ARRAY_LENGTH', 'ERROR_CODE']),
                                       3: ([True, True, False], ['CAT_INDEX', 'ARRAY_LENGTH'])}),
    'MPI_T_category_get_cvars': (False, {
        4: ([True, True, True, True], ['CAT_INDEX', 'ARRAY_LENGTH', 'CVAR_INDEX', 'ERROR_CODE']),
        3: ([True, True, True], ['CAT_INDEX', 'ARRAY_LENGTH', 'CVAR_INDEX'])}), 'MPI_T_category_get_events': (False, {
        4: ([True, True, False, True], ['CAT_INDEX', 'ARRAY_LENGTH', 'ERROR_CODE']),
        3: ([True, True, False], ['CAT_INDEX', 'ARRAY_LENGTH'])}), 'MPI_T_category_get_index': (False, {
        3: ([True, True, True], ['STRING', 'CAT_INDEX', 'ERROR_CODE']), 2: ([True, True], ['STRING', 'CAT_INDEX'])}),
    'MPI_T_category_get_info': (False, {9: ([True, True, True, False, False, True, True, False, True],
                                            ['CAT_INDEX', 'STRING', 'STRING_LENGTH', 'CVAR_INDEX', 'PVAR_INDEX',
                                             'ERROR_CODE']), 8: ([True, True, True, False, False, True, True, False],
                                                                 ['CAT_INDEX', 'STRING', 'STRING_LENGTH', 'CVAR_INDEX',
                                                                  'PVAR_INDEX'])}),
    'MPI_T_category_get_num': (False, {2: ([True, True], ['CAT_INDEX', 'ERROR_CODE']), 1: ([True], ['CAT_INDEX'])}),
    'MPI_T_category_get_num_events': (False, {3: ([True, True, True], ['CAT_INDEX', 'EVENT_INDEX', 'ERROR_CODE']),
                                              2: ([True, True], ['CAT_INDEX', 'EVENT_INDEX'])}),
    'MPI_T_category_get_pvars': (False, {
        4: ([True, True, True, True], ['CAT_INDEX', 'ARRAY_LENGTH', 'PVAR_INDEX', 'ERROR_CODE']),
        3: ([True, True, True], ['CAT_INDEX', 'ARRAY_LENGTH', 'PVAR_INDEX'])}), 'MPI_T_cvar_get_index': (False, {
        3: ([True, True, True], ['STRING', 'CVAR_INDEX', 'ERROR_CODE']), 2: ([True, True], ['STRING', 'CVAR_INDEX'])}),
    'MPI_T_cvar_get_info': (False, {11: ([True, True, True, True, True, True, False, False, True, True, True],
                                         ['CVAR_INDEX', 'STRING', 'STRING_LENGTH', 'TOOL_VAR_VERBOSITY', 'DATATYPE',
                                          'TOOLS_ENUM', 'BIND_TYPE', 'VARIABLE_SCOPE', 'ERROR_CODE']), 10: (
        [True, True, True, True, True, True, False, False, True, True],
        ['CVAR_INDEX', 'STRING', 'STRING_LENGTH', 'TOOL_VAR_VERBOSITY', 'DATATYPE', 'TOOLS_ENUM', 'BIND_TYPE',
         'VARIABLE_SCOPE'])}),
    'MPI_T_cvar_get_num': (False, {2: ([True, True], ['CVAR_INDEX', 'ERROR_CODE']), 1: ([True], ['CVAR_INDEX'])}),
    'MPI_T_cvar_handle_alloc': (False, {5: ([True, True, True, True, True],
                                            ['CVAR_INDEX_SPECIAL', 'TOOL_MPI_OBJ', 'CVAR', 'TOOLS_NUM_ELEM_SMALL',
                                             'ERROR_CODE']), 4: (
        [True, True, True, True], ['CVAR_INDEX_SPECIAL', 'TOOL_MPI_OBJ', 'CVAR', 'TOOLS_NUM_ELEM_SMALL'])}),
    'MPI_T_cvar_handle_free': (False, {2: ([True, True], ['CVAR', 'ERROR_CODE']), 1: ([True], ['CVAR'])}),
    'MPI_T_cvar_read': (
        False, {3: ([True, True, True], ['CVAR', 'BUFFER', 'ERROR_CODE']), 2: ([True, True], ['CVAR', 'BUFFER'])}),
    'MPI_T_cvar_write': (
        False, {3: ([True, True, True], ['CVAR', 'BUFFER', 'ERROR_CODE']), 2: ([True, True], ['CVAR', 'BUFFER'])}),
    'MPI_T_enum_get_info': (False, {
        5: ([True, True, True, True, True], ['TOOLS_ENUM', 'TOOLENUM_SIZE', 'STRING', 'STRING_LENGTH', 'ERROR_CODE']),
        4: ([True, True, True, True], ['TOOLS_ENUM', 'TOOLENUM_SIZE', 'STRING', 'STRING_LENGTH'])}),
    'MPI_T_enum_get_item': (False, {6: ([True, True, True, True, True, True],
                                        ['TOOLS_ENUM', 'TOOLENUM_INDEX', 'TOOL_VAR_VALUE', 'STRING', 'STRING_LENGTH',
                                         'ERROR_CODE']), 5: (
        [True, True, True, True, True],
        ['TOOLS_ENUM', 'TOOLENUM_INDEX', 'TOOL_VAR_VALUE', 'STRING', 'STRING_LENGTH'])}),
    'MPI_T_event_callback_get_info': (False, {
        4: ([True, True, True, True], ['EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'INFO', 'ERROR_CODE']),
        3: ([True, True, True], ['EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'INFO'])}), 'MPI_T_event_callback_set_info': (
        False, {4: ([True, True, True, True], ['EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'INFO', 'ERROR_CODE']),
                3: ([True, True, True], ['EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'INFO'])}),
    'MPI_T_event_cb_function': (
        False, {5: ([True, True, True, True, True],
                    ['EVENT_INSTANCE', 'EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'EXTRA_STATE', 'ERROR_CODE']),
                4: (
                [True, True, True, True], ['EVENT_INSTANCE', 'EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'EXTRA_STATE'])}),
    'MPI_T_event_copy': (False, {3: ([True, True, True], ['EVENT_INSTANCE', 'C_BUFFER', 'ERROR_CODE']),
                                 2: ([True, True], ['EVENT_INSTANCE', 'C_BUFFER'])}),
    'MPI_T_event_dropped_cb_function': (False, {6: ([True, True, True, True, True, True],
                                                    ['DROPPED_COUNT', 'EVENT_REGISTRATION', 'SOURCE_INDEX',
                                                     'CALLBACK_SAFETY', 'EXTRA_STATE', 'ERROR_CODE']), 5: (
        [True, True, True, True, True],
        ['DROPPED_COUNT', 'EVENT_REGISTRATION', 'SOURCE_INDEX', 'CALLBACK_SAFETY', 'EXTRA_STATE'])}),
    'MPI_T_event_free_cb_function': (False, {
        4: ([True, True, True, True], ['EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'EXTRA_STATE', 'ERROR_CODE']),
        3: ([True, True, True], ['EVENT_REGISTRATION', 'CALLBACK_SAFETY', 'EXTRA_STATE'])}), 'MPI_T_event_get_index': (
        False,
        {3: ([True, True, True], ['STRING', 'EVENT_INDEX', 'ERROR_CODE']),
         2: ([True, True], ['STRING', 'EVENT_INDEX'])}),
    'MPI_T_event_get_info': (False, {13: (
        [True, True, True, True, True, True, True, True, True, False, False, True, True],
        ['EVENT_INDEX', 'STRING', 'STRING_LENGTH', 'TOOL_VAR_VERBOSITY', 'DATATYPE', 'DISPLACEMENT_NNI',
         'ARRAY_LENGTH_NNI',
         'TOOLS_ENUM', 'INFO', 'BIND_TYPE', 'ERROR_CODE']), 12: (
        [True, True, True, True, True, True, True, True, True, False, False, True],
        ['EVENT_INDEX', 'STRING', 'STRING_LENGTH', 'TOOL_VAR_VERBOSITY', 'DATATYPE', 'DISPLACEMENT_NNI',
         'ARRAY_LENGTH_NNI',
         'TOOLS_ENUM', 'INFO', 'BIND_TYPE'])}),
    'MPI_T_event_get_num': (False, {2: ([True, True], ['EVENT_INDEX', 'ERROR_CODE']), 1: ([True], ['EVENT_INDEX'])}),
    'MPI_T_event_get_source': (False, {3: ([True, True, True], ['EVENT_INSTANCE', 'SOURCE_INDEX', 'ERROR_CODE']),
                                       2: ([True, True], ['EVENT_INSTANCE', 'SOURCE_INDEX'])}),
    'MPI_T_event_get_timestamp': (False, {3: ([True, True, True], ['EVENT_INSTANCE', 'TOOLS_TICK_COUNT', 'ERROR_CODE']),
                                          2: ([True, True], ['EVENT_INSTANCE', 'TOOLS_TICK_COUNT'])}),
    'MPI_T_event_handle_alloc': (False, {5: (
        [True, True, True, True, True], ['EVENT_INDEX', 'TOOL_MPI_OBJ', 'INFO', 'EVENT_REGISTRATION', 'ERROR_CODE']),
        4: (
            [True, True, True, True], ['EVENT_INDEX', 'TOOL_MPI_OBJ', 'INFO', 'EVENT_REGISTRATION'])}),
    'MPI_T_event_handle_free': (False, {
        4: ([True, True, True, True], ['EVENT_REGISTRATION', 'EXTRA_STATE', 'EVENT_FREE_CB_FUNCTION', 'ERROR_CODE']),
        3: ([True, True, True], ['EVENT_REGISTRATION', 'EXTRA_STATE', 'EVENT_FREE_CB_FUNCTION'])}),
    'MPI_T_event_handle_get_info': (False, {3: ([True, True, True], ['EVENT_REGISTRATION', 'INFO', 'ERROR_CODE']),
                                            2: ([True, True], ['EVENT_REGISTRATION', 'INFO'])}),
    'MPI_T_event_handle_set_info': (False, {3: ([True, True, True], ['EVENT_REGISTRATION', 'INFO', 'ERROR_CODE']),
                                            2: ([True, True], ['EVENT_REGISTRATION', 'INFO'])}), 'MPI_T_event_read': (
        False, {4: ([True, True, True, True], ['EVENT_INSTANCE', 'INDEX', 'C_BUFFER', 'ERROR_CODE']),
                3: ([True, True, True], ['EVENT_INSTANCE', 'INDEX', 'C_BUFFER'])}),
    'MPI_T_event_register_callback': (False,
                                      {6: (
                                          [True,
                                           True,
                                           True,
                                           True,
                                           True,
                                           True],
                                          [
                                              'EVENT_REGISTRATION',
                                              'CALLBACK_SAFETY',
                                              'INFO',
                                              'EXTRA_STATE',
                                              'EVENT_CB_FUNCTION',
                                              'ERROR_CODE']),
                                          5: ([
                                                  True,
                                                  True,
                                                  True,
                                                  True,
                                                  True],
                                              [
                                                  'EVENT_REGISTRATION',
                                                  'CALLBACK_SAFETY',
                                                  'INFO',
                                                  'EXTRA_STATE',
                                                  'EVENT_CB_FUNCTION'])}),
    'MPI_T_event_set_dropped_handler': (False, {
        3: ([True, True, True], ['EVENT_REGISTRATION', 'EVENT_DROP_CB_FUNCTION', 'ERROR_CODE']),
        2: ([True, True], ['EVENT_REGISTRATION', 'EVENT_DROP_CB_FUNCTION'])}),
    'MPI_T_finalize': (False, {1: ([True], ['ERROR_CODE']), 0: ([], [])}), 'MPI_T_init_thread': (
        False, {3: ([True, False, True], ['THREAD_LEVEL', 'ERROR_CODE']), 2: ([True, False], ['THREAD_LEVEL'])}),
    'MPI_T_pvar_get_index': (False,
                             {4: ([True, True, True, True], ['STRING', 'PVAR_CLASS', 'PVAR_INDEX', 'ERROR_CODE']),
                              3: ([True, True, True], ['STRING', 'PVAR_CLASS', 'PVAR_INDEX'])}),
    'MPI_T_pvar_get_info': (False, {14: (
        [True, True, True, True, True, True, True, False, False, True, True, False, False, True],
        ['PVAR_INDEX', 'STRING', 'STRING_LENGTH', 'TOOL_VAR_VERBOSITY', 'PVAR_CLASS', 'DATATYPE', 'TOOLS_ENUM',
         'BIND_TYPE',
         'LOGICAL_OPTIONAL', 'ERROR_CODE']), 13: (
        [True, True, True, True, True, True, True, False, False, True, True, False, False],
        ['PVAR_INDEX', 'STRING', 'STRING_LENGTH', 'TOOL_VAR_VERBOSITY', 'PVAR_CLASS', 'DATATYPE', 'TOOLS_ENUM',
         'BIND_TYPE',
         'LOGICAL_OPTIONAL'])}),
    'MPI_T_pvar_get_num': (False, {2: ([True, True], ['PVAR_INDEX', 'ERROR_CODE']), 1: ([True], ['PVAR_INDEX'])}),
    'MPI_T_pvar_handle_alloc': (False, {6: ([True, True, True, True, True, True],
                                            ['PVAR_SESSION', 'PVAR_INDEX', 'TOOL_MPI_OBJ', 'PVAR',
                                             'TOOLS_NUM_ELEM_SMALL', 'ERROR_CODE']), 5: (
        [True, True, True, True, True],
        ['PVAR_SESSION', 'PVAR_INDEX', 'TOOL_MPI_OBJ', 'PVAR', 'TOOLS_NUM_ELEM_SMALL'])}),
    'MPI_T_pvar_handle_free': (False, {3: ([True, True, True], ['PVAR_SESSION', 'PVAR', 'ERROR_CODE']),
                                       2: ([True, True], ['PVAR_SESSION', 'PVAR'])}), 'MPI_T_pvar_read': (False, {
        4: ([True, True, True, True], ['PVAR_SESSION', 'PVAR', 'BUFFER', 'ERROR_CODE']),
        3: ([True, True, True], ['PVAR_SESSION', 'PVAR', 'BUFFER'])}), 'MPI_T_pvar_readreset': (False, {
        4: ([True, True, True, True], ['PVAR_SESSION', 'PVAR', 'BUFFER', 'ERROR_CODE']),
        3: ([True, True, True], ['PVAR_SESSION', 'PVAR', 'BUFFER'])}), 'MPI_T_pvar_reset': (False, {
        3: ([True, True, True], ['PVAR_SESSION', 'PVAR', 'ERROR_CODE']), 2: ([True, True], ['PVAR_SESSION', 'PVAR'])}),
    'MPI_T_pvar_session_create': (
        False, {2: ([True, True], ['PVAR_SESSION', 'ERROR_CODE']), 1: ([True], ['PVAR_SESSION'])}),
    'MPI_T_pvar_session_free': (
        False, {2: ([True, True], ['PVAR_SESSION', 'ERROR_CODE']), 1: ([True], ['PVAR_SESSION'])}),
    'MPI_T_pvar_start': (
        False,
        {3: ([True, True, True], ['PVAR_SESSION', 'PVAR', 'ERROR_CODE']), 2: ([True, True], ['PVAR_SESSION', 'PVAR'])}),
    'MPI_T_pvar_stop': (False, {3: ([True, True, True], ['PVAR_SESSION', 'PVAR', 'ERROR_CODE']),
                                2: ([True, True], ['PVAR_SESSION', 'PVAR'])}), 'MPI_T_pvar_write': (False, {
        4: ([True, True, True, True], ['PVAR_SESSION', 'PVAR', 'BUFFER', 'ERROR_CODE']),
        3: ([True, True, True], ['PVAR_SESSION', 'PVAR', 'BUFFER'])}), 'MPI_T_source_get_info': (False, {10: (
        [True, True, True, False, False, True, True, False, True, True],
        ['SOURCE_INDEX', 'STRING', 'STRING_LENGTH', 'SOURCE_ORDERING', 'TOOLS_TICK_COUNT', 'INFO', 'ERROR_CODE']), 9: (
        [True, True, True, False, False, True, True, False, True],
        ['SOURCE_INDEX', 'STRING', 'STRING_LENGTH', 'SOURCE_ORDERING', 'TOOLS_TICK_COUNT', 'INFO'])}),
    'MPI_T_source_get_num': (False, {2: ([True, True], ['SOURCE_INDEX', 'ERROR_CODE']), 1: ([True], ['SOURCE_INDEX'])}),
    'MPI_T_source_get_timestamp': (False, {3: ([True, True, True], ['SOURCE_INDEX', 'TOOLS_TICK_COUNT', 'ERROR_CODE']),
                                           2: ([True, True], ['SOURCE_INDEX', 'TOOLS_TICK_COUNT'])}), 'MPI_Test': (
        False, {4: ([True, True, True, True], ['REQUEST', 'LOGICAL', 'STATUS', 'ERROR_CODE']),
                3: ([True, True, True], ['REQUEST', 'LOGICAL', 'STATUS'])}), 'MPI_Test_cancelled': (
        False,
        {3: ([True, True, True], ['STATUS', 'LOGICAL', 'ERROR_CODE']), 2: ([True, True], ['STATUS', 'LOGICAL'])}),
    'MPI_Testall': (False, {
        5: ([True, True, True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'LOGICAL', 'STATUS', 'ERROR_CODE']),
        4: ([True, True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'LOGICAL', 'STATUS'])}), 'MPI_Testany': (False, {
        6: ([True, True, True, True, True, True],
            ['ARRAY_LENGTH_NNI', 'REQUEST', 'INDEX', 'LOGICAL', 'STATUS', 'ERROR_CODE']),
        5: ([True, True, True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'INDEX', 'LOGICAL', 'STATUS'])}),
    'MPI_Testsome': (False, {6: ([True, True, True, True, True, True],
                                 ['ARRAY_LENGTH_NNI', 'REQUEST', 'ARRAY_LENGTH', 'INDEX', 'STATUS', 'ERROR_CODE']), 5: (
        [True, True, True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'ARRAY_LENGTH', 'INDEX', 'STATUS'])}),
    'MPI_Topo_test': (False, {3: ([True, True, True], ['COMMUNICATOR', 'TOPOLOGY_TYPE', 'ERROR_CODE']),
                              2: ([True, True], ['COMMUNICATOR', 'TOPOLOGY_TYPE'])}),
    'MPI_Type_c2f': (False, {2: ([True, True], ['DATATYPE', 'ERROR_CODE']), 1: ([True], ['DATATYPE'])}),
    'MPI_Type_commit': (False, {2: ([True, True], ['DATATYPE', 'ERROR_CODE']), 1: ([True], ['DATATYPE'])}),
    'MPI_Type_contiguous': (False, {
        4: ([True, True, True, True], ['POLYDTYPE_NUM_ELEM_NNI', 'DATATYPE', 'newDATATYPE', 'ERROR_CODE']),
        3: ([True, True, True], ['POLYDTYPE_NUM_ELEM_NNI', 'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_copy_attr_function': (False, {7: ([True, True, True, True, False, True, True],
                                                ['DATATYPE', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL',
                                                 'ERROR_CODE']), 6: (
        [True, True, True, True, False, True], ['DATATYPE', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_Type_create_darray': (False, {11: ([True, True, True, True, True, True, True, True, True, True, True],
                                            ['COMM_SIZE_PI', 'RANK_NNI', 'ARRAY_LENGTH_PI', 'POLYDTYPE_NUM_ELEM_PI',
                                             'DISTRIB_ENUM', 'DTYPE_DISTRIBUTION', 'PROCESS_GRID_SIZE', 'ORDER',
                                             'DATATYPE', 'newDATATYPE', 'ERROR_CODE']), 10: (
        [True, True, True, True, True, True, True, True, True, True],
        ['COMM_SIZE_PI', 'RANK_NNI', 'ARRAY_LENGTH_PI', 'POLYDTYPE_NUM_ELEM_PI', 'DISTRIB_ENUM', 'DTYPE_DISTRIBUTION',
         'PROCESS_GRID_SIZE', 'ORDER', 'DATATYPE', 'newDATATYPE'])}), 'MPI_Type_create_f90_complex': (False, {
        4: ([True, False, True, True], ['MATH', 'newDATATYPE', 'ERROR_CODE']),
        3: ([True, False, True], ['MATH', 'newDATATYPE'])}), 'MPI_Type_create_f90_integer': (False, {
        3: ([True, True, True], ['MATH', 'newDATATYPE', 'ERROR_CODE']), 2: ([True, True], ['MATH', 'newDATATYPE'])}),
    'MPI_Type_create_f90_real': (False, {4: ([True, False, True, True], ['MATH', 'newDATATYPE', 'ERROR_CODE']),
                                         3: ([True, False, True], ['MATH', 'newDATATYPE'])}),
    'MPI_Type_create_hindexed': (False, {6: ([True, False, True, True, True, True],
                                             ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDISPLACEMENT_AINT_COUNT', 'DATATYPE',
                                              'newDATATYPE', 'ERROR_CODE']), 5: ([True, False, True, True, True],
                                                                                 ['POLYDTYPE_NUM_ELEM_NNI',
                                                                                  'POLYDISPLACEMENT_AINT_COUNT',
                                                                                  'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_create_hindexed_block': (False, {6: ([True, False, True, True, True, True],
                                                   ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDISPLACEMENT_AINT_COUNT', 'DATATYPE',
                                                    'newDATATYPE', 'ERROR_CODE']), 5: ([True, False, True, True, True],
                                                                                       ['POLYDTYPE_NUM_ELEM_NNI',
                                                                                        'POLYDISPLACEMENT_AINT_COUNT',
                                                                                        'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_create_hvector': (False, {6: ([True, False, True, True, True, True],
                                            ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDTYPE_STRIDE_BYTES', 'DATATYPE',
                                             'newDATATYPE', 'ERROR_CODE']), 5: (
        [True, False, True, True, True],
        ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDTYPE_STRIDE_BYTES', 'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_create_indexed_block': (False, {6: ([True, False, True, True, True, True],
                                                  ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDISPLACEMENT_COUNT', 'DATATYPE',
                                                   'newDATATYPE', 'ERROR_CODE']), 5: (
        [True, False, True, True, True],
        ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDISPLACEMENT_COUNT', 'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_create_keyval': (False, {
        5: ([True, False, True, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE', 'ERROR_CODE']),
        4: ([True, False, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE'])}), 'MPI_Type_create_resized': (False, {
        5: ([True, True, False, True, True], ['DATATYPE', 'POLYDISPLACEMENT_AINT_COUNT', 'newDATATYPE', 'ERROR_CODE']),
        4: ([True, True, False, True], ['DATATYPE', 'POLYDISPLACEMENT_AINT_COUNT', 'newDATATYPE'])}),
    'MPI_Type_create_struct': (False, {6: ([True, False, True, True, True, True],
                                           ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDISPLACEMENT_AINT_COUNT', 'DATATYPE',
                                            'newDATATYPE', 'ERROR_CODE']), 5: ([True, False, True, True, True],
                                                                               ['POLYDTYPE_NUM_ELEM_NNI',
                                                                                'POLYDISPLACEMENT_AINT_COUNT',
                                                                                'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_create_subarray': (False, {8: ([True, True, False, True, True, True, True, True],
                                             ['ARRAY_LENGTH_PI', 'POLYDTYPE_NUM_ELEM_PI', 'POLYDTYPE_NUM_ELEM_NNI',
                                              'ORDER', 'DATATYPE', 'newDATATYPE', 'ERROR_CODE']), 7: (
        [True, True, False, True, True, True, True],
        ['ARRAY_LENGTH_PI', 'POLYDTYPE_NUM_ELEM_PI', 'POLYDTYPE_NUM_ELEM_NNI', 'ORDER', 'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_delete_attr': (
        False,
        {3: ([True, True, True], ['DATATYPE', 'KEYVAL', 'ERROR_CODE']), 2: ([True, True], ['DATATYPE', 'KEYVAL'])}),
    'MPI_Type_delete_attr_function': (False, {
        5: ([True, True, True, True, True], ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE'])}), 'MPI_Type_dup': (False,
                                                                                                                  {3: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'DATATYPE',
                                                                                                                          'newDATATYPE',
                                                                                                                          'ERROR_CODE']),
                                                                                                                      2: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'DATATYPE',
                                                                                                                          'newDATATYPE'])}),
    'MPI_TYPE_DUP_FN': (False, {7: ([True, True, True, True, False, True, True],
                                    ['DATATYPE', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']),
                                6: ([True, True, True, True, False, True],
                                    ['DATATYPE', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_Type_f2c': (False, {2: ([True, True], ['F90_DATATYPE', 'ERROR_CODE']), 1: ([True], ['F90_DATATYPE'])}),
    'MPI_Type_free': (False, {2: ([True, True], ['DATATYPE', 'ERROR_CODE']), 1: ([True], ['DATATYPE'])}),
    'MPI_Type_free_keyval': (False, {2: ([True, True], ['KEYVAL', 'ERROR_CODE']), 1: ([True], ['KEYVAL'])}),
    'MPI_Type_get_attr': (False, {
        5: ([True, True, True, True, True], ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']),
        4: ([True, True, True, True], ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL', 'LOGICAL'])}), 'MPI_Type_get_contents': (
        False, {10: ([True, True, False, False, False, True, True, True, False, True],
                     ['DATATYPE', 'POLYNUM_PARAM_VALUES', 'GENERIC_DTYPE_INT', 'DISPLACEMENT', 'GENERIC_DTYPE_COUNT',
                      'ERROR_CODE']), 9: ([True, True, False, False, False, True, True, True, False],
                                          ['DATATYPE', 'POLYNUM_PARAM_VALUES', 'GENERIC_DTYPE_INT', 'DISPLACEMENT',
                                           'GENERIC_DTYPE_COUNT'])}), 'MPI_Type_get_envelope': (False, {7: (
        [True, True, False, False, False, True, True], ['DATATYPE', 'POLYNUM_PARAM_VALUES', 'COMBINER', 'ERROR_CODE']),
        6: (
            [True, True, False, False, False, True], ['DATATYPE', 'POLYNUM_PARAM_VALUES', 'COMBINER'])}),
    'MPI_Type_get_extent': (False,
                            {4: ([True, True, False, True], ['DATATYPE', 'POLYDISPLACEMENT_AINT_COUNT', 'ERROR_CODE']),
                             3: ([True, True, False], ['DATATYPE', 'POLYDISPLACEMENT_AINT_COUNT'])}),
    'MPI_Type_get_extent_x': (False, {4: ([True, True, False, True], ['DATATYPE', 'XFER_NUM_ELEM', 'ERROR_CODE']),
                                      3: ([True, True, False], ['DATATYPE', 'XFER_NUM_ELEM'])}), 'MPI_Type_get_name': (
        False, {4: ([True, True, True, True], ['DATATYPE', 'STRING', 'STRING_LENGTH', 'ERROR_CODE']),
                3: ([True, True, True], ['DATATYPE', 'STRING', 'STRING_LENGTH'])}),
    'MPI_Type_get_true_extent': (False, {
        4: ([True, True, False, True], ['DATATYPE', 'POLYDISPLACEMENT_AINT_COUNT', 'ERROR_CODE']),
        3: ([True, True, False], ['DATATYPE', 'POLYDISPLACEMENT_AINT_COUNT'])}), 'MPI_Type_get_true_extent_x': (False, {
        4: ([True, True, False, True], ['DATATYPE', 'XFER_NUM_ELEM', 'ERROR_CODE']),
        3: ([True, True, False], ['DATATYPE', 'XFER_NUM_ELEM'])}), 'MPI_Type_indexed': (False, {6: (
        [True, False, True, True, True, True],
        ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDISPLACEMENT_COUNT', 'DATATYPE', 'newDATATYPE', 'ERROR_CODE']), 5: (
        [True, False, True, True, True],
        ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDISPLACEMENT_COUNT', 'DATATYPE', 'newDATATYPE'])}),
    'MPI_Type_match_size': (False,
                            {4: ([True, True, True, True], ['TYPECLASS', 'TYPECLASS_SIZE', 'DATATYPE', 'ERROR_CODE']),
                             3: ([True, True, True], ['TYPECLASS', 'TYPECLASS_SIZE', 'DATATYPE'])}),
    'MPI_TYPE_NULL_COPY_FN': (False, {7: ([True, True, True, True, False, True, True],
                                          ['DATATYPE', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL',
                                           'ERROR_CODE']), 6: (
        [True, True, True, True, False, True], ['DATATYPE', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_TYPE_NULL_DELETE_FN': (False, {5: (
        [True, True, True, True, True],
        ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE', 'ERROR_CODE_SHOW_INTENT']),
        4: ([True, True, True, True],
            ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE'])}),
    'MPI_Type_set_attr': (False, {4: ([True, True, True, True], ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL', 'ERROR_CODE']),
                                  3: ([True, True, True], ['DATATYPE', 'KEYVAL', 'ATTRIBUTE_VAL'])}),
    'MPI_Type_set_name': (
        False,
        {3: ([True, True, True], ['DATATYPE', 'STRING', 'ERROR_CODE']), 2: ([True, True], ['DATATYPE', 'STRING'])}),
    'MPI_Type_size': (False, {3: ([True, True, True], ['DATATYPE', 'POLYXFER_NUM_ELEM', 'ERROR_CODE']),
                              2: ([True, True], ['DATATYPE', 'POLYXFER_NUM_ELEM'])}), 'MPI_Type_size_x': (False, {
        3: ([True, True, True], ['DATATYPE', 'XFER_NUM_ELEM', 'ERROR_CODE']),
        2: ([True, True], ['DATATYPE', 'XFER_NUM_ELEM'])}), 'MPI_Type_vector': (False, {6: (
        [True, False, True, True, True, True],
        ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDTYPE_NUM_ELEM', 'DATATYPE', 'newDATATYPE', 'ERROR_CODE']), 5: (
        [True, False, True, True, True], ['POLYDTYPE_NUM_ELEM_NNI', 'POLYDTYPE_NUM_ELEM', 'DATATYPE', 'newDATATYPE'])}),
    'MPI_Unpack': (False, {8: ([True, True, True, False, True, True, True, True],
                               ['BUFFER', 'POLYNUM_BYTES_NNI', 'POLYDISPLACEMENT_COUNT', 'POLYDTYPE_NUM_ELEM',
                                'DATATYPE', 'COMMUNICATOR', 'ERROR_CODE']), 7: (
        [True, True, True, False, True, True, True],
        ['BUFFER', 'POLYNUM_BYTES_NNI', 'POLYDISPLACEMENT_COUNT', 'POLYDTYPE_NUM_ELEM', 'DATATYPE', 'COMMUNICATOR'])}),
    'MPI_Unpack_external': (False, {8: ([True, True, True, True, False, True, True, True],
                                        ['STRING', 'BUFFER', 'POLYDTYPE_PACK_SIZE', 'POLYLOCATION',
                                         'POLYDTYPE_NUM_ELEM', 'DATATYPE', 'ERROR_CODE']), 7: (
        [True, True, True, True, False, True, True],
        ['STRING', 'BUFFER', 'POLYDTYPE_PACK_SIZE', 'POLYLOCATION', 'POLYDTYPE_NUM_ELEM', 'DATATYPE'])}),
    'MPI_Unpublish_name': (False, {4: ([True, True, False, True], ['STRING', 'INFO', 'ERROR_CODE']),
                                   3: ([True, True, False], ['STRING', 'INFO'])}),
    'MPI_User_function': (False, {4: ([True, False, True, True], ['C_BUFFER4', 'POLYXFER_NUM_ELEM', 'DATATYPE'])}),
    'MPI_Wait': (
        False,
        {3: ([True, True, True], ['REQUEST', 'STATUS', 'ERROR_CODE']), 2: ([True, True], ['REQUEST', 'STATUS'])}),
    'MPI_Waitall': (False, {4: ([True, True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'STATUS', 'ERROR_CODE']),
                            3: ([True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'STATUS'])}), 'MPI_Waitany': (False,
                                                                                                                  {5: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'ARRAY_LENGTH_NNI',
                                                                                                                          'REQUEST',
                                                                                                                          'INDEX',
                                                                                                                          'STATUS',
                                                                                                                          'ERROR_CODE']),
                                                                                                                      4: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'ARRAY_LENGTH_NNI',
                                                                                                                          'REQUEST',
                                                                                                                          'INDEX',
                                                                                                                          'STATUS'])}),
    'MPI_Waitsome': (False, {6: ([True, True, True, True, True, True],
                                 ['ARRAY_LENGTH_NNI', 'REQUEST', 'ARRAY_LENGTH', 'INDEX', 'STATUS', 'ERROR_CODE']), 5: (
        [True, True, True, True, True], ['ARRAY_LENGTH_NNI', 'REQUEST', 'ARRAY_LENGTH', 'INDEX', 'STATUS'])}),
    'MPI_Win_allocate': (False, {7: ([True, True, True, True, True, True, True],
                                     ['WINDOW_SIZE', 'POLYRMA_DISPLACEMENT', 'INFO', 'COMMUNICATOR', 'C_BUFFER',
                                      'WINDOW', 'ERROR_CODE']), 6: ([True, True, True, True, True, True],
                                                                    ['WINDOW_SIZE', 'POLYRMA_DISPLACEMENT', 'INFO',
                                                                     'COMMUNICATOR', 'C_BUFFER', 'WINDOW'])}),
    'MPI_Win_allocate_shared': (False, {7: ([True, True, True, True, True, True, True],
                                            ['WINDOW_SIZE', 'POLYRMA_DISPLACEMENT', 'INFO', 'COMMUNICATOR', 'C_BUFFER',
                                             'WINDOW', 'ERROR_CODE']), 6: ([True, True, True, True, True, True],
                                                                           ['WINDOW_SIZE', 'POLYRMA_DISPLACEMENT',
                                                                            'INFO', 'COMMUNICATOR', 'C_BUFFER',
                                                                            'WINDOW'])}), 'MPI_Win_attach': (False, {
        4: ([True, True, True, True], ['WINDOW', 'BUFFER', 'WIN_ATTACH_SIZE', 'ERROR_CODE']),
        3: ([True, True, True], ['WINDOW', 'BUFFER', 'WIN_ATTACH_SIZE'])}),
    'MPI_Win_c2f': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}),
    'MPI_Win_call_errhandler': (
        False, {3: ([True, True, False], ['WINDOW', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'ERROR_CODE'])}),
    'MPI_Win_complete': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}),
    'MPI_Win_copy_attr_function': (False, {7: ([True, True, True, True, False, True, True],
                                               ['WINDOW', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL',
                                                'ERROR_CODE']), 6: (
        [True, True, True, True, False, True], ['WINDOW', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_Win_create': (False, {7: ([True, True, True, True, True, True, True],
                                   ['BUFFER', 'WINDOW_SIZE', 'POLYRMA_DISPLACEMENT', 'INFO', 'COMMUNICATOR', 'WINDOW',
                                    'ERROR_CODE']), 6: ([True, True, True, True, True, True],
                                                        ['BUFFER', 'WINDOW_SIZE', 'POLYRMA_DISPLACEMENT', 'INFO',
                                                         'COMMUNICATOR', 'WINDOW'])}), 'MPI_Win_create_dynamic': (False,
                                                                                                                  {4: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'INFO',
                                                                                                                          'COMMUNICATOR',
                                                                                                                          'WINDOW',
                                                                                                                          'ERROR_CODE']),
                                                                                                                      3: (
                                                                                                                      [
                                                                                                                          True,
                                                                                                                          True,
                                                                                                                          True],
                                                                                                                      [
                                                                                                                          'INFO',
                                                                                                                          'COMMUNICATOR',
                                                                                                                          'WINDOW'])}),
    'MPI_Win_create_errhandler': (False, {3: ([True, True, True], ['FUNCTION', 'ERRHANDLER', 'ERROR_CODE']),
                                          2: ([True, True], ['FUNCTION', 'ERRHANDLER'])}), 'MPI_Win_create_keyval': (
        False, {5: ([True, False, True, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE', 'ERROR_CODE']),
                4: ([True, False, True, True], ['FUNCTION', 'KEYVAL', 'EXTRA_STATE'])}), 'MPI_Win_delete_attr': (
        False, {3: ([True, True, True], ['WINDOW', 'KEYVAL', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'KEYVAL'])}),
    'MPI_Win_delete_attr_function': (False, {
        5: ([True, True, True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE'])}), 'MPI_Win_detach': (
        False, {3: ([True, True, True], ['WINDOW', 'BUFFER', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'BUFFER'])}),
    'MPI_WIN_DUP_FN': (False, {7: ([True, True, True, True, False, True, True],
                                   ['WINDOW', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']), 6: (
        [True, True, True, True, False, True], ['WINDOW', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_Win_errhandler_function': (True, {2: ([True, True], ['WINDOW', 'ERROR_CODE'])}),
    'MPI_Win_f2c': (False, {2: ([True, True], ['F90_WIN', 'ERROR_CODE']), 1: ([True], ['F90_WIN'])}), 'MPI_Win_fence': (
        False, {3: ([True, True, True], ['ASSERT', 'WINDOW', 'ERROR_CODE']), 2: ([True, True], ['ASSERT', 'WINDOW'])}),
    'MPI_Win_flush': (
        False,
        {3: ([True, True, True], ['RANK_NNI', 'WINDOW', 'ERROR_CODE']), 2: ([True, True], ['RANK_NNI', 'WINDOW'])}),
    'MPI_Win_flush_all': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}),
    'MPI_Win_flush_local': (
        False,
        {3: ([True, True, True], ['RANK_NNI', 'WINDOW', 'ERROR_CODE']), 2: ([True, True], ['RANK_NNI', 'WINDOW'])}),
    'MPI_Win_flush_local_all': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}),
    'MPI_Win_free': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}),
    'MPI_Win_free_keyval': (False, {2: ([True, True], ['KEYVAL', 'ERROR_CODE']), 1: ([True], ['KEYVAL'])}),
    'MPI_Win_get_attr': (False, {
        5: ([True, True, True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']),
        4: ([True, True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL', 'LOGICAL'])}), 'MPI_Win_get_errhandler': (
        False,
        {3: ([True, True, True], ['WINDOW', 'ERRHANDLER', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'ERRHANDLER'])}),
    'MPI_Win_get_group': (
        False, {3: ([True, True, True], ['WINDOW', 'GROUP', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'GROUP'])}),
    'MPI_Win_get_info': (
        False, {3: ([True, True, True], ['WINDOW', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'INFO'])}),
    'MPI_Win_get_name': (False, {4: ([True, True, True, True], ['WINDOW', 'STRING', 'STRING_LENGTH', 'ERROR_CODE']),
                                 3: ([True, True, True], ['WINDOW', 'STRING', 'STRING_LENGTH'])}), 'MPI_Win_lock': (
        False, {5: ([True, True, True, True, True], ['LOCK_TYPE', 'RANK_NNI', 'ASSERT', 'WINDOW', 'ERROR_CODE']),
                4: ([True, True, True, True], ['LOCK_TYPE', 'RANK_NNI', 'ASSERT', 'WINDOW'])}), 'MPI_Win_lock_all': (
        False, {3: ([True, True, True], ['ASSERT', 'WINDOW', 'ERROR_CODE']), 2: ([True, True], ['ASSERT', 'WINDOW'])}),
    'MPI_WIN_NULL_COPY_FN': (False, {7: ([True, True, True, True, False, True, True],
                                         ['WINDOW', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL', 'ERROR_CODE']),
                                     6: ([True, True, True, True, False, True],
                                         ['WINDOW', 'KEYVAL', 'EXTRA_STATE', 'ATTRIBUTE_VAL', 'LOGICAL'])}),
    'MPI_WIN_NULL_DELETE_FN': (False, {
        5: ([True, True, True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE', 'ERROR_CODE']),
        4: ([True, True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL', 'EXTRA_STATE'])}), 'MPI_Win_post': (False, {
        4: ([True, True, True, True], ['GROUP', 'ASSERT', 'WINDOW', 'ERROR_CODE']),
        3: ([True, True, True], ['GROUP', 'ASSERT', 'WINDOW'])}), 'MPI_Win_set_attr': (False, {
        4: ([True, True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL', 'ERROR_CODE']),
        3: ([True, True, True], ['WINDOW', 'KEYVAL', 'ATTRIBUTE_VAL'])}), 'MPI_Win_set_errhandler': (False, {
        3: ([True, True, True], ['WINDOW', 'ERRHANDLER', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'ERRHANDLER'])}),
    'MPI_Win_set_info': (
        False, {3: ([True, True, True], ['WINDOW', 'INFO', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'INFO'])}),
    'MPI_Win_set_name': (
        False, {3: ([True, True, True], ['WINDOW', 'STRING', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'STRING'])}),
    'MPI_Win_shared_query': (False, {6: ([True, True, True, True, True, True],
                                         ['WINDOW', 'RANK_NNI', 'WINDOW_SIZE', 'POLYRMA_DISPLACEMENT', 'C_BUFFER',
                                          'ERROR_CODE']), 5: (
        [True, True, True, True, True], ['WINDOW', 'RANK_NNI', 'WINDOW_SIZE', 'POLYRMA_DISPLACEMENT', 'C_BUFFER'])}),
    'MPI_Win_start': (False, {4: ([True, True, True, True], ['GROUP', 'ASSERT', 'WINDOW', 'ERROR_CODE']),
                              3: ([True, True, True], ['GROUP', 'ASSERT', 'WINDOW'])}),
    'MPI_Win_sync': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}), 'MPI_Win_test': (
        False,
        {3: ([True, True, True], ['WINDOW', 'LOGICAL', 'ERROR_CODE']), 2: ([True, True], ['WINDOW', 'LOGICAL'])}),
    'MPI_Win_unlock': (
        False,
        {3: ([True, True, True], ['RANK_NNI', 'WINDOW', 'ERROR_CODE']), 2: ([True, True], ['RANK_NNI', 'WINDOW'])}),
    'MPI_Win_unlock_all': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}),
    'MPI_Win_wait': (False, {2: ([True, True], ['WINDOW', 'ERROR_CODE']), 1: ([True], ['WINDOW'])}),
    'MPI_Wtick': (False, {0: ([], [])}), 'MPI_Wtime': (False, {0: ([], [])})}
