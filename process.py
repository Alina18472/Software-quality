import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from ui_dialog import *
from radar_diagram import RadarDiagram
from functions import pend, function_list, fak_1, fak_2, fak_3, fak_4, fak_5, fak_6
from random import randint

# словать ф-ий, key - индекс выбранной ф-ии, value - соотвевующее уравнение
dict_of_function_expressions = dict()
# матрица свободных членов в ур-ях
free_members_of_fun_expr = []

data_sol = []


def init():
    dict_of_function_expressions[1] = function_0
    dict_of_function_expressions[2] = function_1
    dict_of_function_expressions[3] = function_2
    dict_of_function_expressions[4] = function_3
    dict_of_function_expressions[5] = function_4
    dict_of_function_expressions[6] = function_5
    dict_of_function_expressions[7] = function_6


def handle(ui):
    # init()
    ui.pushButton_2.clicked.connect(lambda: ui.label_15.setPixmap(QtGui.QPixmap('./figure.png')))
    ui.pushButton_3.clicked.connect(lambda: fillDiagrams(ui, data_sol, labels_array()))
    ui.pushButton_4.clicked.connect(lambda: ui.label_56.setPixmap(QtGui.QPixmap('./figure2.png')))
    ui.comboBox_1.activated[str].connect(lambda text: activatedCombox(0, text))
    ui.comboBox_2.activated[str].connect(lambda text: activatedCombox(1, text))
    ui.comboBox_3.activated[str].connect(lambda text: activatedCombox(2, text))
    ui.comboBox_4.activated[str].connect(lambda text: activatedCombox(3, text))
    ui.comboBox_5.activated[str].connect(lambda text: activatedCombox(4, text))
    ui.comboBox_6.activated[str].connect(lambda text: activatedCombox(5, text))
    ui.comboBox_7.activated[str].connect(lambda text: activatedCombox(6, text))
    ui.pushButton.clicked.connect(lambda: process(ui, [
        [
            float(ui.begin_expression_lineEdit_1.text()),
            float(ui.begin_expression_lineEdit_2.text()),
            float(ui.begin_expression_lineEdit_3.text()),
            float(ui.begin_expression_lineEdit_4.text()),
            float(ui.begin_expression_lineEdit_5.text()),
            float(ui.begin_expression_lineEdit_6.text()),
            float(ui.begin_expression_lineEdit_7.text()),
            float(ui.begin_expression_lineEdit_8.text()),
            float(ui.begin_expression_lineEdit_9.text()),
            float(ui.begin_expression_lineEdit_10.text()),
            float(ui.begin_expression_lineEdit_11.text()),
            float(ui.begin_expression_lineEdit_12.text()),
            float(ui.begin_expression_lineEdit_13.text()),
            float(ui.begin_expression_lineEdit_14.text()),
            float(ui.begin_expression_lineEdit_15.text()),
            float(ui.begin_expression_lineEdit_16.text()),
            float(ui.begin_expression_lineEdit_17.text()),
            float(ui.begin_expression_lineEdit_18.text()),
            float(ui.begin_expression_lineEdit_19.text()),
            float(ui.begin_expression_lineEdit_20.text()),
            float(ui.begin_expression_lineEdit_21.text()),
            float(ui.begin_expression_lineEdit_22.text()),
            float(ui.begin_expression_lineEdit_23.text()),
            float(ui.begin_expression_lineEdit_24.text()),
            float(ui.begin_expression_lineEdit_25.text()),
            float(ui.begin_expression_lineEdit_26.text()),
            float(ui.begin_expression_lineEdit_27.text()),
            float(ui.begin_expression_lineEdit_28.text())
        ],
        [
            [float(ui.expression_lineEdit_1_1.text()), float(ui.expression_lineEdit_1_2.text()),
             float(ui.expression_lineEdit_1_3.text()), float(ui.expression_lineEdit_1_4.text())],
            [float(ui.expression_lineEdit_2_1.text()), float(ui.expression_lineEdit_2_1.text())],
            [float(ui.expression_lineEdit_3_1.text()), float(ui.expression_lineEdit_3_2.text()),
             float(ui.expression_lineEdit_3_3.text())],
            [float(ui.expression_lineEdit_4_1.text()), float(ui.expression_lineEdit_4_2.text())],
            [float(ui.expression_lineEdit_5_1.text()), float(ui.expression_lineEdit_5_2.text()),
             float(ui.expression_lineEdit_5_3.text())],
            [float(ui.expression_lineEdit_6_1.text()), float(ui.expression_lineEdit_6_2.text())],
            [float(ui.expression_lineEdit_7_1.text()), float(ui.expression_lineEdit_7_2.text()),
             float(ui.expression_lineEdit_7_3.text())],
        ]
    ]))


