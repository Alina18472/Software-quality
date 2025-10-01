

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import functions
import process
from radar_diagram import RadarDiagram


st.set_page_config(page_title="Модель ISO", layout="wide")

# Инициализация сессии
if 'data_sol' not in st.session_state:
    st.session_state.data_sol = None
if 'calculation_done' not in st.session_state:
    st.session_state.calculation_done = False
if 'free_members' not in st.session_state:
    st.session_state.free_members = None

# Заголовок
st.title("Модель ISO - Анализ качества программного обеспечения")

# Вкладки 
tab1, tab2, tab3, tab4 = st.tabs(["Параметры", "Графики", "Диаграмма", "Возмущение"])


with tab1:
    # Основной контейнер с двумя колонками
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Группа "Входные параметры" - 28 полей ввода
        st.header("Входные параметры")
        
        start_values = []
        labels = process.labels_array()
        
        # Создаем 28 полей ввода в 2 колонки для компактности
        cols = st.columns(2)
        for i in range(28):
            with cols[i % 2]:
                # Устанавливаем значения по умолчанию как в оригинале
                default_value = 0.9 if i == 0 else 0.5
                if i in [27, 26, 25, 24, 22, 23, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    # Устанавливаем специфичные значения как в оригинале
                    defaults = {
                        1: 0.9, 2: 0.6, 3: 0.7, 4: 0.5, 5: 0.4, 6: 0.9, 7: 0.24, 8: 0.567, 9: 0.234,
                        10: 0.52, 11: 0.25, 12: 0.678, 13: 0.7534, 14: 0.67, 15: 0.3, 16: 0.4, 17: 0.6,
                        18: 0.234, 19: 0.42, 20: 0.56, 21: 0.89, 22: 0.9, 23: 0.54, 24: 0.67, 25: 0.64,
                        26: 0.873, 27: 0.43
                    }
                    default_value = defaults.get(i, 0.5)
                
                value = st.number_input(
                    labels[i],
                    value=default_value,
                    min_value=0.0,
                    max_value=1.0,
                    key=f"param_{i}"
                )
                start_values.append(value)
    
    with col2:
        # Группа "Уравнения" - 7 функций 
        st.header("Уравнения")
        
        free_members = []
        selected_functions = []
        
        # Function 1 - кубическая (ax³ + bx² + cx + d)
        st.subheader("F(x) = ax³ + bx² + cx + d")
        col_f1_header = st.columns([1, 3])
        with col_f1_header[0]:
            func1_select = st.selectbox(
                f"F(x) ->",
                options=list(range(1, 128)),
                index=0,  
                key="func1_select"
            )
            selected_functions.append(func1_select)
        with col_f1_header[1]:
            st.write(f"F{func1_select}(x)")
        
        col_f1 = st.columns(4)
        with col_f1[0]:
            a1 = st.number_input("a", value=1.0, key="f1_a")
        with col_f1[1]:
            b1 = st.number_input("b", value=1.0, key="f1_b")
        with col_f1[2]:
            c1 = st.number_input("c", value=1.0, key="f1_c")
        with col_f1[3]:
            d1 = st.number_input("d", value=1.0, key="f1_d")
        free_members.append([a1, b1, c1, d1])
        
        # Function 2 - линейная (ax + b)
        st.subheader("F(x) = ax + b")
        col_f2_header = st.columns([1, 3])
        with col_f2_header[0]:
            func2_select = st.selectbox(
                "F(x) →", 
                options=list(range(1, 128)),
                index=1,  
                key="func2_select"
            )
            selected_functions.append(func2_select)
        with col_f2_header[1]:
            st.write(f"F{func2_select}(x)")
            
        col_f2 = st.columns(2)
        with col_f2[0]:
            a2 = st.number_input("a", value=1.0, key="f2_a")
        with col_f2[1]:
            b2 = st.number_input("b", value=1.0, key="f2_b")
        free_members.append([a2, b2])
        
        # Function 3 - квадратичная (ax² + bx + c)
        st.subheader("F(x) = ax² + bx + c")
        col_f3_header = st.columns([1, 3])
        with col_f3_header[0]:
            func3_select = st.selectbox(
                "F(x) →",
                options=list(range(1, 128)), 
                index=2, 
                key="func3_select"
            )
            selected_functions.append(func3_select)
        with col_f3_header[1]:
            st.write(f"F{func3_select}(x)")
            
        col_f3 = st.columns(3)
        with col_f3[0]:
            a3 = st.number_input("a", value=1.0, key="f3_a")
        with col_f3[1]:
            b3 = st.number_input("b", value=1.0, key="f3_b")
        with col_f3[2]:
            c3 = st.number_input("c", value=1.0, key="f3_c")
        free_members.append([a3, b3, c3])
        
        # Function 4 - линейная (ax + b)
        st.subheader("F(x) = ax + b")
        col_f4_header = st.columns([1, 3])
        with col_f4_header[0]:
            func4_select = st.selectbox(
                "F(x) →",
                options=list(range(1, 128)),
                index=3,  
                key="func4_select"
            )
            selected_functions.append(func4_select)
        with col_f4_header[1]:
            st.write(f"F{func4_select}(x)")
            
        col_f4 = st.columns(2)
        with col_f4[0]:
            a4 = st.number_input("a", value=1.0, key="f4_a")
        with col_f4[1]:
            b4 = st.number_input("b", value=1.0, key="f4_b")
        free_members.append([a4, b4])
        
        # Function 5 - квадратичная (ax² + bx + c)
        st.subheader("F(x) = ax² + bx + c")
        col_f5_header = st.columns([1, 3])
        with col_f5_header[0]:
            func5_select = st.selectbox(
                "F(x) →",
                options=list(range(1, 128)),
                index=4,
                key="func5_select"
            )
            selected_functions.append(func5_select)
        with col_f5_header[1]:
            st.write(f"F{func5_select}(x)")
            
        col_f5 = st.columns(3)
        with col_f5[0]:
            a5 = st.number_input("a", value=1.0, key="f5_a")
        with col_f5[1]:
            b5 = st.number_input("b", value=1.0, key="f5_b")
        with col_f5[2]:
            c5 = st.number_input("c", value=1.0, key="f5_c")
        free_members.append([a5, b5, c5])
        
        # Function 6 - линейная (ax + b)
        st.subheader("F(x) = ax + b")
        col_f6_header = st.columns([1, 3])
        with col_f6_header[0]:
            func6_select = st.selectbox(
                "F(x) →",
                options=list(range(1, 128)),
                index=5, 
                key="func6_select"
            )
            selected_functions.append(func6_select)
        with col_f6_header[1]:
            st.write(f"F{func6_select}(x)")
            
        col_f6 = st.columns(2)
        with col_f6[0]:
            a6 = st.number_input("a", value=1.0, key="f6_a")
        with col_f6[1]:
            b6 = st.number_input("b", value=1.0, key="f6_b")
        free_members.append([a6, b6])
        
        # Function 7 - квадратичная (ax² + bx + c)
        st.subheader("F(x) = ax² + bx + c")
        col_f7_header = st.columns([1, 3])
        with col_f7_header[0]:
            func7_select = st.selectbox(
                "F(x) →",
                options=list(range(1, 128)),
                index=6, 
                key="func7_select"
            )
            selected_functions.append(func7_select)
        with col_f7_header[1]:
            st.write(f"F{func7_select}(x)")
            
        col_f7 = st.columns(3)
        with col_f7[0]:
            a7 = st.number_input("a", value=1.0, key="f7_a")
        with col_f7[1]:
            b7 = st.number_input("b", value=1.0, key="f7_b")
        with col_f7[2]:
            c7 = st.number_input("c", value=1.0, key="f7_c")
        free_members.append([a7, b7, c7])
        
        # Групка "Управление"
        st.header("Управление")
        
        # Статус
        status_placeholder = st.empty()
        status_placeholder.text("Статус: Ожидание вычислений")
        
        # Кнопки управления
        if st.button("Вычислить", use_container_width=True):
            with st.spinner("Выполняется расчет..."):
                try:
                    # Устанавливаем параметры
                    process.free_members_of_fun_expr = free_members
                    
                    # Инициализация функций через комбобоксы (как в десктопной версии)
                    process.dict_of_function_expressions.clear()
                    
                    # Применяем выбранные функции через activatedCombox логику
                    process.activatedCombox(0, str(func1_select))
                    process.activatedCombox(1, str(func2_select)) 
                    process.activatedCombox(2, str(func3_select))
                    process.activatedCombox(3, str(func4_select))
                    process.activatedCombox(4, str(func5_select))
                    process.activatedCombox(5, str(func6_select))
                    process.activatedCombox(6, str(func7_select))
                    
                   
                    # Время моделирования
                    t = np.linspace(0, 1, 80)
                    
                    # Выполняем расчет
                    t, data_sol = process.process_calculation(start_values, free_members)
                    
                    # Сохраняем результаты
                    st.session_state.data_sol = data_sol
                    st.session_state.t = t
                    st.session_state.free_members = free_members
                    st.session_state.calculation_done = True
                    st.session_state.selected_functions = selected_functions
                    
                    status_placeholder.text("Статус: Успешно")
                    st.success("Моделирование завершено успешно!")
                    
                except Exception as e:
                    status_placeholder.text("Статус: Ошибка")
                    st.error(f"Ошибка при вычислении: {str(e)}")      
with tab2:
    st.header("Графики характеристик")
    
    if st.session_state.calculation_done and st.session_state.data_sol is not None:
        # Создаем основной график динамики характеристик
        fig = process.create_graphic(st.session_state.t, st.session_state.data_sol)
        st.pyplot(fig)
        
        # Кнопка для обновления графика
        if st.button("Обновить график"):
            st.rerun()
    else:
        st.info("Выполните вычисления на вкладке 'Параметры' чтобы увидеть графики")

with tab3:
    st.header("Радар-диаграммы")
    
    if st.session_state.calculation_done and st.session_state.data_sol is not None:
        # # Добавляем информацию о данных для отладки
        # with st.expander("Информация о данных (для отладки)"):
        #     st.write(f"Размер данных: {st.session_state.data_sol.shape}")
        #     st.write(f"Диапазон значений: {np.min(st.session_state.data_sol):.3f} - {np.max(st.session_state.data_sol):.3f}")
        #     st.write("Первые 5 значений начального момента:")
        #     st.write(st.session_state.data_sol[0][:5])
        #     st.write("Первые 5 значений конечного момента:")
        #     st.write(st.session_state.data_sol[-1][:5])
        
        # Создаем диаграммы
        diagrams = process.create_radar_diagrams(
            st.session_state.data_sol, 
            process.labels_array()
        )
        
        # Отображаем диаграммы
        for fig, title in diagrams:
            st.subheader(title)
            st.pyplot(fig)
            
        # Кнопка для принудительного обновления
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Обновить диаграммы", use_container_width=True):
                st.rerun()
                
    else:
        st.info("Выполните вычисления на вкладке 'Параметры' чтобы увидеть диаграммы")

with tab4:
    st.header("Графики возмущений")
    
    if st.session_state.calculation_done and st.session_state.free_members is not None:
        # Создаем график возмущений
        t = st.session_state.t
        fig = process.draw_third_graphic(t)
        st.pyplot(fig)
        
        # Кнопка для обновления графика возмущений
        if st.button("Обновить график возмущений"):
            st.rerun()
    else:
        st.info("Выполните вычисления на вкладке 'Параметры' чтобы увидеть графики возмущений")

# Информация внизу
st.markdown("---")
st.write("Модель ISO для анализа качества программного обеспечения")
