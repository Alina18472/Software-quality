
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from radar_diagram import RadarDiagram
import functions
import streamlit as st

dict_of_function_expressions = dict()
free_members_of_fun_expr = []
data_sol = []


def init():
    """Инициализация функций"""
    dict_of_function_expressions[1] = function_0
    dict_of_function_expressions[2] = function_1
    dict_of_function_expressions[3] = function_2
    dict_of_function_expressions[4] = function_3
    dict_of_function_expressions[5] = function_4
    dict_of_function_expressions[6] = function_5
    dict_of_function_expressions[7] = function_6


def init_default_functions():
    """Инициализация функций по умолчанию"""
    global dict_of_function_expressions
    dict_of_function_expressions.clear()
    dict_of_function_expressions[1] = function_0
    dict_of_function_expressions[2] = function_1  
    dict_of_function_expressions[3] = function_2
    dict_of_function_expressions[4] = function_3
    dict_of_function_expressions[5] = function_4
    dict_of_function_expressions[6] = function_5
    dict_of_function_expressions[7] = function_6


def activatedCombox(index, text):
   
    try:
        func_num = int(text)
        if index == 0:
            dict_of_function_expressions[func_num] = function_0
        elif index == 1:
            dict_of_function_expressions[func_num] = function_1
        elif index == 2:
            dict_of_function_expressions[func_num] = function_2
        elif index == 3:
            dict_of_function_expressions[func_num] = function_3
        elif index == 4:
            dict_of_function_expressions[func_num] = function_4
        elif index == 5:
            dict_of_function_expressions[func_num] = function_5
        elif index == 6:
            dict_of_function_expressions[func_num] = function_6
    except ValueError:
        st.error(f"Ошибка: неверный номер функции '{text}'")


def function_0(u):
    return free_members_of_fun_expr[0][0] * u ** 3 + \
           free_members_of_fun_expr[0][1] * u ** 2 + \
           free_members_of_fun_expr[0][2] * u + \
           free_members_of_fun_expr[0][3]


def function_1(u):
    return free_members_of_fun_expr[1][0] * u + \
           free_members_of_fun_expr[1][1]


def function_2(u):
    return free_members_of_fun_expr[2][0] * u ** 2 + \
           free_members_of_fun_expr[2][1] * u + \
           free_members_of_fun_expr[2][2]


def function_3(u):
    return free_members_of_fun_expr[3][0] * u + \
           free_members_of_fun_expr[3][1]


def function_4(u):
    return free_members_of_fun_expr[4][0] * u ** 2 + \
           free_members_of_fun_expr[4][1] * u + \
           free_members_of_fun_expr[4][2]


def function_5(u):
    return free_members_of_fun_expr[5][0] * u + \
           free_members_of_fun_expr[5][1]


def function_6(u):
    return free_members_of_fun_expr[6][0] * u ** 2 + \
           free_members_of_fun_expr[6][1] * u + \
           free_members_of_fun_expr[6][2]


def draw_third_graphic(t):
    """График возмущений"""
    global free_members_of_fun_expr
    fig = plt.figure(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    for i in t:
        y1.append(free_members_of_fun_expr[0][0] * i**3 +
                 free_members_of_fun_expr[0][1] * i**2 +
                 free_members_of_fun_expr[0][2] * i +
                 free_members_of_fun_expr[0][3])
        y2.append(free_members_of_fun_expr[1][0] * i +
                 free_members_of_fun_expr[1][1])
        y3.append(free_members_of_fun_expr[2][0] * i**2 +
                 free_members_of_fun_expr[2][1] * i +
                 free_members_of_fun_expr[2][2])
        y4.append(free_members_of_fun_expr[3][0] * i +
                 free_members_of_fun_expr[3][1])
        y5.append(free_members_of_fun_expr[4][0] * i**2 +
                 free_members_of_fun_expr[4][1] * i +
                 free_members_of_fun_expr[4][2])
        y6.append(free_members_of_fun_expr[5][0] * i +
                 free_members_of_fun_expr[5][1])
    plt.plot(t, y1, label='Fak1')
    plt.plot(t, y2, label='Fak2')
    plt.plot(t, y3, label='Fak3')
    plt.plot(t, y4, label='Fak4')
    plt.plot(t, y5, label='Fak5')
    plt.plot(t, y6, label='Fak6')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    return fig


def create_radar_diagrams(data, labels):
    radar = RadarDiagram()
    diagrams = []
    
    moments = [
        ([data[0]], "Характеристики системы в начальный момент времени"),
        ([data[0], data[int(len(data) / 4)]], "Характеристики системы в 1 четверти"),
        ([data[0], data[int(len(data) / 2)]], "Характеристики системы во 2 четверти"),
        ([data[0], data[int(len(data)) - 1]], "Характеристики системы в 3 четверти"),
        ([data[0], data[int(len(data)) - 1]], "Характеристики системы в последний момент времени")
    ]
    
    for data_moment, title in moments:
        fig = radar.draw(data_moment, labels, title)
        diagrams.append((fig, title))
    
    return diagrams


def process_function_list(num_functions):
    new_function_list = []
    for ind, expression in enumerate(functions.function_list):
        new_expression = []
        for ind2, part in enumerate(expression):
            new_expression.append(np.intersect1d(list(part), num_functions))
            functions.function_list[ind][ind2] = recreate(new_expression[ind2], part)


def recreate(new_expression, part):
    new_part = {}
    for ind in new_expression:
        new_part[ind] = part[ind]
    return new_part


def create_graphic(t, data):
    """График характеристик"""
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    labels = labels_array()
    for i in range(28):
        plt.plot(t, data[:, i], label=labels[i])
    plt.legend(loc='best')
    plt.xlabel('t')
    axs.legend(labels, loc=(.75, .64),
               labelspacing=0.1, fontsize='small')
    plt.grid()
    plt.xlim([0, 1])
    return fig


def labels_array():
    return [
        "сопровождаемость",
        "анализируемость",
        "изменяемость",
        "стабильность",
        "тестируемость",
        "согласованность",
        "несоответствие комплектности",
        "несоответствие стандартам",
        "отсутствие лицензии на ПО",
        "устаревшие технологии кодирования",
        "отсутствие иерархии модулей ПО",
        "низкая читабельность кода",
        "недостаточно комментариев",
        "отсутствие системного подхода при выделении модулей",
        "слишком большие модули",
        "недостатки средств диагностики",
        "недостаточность средств регистрации процесса выполнения",
        "высокая трудоемкость внесения изменений",
        "низкий уровень параметризации",
        "низкая локальность модификации",
        "вторичные дефекты после модификации",
        "недостаточность требований к тестированию ПО",
        "отсутствие описания методов испытаний ПО",
        "невозможность разработки теста для выполенния требований",
        "невозможность использования средств тестирования",
        "несоответствие требованиям стандартов сопровождаемости",
        "несоответствие требованиям к исходным текстам программ",
        "отсутствие регистрации изменений"
    ]


def process_calculation(start_values, free_members):
    """Основная функция расчета"""
    global data_sol
    global free_members_of_fun_expr
    
    plt.close('all')

    free_members_of_fun_expr = free_members
    t = np.linspace(0, 1, 80)
    
    process_function_list(list(dict_of_function_expressions.keys()))

    data_sol = odeint(functions.pend, start_values, t, 
                     args=(dict_of_function_expressions, functions.function_list))
    
    return t, data_sol