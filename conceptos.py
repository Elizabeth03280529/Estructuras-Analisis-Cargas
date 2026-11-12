import streamlit as st

CONCEPTOS_GLOSARIO = [
    (
        "Estructura",
        "Ensamblaje de elementos interconectados diseñado para soportar y transmitir "
        "cargas con seguridad hacia las cimentaciones y el terreno."
    ),
    (
        "Carga Estructural",
        "Fuerzas, pesos o acciones externas e internas actuantes sobre la edificación "
        "(permanentes, variables o accidentales)."
    ),
    (
        "Elementos Estructurales",
        "Componentes físicos como vigas, columnas, muros, losas y zapatas que absorben "
        "y canalizan las fuerzas del sistema."
    ),
    (
        "Transmisión de Cargas",
        "Camino o trayectoria continua que recorre el peso desde la losa hacia las vigas, "
        "columnas, muros y finalmente la cimentación."
    ),
    (
        "Deformación",
        "Cambio de forma o tamaño que experimenta un cuerpo debido a la acción de cargas "
        "externas o efectos térmicos."
    ),
    (
        "Esfuerzo",
        "Intensidad de la fuerza interna por unidad de área producida por las cargas "
        "aplicadas (σ = P/A, τ = V/A)."
    ),
    (
        "Tipos de Cargas Estructurales",
        "Clasificación general según su permanencia (Cargas Muertas, Cargas Vivas) y su "
        "origen (Accidentales como Sismo o Viento)."
    ),
    (
        "Carga Concentrada",
        "Fuerza cuya área de aplicación es tan pequeña que numéricamente se idealiza "
        "como un punto (fuerza puntual P)."
    ),
    (
        "Carga Distribuida",
        "Carga continua repartida uniformemente o de forma variable sobre una longitud "
        "(kg/m) o una superficie (kg/m²)."
    ),
    (
        "Flexión",
        "Efecto estructural generado por momentos flectores que induce tracción en una "
        "cara del elemento y compresión en la cara opuesta."
    ),
    (
        "Compresión",
        "Esfuerzo interno axial que tiende a acortar y aplastar un elemento "
        "longitudinalmente a lo largo de su eje principal."
    ),
    (
        "Tensión / Tracción",
        "Esfuerzo interno axial que tiende a estirar y alargar la longitud de un "
        "elemento estructural."
    ),
    (
        "Cortante",
        "Fuerza transversal que intenta cizallar o deslizar una sección de la estructura "
        "con respecto a la sección adyacente."
    ),
    (
        "Torsión",
        "Momento o esfuerzo que tiende a retorcer un elemento alrededor de su eje "
        "longitudinal."
    ),
    (
        "Capacidad de Carga",
        "Magnitud máxima de carga que un elemento o suelo soporta antes de alcanzar un "
        "estado límite de falla o deformación."
    ),
    (
        "Factor de Seguridad",
        "Relación o coeficiente numérico entre la resistencia real del elemento y la "
        "carga de servicio máxima esperada."
    )
]

def mostrar_conceptos():
    st.header("Conceptos Básicos de Análisis Estructural")
    st.caption("Glosario completo con las 16 definiciones fundamentales del análisis de cargas.")

    cols = st.columns(2)
    for idx, (titulo, desc) in enumerate(CONCEPTOS_GLOSARIO):
        with cols[idx % 2]:
            st.markdown(f"""
                <div style="background-color: white; padding: 1rem; border-radius: 0.5rem;
                            border: 1px solid #e2e8f0; margin-bottom: 0.75rem;">
                    <h4 style="margin: 0; color: #0284c7; font-size: 0.95rem;">
                        🔹 {idx + 1}. {titulo}
                    </h4>
                    <p style="margin-top: 0.4rem; margin-bottom: 0; color: #475569;
                              font-size: 0.85rem; line-height: 1.4;">
                        {desc}
                    </p>
                </div>
            """, unsafe_allow_html=True)