
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import functions
import process
from radar_diagram import RadarDiagram
from functions import fak_1, fak_2, fak_3, fak_4, fak_5, fak_6

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
  
    st.header("Входные параметры")
    
    start_values = []
    labels = process.labels_array()
    
    # Создаем 28 полей ввода в 3 колонки 
    cols = st.columns(3)
    for i in range(28):
        with cols[i % 3]:
      
            default_value = 0.9 if i == 0 else 0.5
            if i in [27, 26, 25, 24, 22, 23, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
            
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

    st.header("Уравнения")
    
    free_members = []
    selected_functions = []
    

    with st.expander("F(x) = ax³ + bx² + cx + d", expanded=False):
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
            a1 = st.number_input("a", value=0.1, key="f1_a")
        with col_f1[1]:
            b1 = st.number_input("b", value=0.1, key="f1_b")
        with col_f1[2]:
            c1 = st.number_input("c", value=0.1, key="f1_c")
        with col_f1[3]:
            d1 = st.number_input("d", value=0.1, key="f1_d")
        free_members.append([a1, b1, c1, d1])
    
    with st.expander("F(x) = ax + b", expanded=False):
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
            a2 = st.number_input("a", value=0.1, key="f2_a")
        with col_f2[1]:
            b2 = st.number_input("b", value=0.1, key="f2_b")
        free_members.append([a2, b2])
    
    with st.expander("F(x) = ax² + bx + c", expanded=False):
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
            a3 = st.number_input("a", value=0.1, key="f3_a")
        with col_f3[1]:
            b3 = st.number_input("b", value=0.1, key="f3_b")
        with col_f3[2]:
            c3 = st.number_input("c", value=0.1, key="f3_c")
        free_members.append([a3, b3, c3])
    
    with st.expander("F(x) = ax + b", expanded=False):
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
            a4 = st.number_input("a", value=0.1, key="f4_a")
        with col_f4[1]:
            b4 = st.number_input("b", value=0.1, key="f4_b")
        free_members.append([a4, b4])
    
    with st.expander("F(x) = ax² + bx + c", expanded=False):
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
            a5 = st.number_input("a", value=0.1, key="f5_a")
        with col_f5[1]:
            b5 = st.number_input("b", value=0.1, key="f5_b")
        with col_f5[2]:
            c5 = st.number_input("c", value=0.1, key="f5_c")
        free_members.append([a5, b5, c5])
    
    with st.expander("F(x) = ax + b", expanded=False):
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
            a6 = st.number_input("a", value=0.1, key="f6_a")
        with col_f6[1]:
            b6 = st.number_input("b", value=0.1, key="f6_b")
        free_members.append([a6, b6])
    
    with st.expander("F(x) = ax² + bx + c", expanded=False):
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
            a7 = st.number_input("a", value=0.1, key="f7_a")
        with col_f7[1]:
            b7 = st.number_input("b", value=0.1, key="f7_b")
        with col_f7[2]:
            c7 = st.number_input("c", value=0.1, key="f7_c")
        free_members.append([a7, b7, c7])
    
    st.markdown("---")
    

    col_status1, col_status2, col_status3 = st.columns([1, 2, 1])
    with col_status2:
        status_placeholder = st.empty()
        status_placeholder.text("Статус: Ожидание вычислений")
    
    col_calc1, col_calc2, col_calc3 = st.columns([1, 2, 1])
    with col_calc2:
        if st.button("Вычислить", use_container_width=True, key="main_calculate"):
            with st.spinner("Выполняется расчет..."):
                try:
                    # Сохраняем уравнения в сессии
                    st.session_state.free_members = free_members
                    st.session_state.selected_functions = selected_functions
                    
                    # Устанавливаем параметры
                    process.free_members_of_fun_expr = free_members
                    
                    # Инициализация функций через комбобоксы
                    process.dict_of_function_expressions.clear()
                    
                    # Применяем выбранные функции через activatedCombox логику
                    process.activatedCombox(0, str(selected_functions[0]))
                    process.activatedCombox(1, str(selected_functions[1])) 
                    process.activatedCombox(2, str(selected_functions[2]))
                    process.activatedCombox(3, str(selected_functions[3]))
                    process.activatedCombox(4, str(selected_functions[4]))
                    process.activatedCombox(5, str(selected_functions[5]))
                    process.activatedCombox(6, str(selected_functions[6]))
                    
                    # Время моделирования
                    t = np.linspace(0, 1, 80)
                    
                    # Выполняем расчет
                    t, data_sol = process.process_calculation(start_values, free_members)
                    
                    # Сохраняем результаты
                    st.session_state.data_sol = data_sol
                    st.session_state.t = t
                    st.session_state.calculation_done = True
                    
                    status_placeholder.text("Статус: Успешно")
                    st.success("Моделирование завершено успешно!")
                    
                except Exception as e:
                    status_placeholder.text("Статус: Ошибка")
                    st.error(f"Ошибка при вычислении: {str(e)}")

with tab2:
    st.header("График характеристик")
    
    if st.session_state.calculation_done and st.session_state.data_sol is not None:
        if st.button("Построить график"):
            t = st.session_state.t
            data_sol = st.session_state.data_sol
            labels = process.labels_array()
            
            fig, ax = plt.subplots(figsize=(15, 10))
            for i in range(28):
                ax.plot(t, data_sol[:, i], label=labels[i], linewidth=1)
            
            ax.set_xlabel('Время')
            ax.set_ylabel('Значение')
            ax.set_title('Динамика характеристик качества ПО')
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
            ax.grid(True, alpha=0.3)
            ax.set_xlim([0, 1])
            
            st.pyplot(fig)
            # Кнопка скачивания графика
            from io import BytesIO
            buf = BytesIO()
            fig.savefig(buf, format="png", dpi=300, bbox_inches='tight')
            st.download_button(
                label="📥 Скачать график характеристик",
                data=buf.getvalue(),
                file_name="график_характеристик_качества_ПО.png",
                mime="image/png",
                use_container_width=True
            )
    else:
        st.info("Выполните вычисления на вкладке 'Параметры' чтобы увидеть график характеристик")

with tab3:
    st.header("Радар-диаграммы")
    
    if st.session_state.calculation_done and st.session_state.data_sol is not None:
        # Создаем диаграммы
        radar = RadarDiagram()
        diagrams = {}
        data_sol = st.session_state.data_sol
        labels = process.labels_array()
        n = len(data_sol)
        
   
        diagrams['initial'] = radar.draw([data_sol[0]], labels, 
                                       "Характеристики системы в начальный момент времени")
        
        quarter_idx = n // 4
        diagrams['quarter'] = radar.draw([data_sol[0], data_sol[quarter_idx]], labels,
                                       "Характеристики системы в 1 четверти")
        
        half_idx = n // 2
        diagrams['half'] = radar.draw([data_sol[0], data_sol[half_idx]], labels,
                                    "Характеристики системы во 2 четверти")
        
        three_quarter_idx = 3 * n // 4
        diagrams['three_quarters'] = radar.draw([data_sol[0], data_sol[three_quarter_idx]], labels,
                                              "Характеристики системы в 3 четверти")
        
        diagrams['final'] = radar.draw([data_sol[0], data_sol[-1]], labels,
                                     "Характеристики системы в последний момент времени")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Начальный момент")
            st.pyplot(diagrams['initial'])
            
            st.subheader("1/2 времени")
            st.pyplot(diagrams['half'])
            
            st.subheader("Конечный момент")
            st.pyplot(diagrams['final'])
        
        with col2:
            st.subheader("1/4 времени")
            st.pyplot(diagrams['quarter'])
            
            st.subheader("3/4 времени")
            st.pyplot(diagrams['three_quarters'])
            
        st.markdown("---")
        st.subheader("Скачать диаграммы")
        
        download_cols = st.columns(5)
        diagram_names = {
            'initial': 'Начальный момент',
            'quarter': '1/4 времени', 
            'half': '1/2 времени',
            'three_quarters': '3/4 времени',
            'final': 'Конечный момент'
        }
        
        for idx, (key, name) in enumerate(diagram_names.items()):
            with download_cols[idx]:
                from io import BytesIO
                buf = BytesIO()
                diagrams[key].savefig(buf, format="png", dpi=300, bbox_inches='tight')
                st.download_button(
                    label=f"📥 {name}",
                    data=buf.getvalue(),
                    file_name=f"радар_диаграмма_{key}.png",
                    mime="image/png",
                    use_container_width=True
                )
                
                
    else:
        st.info("Выполните вычисления на вкладке 'Параметры' чтобы увидеть диаграммы")
# with tab4:
#     st.header("Графики возмущений")
    
#     if st.session_state.calculation_done and st.session_state.free_members is not None:
#         t = st.session_state.t
#         fig = process.draw_third_graphic(t)
        
#         fig.set_size_inches(10, 6)
#         ax = fig.gca()
     
#         ax.set_xlabel('Время')
#         ax.set_ylabel('Значение')
#         ax.set_title('Временные коэффициенты возмущений')
#         ax.legend()
#         ax.grid(True)
        
#         st.pyplot(fig)
#         from io import BytesIO
#         buf = BytesIO()
#         fig.savefig(buf, format="png", dpi=300, bbox_inches='tight')
#         st.download_button(
#             label="📥 Скачать график возмущений",
#             data=buf.getvalue(),
#             file_name="график_возмущений.png",
#             mime="image/png",
#             use_container_width=True
#         )
        
        
#     else:
#         st.info("Выполните вычисления на вкладке 'Параметры' чтобы увидеть графики возмущений")
with tab4:
    st.header("График возмущений")
   
    t = np.linspace(0, 1, 100)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(t, [fak_1(ti) for ti in t], label='fak_1: t² + 1', linewidth=2)
    ax.plot(t, [fak_2(ti) for ti in t], label='fak_2: cos²(1.5πt - π/6)/4 + 0.2', linewidth=2)
    ax.plot(t, [fak_3(ti) for ti in t], label='fak_3: sin(πt - π/6)/2.5 + 0.3', linewidth=2)
    ax.plot(t, [fak_4(ti) for ti in t], label='fak_4: 2t - 1', linewidth=2)
    ax.plot(t, [fak_5(ti) for ti in t], label='fak_5: cos²(1.5πt - π/6)/4', linewidth=2)
    ax.plot(t, [fak_6(ti) for ti in t], label='fak_6: sin²(πt - π/6)/2.5 + 0.3', linewidth=2)
    
    ax.set_xlabel('Время')
    ax.set_ylabel('Значение')
    ax.set_title('Временные коэффициенты возмущений')
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)
    
    # Кнопка скачивания
    from io import BytesIO
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=300, bbox_inches='tight')
    st.download_button(
        label="📥 Скачать график возмущений",
        data=buf.getvalue(),
        file_name="график_возмущений.png",
        mime="image/png",
        use_container_width=True
    )


st.markdown("---")
st.write("Модель ISO для анализа качества программного обеспечения")