def activatedCombox(index, text):
    if index == 0:
        dict_of_function_expressions[int(text)] = function_0
    elif index == 1:
        dict_of_function_expressions[int(text)] = function_1
    elif index == 2:
            dict_of_function_expressions[int(text)] = function_2
    elif index == 3:
            dict_of_function_expressions[int(text)] = function_3
    elif index == 4:
            dict_of_function_expressions[int(text)] = function_4
    elif index == 5:
            dict_of_function_expressions[int(text)] = function_5
    elif index == 6:
            dict_of_function_expressions[int(text)] = function_6


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
    fig = plt.figure(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    for i in t:
        y1.append(fak_1(i))
        y2.append(fak_2(i))
        y3.append(fak_3(i))
        y4.append(fak_4(i))
        y5.append(fak_5(i))
        y6.append(fak_6(i))
    plt.plot(t, y1, label='Fak1')
    plt.plot(t, y2, label='Fak2')
    plt.plot(t, y3, label='Fak3')
    plt.plot(t, y4, label='Fak4')
    plt.plot(t, y5, label='Fak5')
    plt.plot(t, y6, label='Fak6')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    fig.savefig("./figure2.png")

def fillDiagrams(ui, data, labels):
    radar1 = RadarDiagram()
    radar1.draw('./diagram.png', [data[0]], labels, "Характеристики системы в начальный момент времени")
    radar1.draw('./diagram2.png', (data[0], data[int(len(data)/4)]), labels, "Характеристики системы в 1 четверти")
    radar1.draw('./diagram3.png', (data[0], data[int(len(data)/2)]), labels, "Характеристики системы во 2 четверти")
    radar1.draw('./diagram4.png', (data[0], data[int(len(data))-1]), labels, "Характеристики системы в 3 четверти")
    radar1.draw('./diagram5.png', (data[0], data[int(len(data))-1]), labels, "Характеристики системы в последний момент времени")
    ui.label_53.setPixmap(QtGui.QPixmap('./diagram.png'))
    ui.label_54.setPixmap(QtGui.QPixmap('./diagram2.png'))
    ui.label_38.setPixmap(QtGui.QPixmap('./diagram3.png'))
    ui.label_55.setPixmap(QtGui.QPixmap('./diagram4.png'))
    ui.label_62.setPixmap(QtGui.QPixmap('./diagram5.png'))


# Выявление из краткой записи ф-ий дифф. ур-ий какие необходимо заменить на уравнения, а какие удалить (превратить в 1)
def process_function_list(num_functions):
    new_function_list = []
    for ind, expression in enumerate(function_list):
        new_expression = []
        for ind2, part in enumerate(expression):
            new_expression.append(np.intersect1d(list(part), num_functions))
            function_list[ind][ind2] = recreate(new_expression[ind2], part)

def recreate(new_expression, part):
    new_part = {}
    for ind in new_expression:
        new_part[ind] = part[ind]
    return new_part

def create_graphic(t, data):
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    for i in range(28):
        plt.plot(t, data[:, i])
    plt.legend(loc='best')
    plt.xlabel('t')
    axs.legend(labels_array(), loc=(.75, .64),
                            labelspacing=0.1, fontsize='small')
    plt.grid()

    plt.xlim([0, 1])
    draw_third_graphic(t)
    #
    # plt.subplot(121)
    # plt.plot(sol.t, sol.y[0], color="#8B008B")
    # plt.plot(sol.t, sol.y[0], color="#FF8C00")
    # plt.xlabel('t')
    # plt.ylabel('S(t)')
    # plt.tight_layout()
    # plt.show()
    fig.savefig('./figure.png')

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
        "невысокий уровень используемого языка",
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

def process(ui, numbers):
    global data_sol
    global free_members_of_fun_expr
    start_value = numbers[0]

    free_members_of_fun_expr = numbers[1]
    t = np.linspace(0, 1, 80)
    process_function_list(list(dict_of_function_expressions.keys()))

    data_sol = odeint(pend, start_value, t, args=(dict_of_function_expressions, function_list))
    ui.expression_lineEdit_41.setText("Выполнено")
    create_graphic(t, data_sol)