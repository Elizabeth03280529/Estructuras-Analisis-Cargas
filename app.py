import os
import streamlit as st
from conceptos import mostrar_conceptos
from geolocalizacion import mostrar_geolocalizacion
from cargas import (
    mostrar_cargas_basicas,
    mostrar_cargas_m2,
    mostrar_combinaciones,
    mostrar_ejercicios
)
from modelos_3d import mostrar_muros_3d, mostrar_elementos

# ==============================================================================
# 1. CONFIGURACIÓN INICIAL Y ESTILOS VISUALES DE LA APLICACIÓN
# ==============================================================================
st.set_page_config(
    page_title="ESTRUCTURAS | Análisis de Cargas",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0284c7 100%);
        color: white;
        padding: 2.2rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        margin: 0;
        color: #ffffff;
        letter-spacing: -0.025em;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        color: #7dd3fc;
        font-weight: 600;
        margin-top: 0.2rem;
        margin-bottom: 0.8rem;
    }
    .calc-step {
        background-color: #ffffff;
        border-left: 4px solid #0284c7;
        padding: 1rem;
        margin-bottom: 0.75rem;
        border-radius: 0 0.5rem 0.5rem 0;
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
    }
    .calc-formula {
        font-family: 'Courier New', Courier, monospace;
        color: #0369a1;
        font-weight: 700;
        background-color: #e0f2fe;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        display: inline-block;
        margin: 0.35rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. BARRA LATERAL (NAVEGACIÓN DE LA APLICACIÓN)
# ==============================================================================
st.sidebar.markdown("### Navegación Principal")
menu_opcion = st.sidebar.radio(
    "Ir al módulo:",
    [
        "📌 Inicio & Presentación",
        "📚 Conceptos Básicos",
        "🌐 Geolocalización y Normativa",
        "🧮 Cargas Estructurales Básicas",
        "🧱 Muros de Mampostería (3D)",
        "📦 Vigas, Columnas y Losas",
        "📐 Cargas por Metro Cuadrado (m²)",
        "🔀 Combinación de Cargas",
        "✍️ Ejercicios Resueltos"
    ]
)

st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">ESTRUCTURAS | Análisis de Cargas</h1>
        <div class="hero-subtitle">Ingeniería Civil</div>
        <p style="margin: 0; color: #e0f2fe; font-size: 0.95rem;">
            Plataforma Profesional de Cálculo, Simulación e Interpretación Estructural
        </p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. ENRUTAMIENTO DE MÓDULOS
# ==============================================================================
if menu_opcion == "📌 Inicio & Presentación":
    st.header("Importancia del Análisis de Cargas Estructurales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.write("""
        Toda construcción está sometida a diferentes tipos de cargas, como el peso de sus propios materiales,
        las personas, los muebles, los equipos y las acciones ambientales, entre ellas el viento y los sismos.
        Estas fuerzas pueden afectar el comportamiento de una estructura y, si no se consideran adecuadamente
        durante su diseño, pueden provocar deformaciones excesivas, daños o fallas estructurales.

        Por esta razón, es necesario realizar un análisis que permita identificar las cargas, calcular sus
        magnitudes, establecer sus combinaciones y evaluar sus efectos sobre los elementos que conforman una
        edificación.

        Esta investigación tiene como finalidad explicar los fundamentos del análisis de cargas estructurales,
        identificar los datos necesarios para realizarlo y establecer los procedimientos que podrían incorporarse
        en una aplicación web destinada a facilitar estos cálculos.
        """)

        st.info(
            "💡 **Sistema Interactivo:** Seleccione cualquiera de los módulos en el menú lateral "
            "para realizar cálculos dinámicos con desgloses matemáticos explicados paso a paso."
        )

    with col2:
        ruta_img = next(
            (p for p in ["imagenes/portada.jpg", "imagenes/portada.png", "imagenes/portada.jpeg"] if os.path.exists(p)),
            None
        )
        if ruta_img:
            st.image(
                ruta_img,
                caption="Estructura de Edificación - Análisis y Diseño",
                use_container_width=True
            )
        else:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #1e293b 0%, #0369a1 100%);
                            color: white; padding: 2rem; border-radius: 0.75rem;
                            text-align: center; border: 1px solid #0284c7;">
                    <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">🏗️</div>
                    <h3 style="margin: 0; color: #ffffff;">Análisis Estructural</h3>
                    <p style="color: #bae6fd; font-size: 0.9rem; margin-top: 0.5rem;">
                        Cargas Muertas · Cargas Vivas · Sismo y Viento · Combinaciones LRFD / NTC
                    </p>
                </div>
            """, unsafe_allow_html=True)

elif menu_opcion == "📚 Conceptos Básicos":
    mostrar_conceptos()

elif menu_opcion == "🌐 Geolocalización y Normativa":
    mostrar_geolocalizacion()

elif menu_opcion == "🧮 Cargas Estructurales Básicas":
    mostrar_cargas_basicas()

elif menu_opcion == "🧱 Muros de Mampostería (3D)":
    mostrar_muros_3d()

elif menu_opcion == "📦 Vigas, Columnas y Losas":
    mostrar_elementos()

elif menu_opcion == "📐 Cargas por Metro Cuadrado (m²)":
    mostrar_cargas_m2()

elif menu_opcion == "🔀 Combinación de Cargas":
    mostrar_combinaciones()

elif menu_opcion == "✍️ Ejercicios Resueltos":
    mostrar_ejercicios()