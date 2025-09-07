import numpy as np
# краткая запись ф-ий в дифференциальных ур-ях
function_list = np.array([
    # 0
    [
        {1: 3},
        {2: 6, 3: 7, 4: 8, 5: 11, 6: 12, 7: 15, 8: 25, 9: 26}
    ],
    # 1
    [
        [],
        {10: 6, 11: 7, 12: 16, 13: 26}
    ],
    # 2
    [
        {},
        {10: 6, 11: 7, 12: 16, 13: 26}
    ],
    # 3
    [
        {32: 4, 33: 5, 34: 17},
        {35: 2, 36: 15, 37: 16, 38: 19, 39: 20, 40: 26}
    ],
    # 4
    [
        {},
        {41: 21, 42: 22, 43: 23, 44: 24}
    ],
    # 5
    [
        {45: 1},
        {46: 6, 47: 7, 48: 10, 49: 13, 50: 14, 51: 14, 52: 26}
    ],
    # 6
    [
        {53: 7, 54: 25, 55: 26},
        {56: 0, 57: 1, 58: 5}
    ],
    # 7
    [
        {59: 6, 60: 25, 61: 26},
        {62: 0, 63: 1}
    ],
    # 8
    [
        {},
        {64: 0}
    ],
    # 9
    [
        {},
        {65: 2}
    ],
    # 10
    [
        {66: 11, 67: 12, 68: 13, 69: 14},
        {70: 2, 71: 5}
    ],
    # 11
    [
        {72: 9, 73: 10, 74: 12, 75: 13, 76: 14, 77: 18, 78: 19},
        {79: 0, 80: 2}
    ],
    # 12
    [
        {},
        {86: 0, 87: 2, 88: 5}
    ],
    # 13
    [
        {83: 9, 84: 10, 85: 14},
        {86: 0, 87: 2, 88: 5}
    ],
    # 14
    [
        {89: 10, 90: 13},
        {91: 2, 92: 5}
    ],
    # 15
    [
        {93: 21, 94: 22, 95: 23, 96: 25, 97: 26},
        {98: 0, 99: 3}
    ],
    # 16
    [
        {100: 15, 101: 26, 102: 27},
        {103: 0, 104: 3}
    ],
    # 17
    [
        {105: 9, 106: 10, 107: 11, 108: 12, 109: 13, 110: 14, 111: 19, 112: 20, 113: 26, 114: 27},
        {115: 2}
    ],
    # 18
    [
        {116: 9, 117: 26},
        {118: 1, 119: 2, 120: 5}
    ],
    # 19
    [
        {121: 9, 122: 10, 123: 13, 124: 14, 125: 26},
        {126: 1, 127: 2}
    ],
    # 20
    [
        {128: 9, 129: 11, 130: 12, 131: 14, 132: 17, 133: 19, 134: 21, 135: 22, 136: 23},
        {137: 2}
    ],
    # 21
    [
        {138: 22, 139: 23, 140: 24, 141: 26},
        {142: 2, 143: 4}
    ],
    # 22
    [
        {144: 6, 145: 21, 146: 23, 147: 24, 148: 25},
        {149: 4}
    ],
    # 23
    [
        {150: 6, 151: 7, 152: 16, 153: 21, 154: 22, 155: 24},
        {156: 1, 157: 4, 158: 5}
    ],
    # 24
    [
        {159: 22},
        {160: 4}
    ],
    # 25
    [
        {161: 6, 162: 7, 163: 8, 164: 15, 165: 16, 166: 17, 167: 20, 168: 27},
        {169: 0, 170: 1, 171: 5}
    ],
    # 26
    [
        {172: 6, 173: 7, 174: 9, 175: 10, 176: 11, 177: 12, 178: 13, 179: 14, 180: 27},
        {181: 0, 182: 1}
    ],
    # 27
    [
        {183: 6, 184: 17, 185: 20},
        {186: 0, 187: 2}
    ]
], dtype=object)


