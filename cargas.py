import streamlit as st
import matplotlib.pyplot as plt

def mostrar_cargas_basicas():
    st.header("Cargas Estructurales Básicas")

    col_in, col_out = st.columns([1, 1.2])

    with col_in:
        st.subheader("Datos de Entrada")
        cm = st.number_input("Carga Muerta (CM) [kg/m²]", min_value=0.1, value=250.0, step=10.0)
        cv = st.number_input("Carga Viva (CV) [kg/m²]", min_value=0.1, value=170.0, step=10.0)
        L = st.number_input("Longitud Tributaria / Claro (L) [m]", min_value=0.1, value=6.0, step=0.5)

    ct = cm + cv
    w = ct * L
    p_total = w * L
    p_kn = (p_total * 9.81) / 1000

    with col_out:
        st.subheader("Resultados Principales")
        r1, r2, r3 = st.columns(3)
        r1.metric("Carga Total (CT)", f"{ct:.1f} kg/m²")
        r2.metric("Carga Lineal (w)", f"{w:.1f} kg/m")
        r3.metric("Puntual Eq. (P)", f"{p_kn:.2f} kN")

        st.subheader("Procedimiento Detallado Paso a Paso")
        st.markdown(f"""
        <div class="calc-step">
            <strong>1. Carga Total por Metro Cuadrado (CT):</strong><br>
            <span class="calc-formula">CT = CM + CV</span><br>
            Sustitución: CT = {cm} kg/m² + {cv} kg/m² = <strong>{ct:.1f} kg/m²</strong>
        </div>
        <div class="calc-step">
            <strong>2. Carga Distribuida Lineal (w):</strong><br>
            <span class="calc-formula">w = CT × L</span><br>
            Sustitución: w = {ct:.1f} kg/m² × {L} m = <strong>{w:.1f} kg/m</strong>
        </div>
        <div class="calc-step">
            <strong>3. Carga Puntual Resultante Equivalente (P):</strong><br>
            <span class="calc-formula">P = w × L</span><br>
            Sustitución: P = {w:.1f} kg/m × {L} m = {p_total:.1f} kg ≈ <strong>{p_kn:.2f} kN</strong>
        </div>
        """, unsafe_allow_html=True)

def mostrar_cargas_m2():
    st.header("Análisis de Cargas Unitario por Metro Cuadrado (w/m²)")

    col_in, col_chart = st.columns([1, 1.2])

    with col_in:
        st.subheader("Componentes de la Losa")
        h_cm = st.number_input("Espesor de losa de concreto [cm]", value=12.0, step=1.0)
        firme = st.number_input("Firme y mortero de nivelación [kg/m²]", value=40.0, step=5.0)
        acabado = st.number_input("Acabados (Piso / Plafón) [kg/m²]", value=35.0, step=5.0)
        instalaciones = st.number_input("Instalaciones hidro-sanitarias y eléctricas [kg/m²]", value=15.0, step=5.0)
        cv_reg = st.number_input("Carga Viva Reglamentaria (CV) [kg/m²]", value=170.0, step=10.0)

    peso_losa = (h_cm / 100.0) * 2400
    cm_tot = peso_losa + firme + acabado + instalaciones
    w_tot_m2 = cm_tot + cv_reg

    with col_chart:
        st.subheader("Desglose Porcentual")
        st.metric("CARGA TOTAL RESULTANTE", f"{w_tot_m2:.1f} kg/m²")

        labels = ['Losa Concreto', 'Firme Mortero', 'Acabados', 'Instalaciones', 'Carga Viva']
        sizes = [peso_losa, firme, acabado, instalaciones, cv_reg]
        colors = ['#0369a1', '#0284c7', '#38bdf8', '#bae6fd', '#f59e0b']

        fig, ax = plt.subplots(figsize=(5, 3.8))
        ax.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=140,
            wedgeprops=dict(width=0.4)
        )
        st.pyplot(fig)

