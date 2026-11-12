import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def mostrar_muros_3d():
    st.header("Análisis de Muros de Mampostería")

    col_in, col_out = st.columns([1, 1.2])

    with col_in:
        st.subheader("Geometría del Muro")
        L = st.number_input("Longitud del muro (L) [m]", min_value=0.1, value=5.0, step=0.5)
        H = st.number_input("Altura libre por nivel (H) [m]", min_value=0.1, value=2.7, step=0.1)
        e = st.number_input("Espesor del muro (e) [m]", min_value=0.05, value=0.15, step=0.01)
        niveles = st.number_input("Número de niveles del edificio", min_value=1, value=2, step=1)

        tipo_mamp = st.selectbox(
            "Tipo de Mampostería",
            [
                "Tabique Rojo Macizo (1,500 kg/m³)",
                "Bloque Hueco de Concreto (1,200 kg/m³)",
                "Tabicon Pesado de Concreto (1,800 kg/m³)"
            ]
        )
        pv_val = 1500 if "Rojo" in tipo_mamp else (1200 if "Hueco" in tipo_mamp else 1800)
        fm = st.number_input("Resistencia a compresión f'm [kg/cm²]", min_value=10, value=50, step=5)

    area = L * H
    vol = area * e
    peso_1 = vol * pv_val
    peso_tot = peso_1 * niveles

    with col_out:
        st.subheader("Resultados del Cálculo")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Área", f"{area:.2f} m²")
        m2.metric("Volumen", f"{vol:.3f} m³")
        m3.metric("Peso Nivel 1", f"{peso_1:,.1f} kg")
        m4.metric("Carga Total", f"{peso_tot:,.1f} kg")

        st.subheader("Visor 3D Estructural del Muro")
        fig = go.Figure()

        for n in range(int(niveles)):
            z0 = n * H
            z1 = (n + 1) * H
            x = [0, L, L, 0, 0, L, L, 0]
            y = [0, 0, e, e, 0, 0, e, e]
            z = [z0, z0, z0, z0, z1, z1, z1, z1]

            fig.add_trace(go.Mesh3d(
                x=x,
                y=y,
                z=z,
                i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                opacity=0.85,
                color='#0284c7',
                name=f'Nivel {n + 1}'
            ))

        fig.update_layout(
            scene=dict(
                xaxis_title='Longitud (m)',
                yaxis_title='Espesor (m)',
                zaxis_title='Altura (m)',
                aspectmode='data'
            ),
            margin=dict(l=0, r=0, b=0, t=0),
            height=280
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    <div class="calc-step">
        1. <strong>Área Frontal:</strong> A = L × H = {L} m × {H} m = <strong>{area:.2f} m²</strong><br>
        2. <strong>Volumen de Mampostería:</strong> V = A × e = {area:.2f} m² × {e} m =
           <strong>{vol:.3f} m³</strong><br>
        3. <strong>Peso Propio por Nivel:</strong> W_1 = V × γ = {vol:.3f} m³ × {pv_val} kg/m³ =
           <strong>{peso_1:,.1f} kg</strong><br>
        4. <strong>Carga Muerta Total ({niveles} Niveles):</strong> W_tot = W_1 × {niveles} =
           <strong>{peso_tot:,.1f} kg</strong><br>
        5. <strong>Resistencia nominal f'm ingresada:</strong> {fm} kg/cm²
    </div>
    """, unsafe_allow_html=True)

def mostrar_elementos():
    st.header("Análisis de Elementos Estructurales Individuales")

    elem_tipo = st.radio(
        "Seleccione tipo de elemento:",
        ["Viga de Concreto Armado", "Columna de Concreto", "Losa Maciza"],
        horizontal=True
    )

    if elem_tipo == "Viga de Concreto Armado":
        c1, c2 = st.columns(2)
        with c1:
            b = st.number_input("Base b [m]", value=0.25, step=0.05)
            h = st.number_input("Peralte h [m]", value=0.50, step=0.05)
            L = st.number_input("Claro de Viga L [m]", value=6.0, step=0.5)
            cv_lineal = st.number_input("Carga Viva Lineal [kg/m]", value=300.0, step=50.0)

        peso_propio_viga = b * h * 2400
        w_total = peso_propio_viga + cv_lineal
        M_max = (w_total * (L ** 2)) / 8

        with c2:
            st.metric("Peso Propio (CM)", f"{peso_propio_viga:.1f} kg/m")
            st.metric("Carga Total (w)", f"{w_total:.1f} kg/m")
            st.metric("Momento Máximo (M_max)", f"{M_max:,.1f} kg·m")

            fig, ax = plt.subplots(figsize=(5, 2.2))
            ax.bar(
                ["Carga Muerta", "Carga Viva"],
                [peso_propio_viga, cv_lineal],
                color=["#0284c7", "#7dd3fc"]
            )
            ax.set_ylabel("kg/m")
            st.pyplot(fig)

    elif elem_tipo == "Columna de Concreto":
        c1, c2 = st.columns(2)
        with c1:
            a = st.number_input("Lado A [m]", value=0.40, step=0.05)
            b = st.number_input("Lado B [m]", value=0.40, step=0.05)
            H = st.number_input("Altura Columna H [m]", value=3.5, step=0.5)
            p_trib = st.number_input("Carga Tributaria Superior [kg]", value=12000.0, step=1000.0)

        peso_col = a * b * H * 2400
        p_axial_tot = peso_col + p_trib

        with c2:
            st.metric("Peso Columna (CM)", f"{peso_col:.1f} kg")
            st.metric("Carga Axial Total (P_u)", f"{p_axial_tot:,.1f} kg")

            fig, ax = plt.subplots(figsize=(5, 2.2))
            ax.bar(
                ["Peso Columna", "Carga Tributaria"],
                [peso_col, p_trib],
                color=["#0369a1", "#0284c7"]
            )
            ax.set_ylabel("kg")
            st.pyplot(fig)

    else:
        c1, c2 = st.columns(2)
        with c1:
            e_losa = st.number_input("Espesor de losa [m]", value=0.12, step=0.01)
            lx = st.number_input("Largo Lx [m]", value=4.0, step=0.5)
            ly = st.number_input("Ancho Ly [m]", value=5.0, step=0.5)
            cv_m2 = st.number_input("Carga Viva [kg/m²]", value=170.0, step=10.0)

        cm_losa = e_losa * 2400 + 90
        w_m2 = cm_losa + cv_m2
        peso_total_losa = w_m2 * lx * ly

        with c2:
            st.metric("Carga Muerta (CM)", f"{cm_losa:.1f} kg/m²")
            st.metric("Carga Total (w)", f"{w_m2:.1f} kg/m²")
            st.metric("Peso Tablero Completo", f"{peso_total_losa:,.1f} kg")