def process_part_of_expression(u,
                               fak_list,
                               t,
                               dict_of_function_expressions,
                               new_function_list,
                               index_expression,
                               index_side):
    result = 1
    result_fak = 0

    for num_function in new_function_list[index_expression][index_side]:
        result *= dict_of_function_expressions[num_function](u[new_function_list[index_expression][index_side][num_function]])
    for fak in fak_list:
        result_fak += fak(t)
    return result * result_fak


def fak_1(t):
    return t**2 + 1


def fak_2(t):
    return np.cos(1.5 * t * np.pi - np.pi / 6) ** 2 / 4 + 0.2


def fak_3(t):
    return np.sin(t * np.pi - np.pi / 6) / 2.5 + 0.3


def fak_4(t):
    return 2*t - 1


def fak_5(t):
    return np.cos(1.5 * t * np.pi - np.pi / 6) ** 2 / 4


def fak_6(t):
    return np.sin(t * np.pi - np.pi / 6) ** 2 / 2.5 + 0.3


def pend(u, t, dict_of_function_expressions, new_function_list):
    dudt = [
        # 0
        (process_part_of_expression(u,
                                    [fak_1, fak_2, fak_6],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list, 0, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list, 0, 1)),

        # 1
        (process_part_of_expression(u,
                                    [fak_1, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    1, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    1, 1)),

        # 2
        (process_part_of_expression(u,
                                    [fak_1, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    2, 0)
         -
         process_part_of_expression( u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    2, 1)),

        # 3
        (process_part_of_expression(u,
                                    [fak_1, fak_2, fak_5, fak_6],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    3, 0)
         -
         process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    3, 1)),

        # 4
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    4, 0)
         -
         process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list, 4, 1)),

        # 5
        (process_part_of_expression(u,
                                    [fak_1,
                                     fak_2],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    5, 0)
         -
         process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    5, 1)),

        # 6
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    6, 0)
         -
         process_part_of_expression(u,
                                    [fak_1,
                                     fak_2],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    6, 1)),

        # 7
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    7, 0) -
         process_part_of_expression(u,
                                    [fak_1, fak_2],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    7, 1)),

        # 8
        (process_part_of_expression(u,
                                    [fak_4],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    8, 0)
         -
         process_part_of_expression(u,
                                    [fak_5, fak_6],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    8, 1)),

        # 9
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    9, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    9, 1)),

        # 10
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    10, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    10, 1)),

        # 11
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    11, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_5],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    11, 1)),

        # 12
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    12, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    12, 1)),

        # 13
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    13, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    13, 1)),

        # 14
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    14, 0)
         -
         process_part_of_expression(u, [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    14, 1)),

        # 15
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    15, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_2],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    15, 1)),

        # 16
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    16, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    16, 1)),

        # 17
        (process_part_of_expression(
            u,
            [fak_3],
            t,
            dict_of_function_expressions,
            new_function_list,
            17, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    17, 1)),

        # 18
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    18, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    18, 1)),

        # 19
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    19, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    1, 1)),

        # 20
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    19, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    19, 1)),

        # 21
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    21, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    21, 1)),

        # 22
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    22, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    22, 1)),

        # 23
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    23, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_2],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    23, 1)),

        # 24
        (process_part_of_expression(u,
                                    [fak_4],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    24, 0)
         -
         process_part_of_expression(u,
                                    [fak_5, fak_6],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    24, 1)),

        # 25
       (process_part_of_expression(u,
                                    [fak_4],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    25, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_2, fak_5, fak_6],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    25, 1)),

        # 26
        (process_part_of_expression(u,
                                    [],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    26, 0)
         -
         process_part_of_expression(u,
                                    [fak_1, fak_2, fak_5, fak_6],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    26, 1)),

        # 27
        (process_part_of_expression(u,
                                    [fak_3],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    27, 0)
         -
         process_part_of_expression(u,
                                    [fak_1],
                                    t,
                                    dict_of_function_expressions,
                                    new_function_list,
                                    27, 1)),
    ]
    return dudt