def mostrar_combinaciones():
    st.header("Combinación de Cargas Factorizadas (LRFD / NTC)")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Factores de Carga")
        f_cm = st.number_input("Factor Carga Muerta (γ_D)", value=1.3, step=0.1)
        f_cv = st.number_input("Factor Carga Viva (γ_L)", value=1.5, step=0.1)

        st.subheader("Cargas Nominales de Servicio")
        cm_val = st.number_input("Carga Muerta Nominal (CM) [kg/m²]", value=378.0)
        cv_val = st.number_input("Carga Viva Nominal (CV) [kg/m²]", value=170.0)

    qu = (f_cm * cm_val) + (f_cv * cv_val)
    qu_kn = qu * 0.00981

    with col2:
        st.subheader("Resultado de Carga Factorizada")
        st.markdown(f"""
        <div style="background-color: #0f172a; color: #38bdf8; padding: 1.5rem;
                    border-radius: 0.75rem; text-align: center;">
            <div style="font-size: 0.85rem; color: #94a3b8;">
                COMBINACIÓN GRAVITACIONAL ÚLTIMA
            </div>
            <div style="font-size: 2.1rem; font-weight: 800; margin: 0.5rem 0;">
                Qu = {qu:.1f} kg/m²
            </div>
            <div style="font-size: 1.05rem; color: #7dd3fc;">
                {qu_kn:.2f} kN/m²
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="calc-step" style="margin-top: 1rem;">
            <strong>Fórmula Utilizada:</strong><br>
            <span class="calc-formula">Qu = γ_D · CM + γ_L · CV</span><br><br>
            <strong>Sustitución de Valores:</strong><br>
            Qu = ({f_cm} × {cm_val} kg/m²) + ({f_cv} × {cv_val} kg/m²)<br>
            Qu = {f_cm * cm_val:.1f} + {f_cv * cv_val:.1f} = <strong>{qu:.1f} kg/m²</strong>
        </div>
        """, unsafe_allow_html=True)

def mostrar_ejercicios():
    st.header("Ejercicios Resueltos de Análisis de Cargas")

    ex_sel = st.selectbox(
        "Seleccione Ejercicio a Revisar:",
        [
            "Ejercicio 1: Muro de Mampostería Completo",
            "Ejercicio 2: Carga en Losa Maciza",
            "Ejercicio 3: Carga Total en Viga Principal"
        ]
    )

    if "Ejercicio 1" in ex_sel:
        st.subheader("Ejercicio 1: Muro de Mampostería de 2 Niveles")
        st.write(
            "**Planteamiento:** Calcular el peso propio total de un muro de tabique rojo macizo "
            "(γ = 1500 kg/m³) de 5.0 m de longitud, 2.7 m de altura libre por nivel y 0.15 m de "
            "espesor en 2 niveles."
        )

        st.code("""
1. Área Frontal:
   A = 5.0 m × 2.7 m = 13.50 m²

2. Volumen de Mampostería:
   V = 13.50 m² × 0.15 m = 2.025 m³

3. Peso Propio por Nivel:
   W_1 = 2.025 m³ × 1500 kg/m³ = 3,037.5 kg

4. Carga Muerta Total (2 Niveles):
   W_tot = 3,037.5 kg × 2 = 6,075.0 kg (59.60 kN)
        """, language="markdown")

    elif "Ejercicio 2" in ex_sel:
        st.subheader("Ejercicio 2: Carga Unitario en Losa de Concreto Armado")
        st.write(
            "**Planteamiento:** Determinar la carga total de servicio por m² para una losa de "
            "12 cm de espesor con acabados de 35 kg/m², firme de 40 kg/m² e instalaciones de "
            "15 kg/m² para uso habitacional (CV = 170 kg/m²)."
        )

        st.code("""
1. Peso Propio Losa de Concreto:
   CM_losa = 0.12 m × 2400 kg/m³ = 288.0 kg/m²

2. Carga Muerta Total (CM):
   CM = 288.0 (Losa) + 40 (Firme) + 35 (Acabados) + 15 (Instalaciones) = 378.0 kg/m²

3. Carga Total de Servicio (CT):
   CT = CM + CV = 378.0 kg/m² + 170.0 kg/m² = 548.0 kg/m² (5.38 kN/m²)
        """, language="markdown")

    else:
        st.subheader("Ejercicio 3: Carga Total Distribuida en Viga Principal")
        st.write(
            "**Planteamiento:** Una viga de 25×50 cm soporta una carga viva de 300 kg/m sobre "
            "un claro de 6.0 metros. Se requiere calcular la carga uniformemente distribuida total (w)."
        )

        st.code("""
1. Peso Propio Viga de Concreto:
   CM_viga = 0.25 m × 0.50 m × 2400 kg/m³ = 300.0 kg/m

2. Carga Total Distribuida (w):
   w = CM + CV = 300.0 kg/m + 300.0 kg/m = 600.0 kg/m

3. Carga Puntual Equivalente (P):
   P = w × L = 600.0 kg/m × 6.0 m = 3,600.0 kg (35.32 kN)
        """, language="markdown")