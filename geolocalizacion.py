import streamlit as st
import pandas as pd

BASE_NORMATIVA = {
    "Campeche": {
        "norma": "Reglamento de Construcciones del Estado de Campeche / NTC",
        "municipios": {
            "Campeche (Capital)": {
                "zona": "B1",
                "c": 0.12,
                "viento": 160,
                "desc": "Zona costera con sismicidad baja-moderada e impacto de vientos huracanados."
            },
            "Carmen (Ciudad del Carmen)": {
                "zona": "B2",
                "c": 0.14,
                "viento": 180,
                "desc": "Alta exposición a vientos francos del Golfo de México e influencia marina."
            },
            "Champotón": {
                "zona": "B1",
                "c": 0.12,
                "viento": 160,
                "desc": "Zona costera con vientos de diseño regionales según MDOC-CFE."
            },
            "Escárcega": {
                "zona": "A",
                "c": 0.08,
                "viento": 140,
                "desc": "Zona continental interior de Campeche, sismicidad baja."
            },
            "Calakmul": {
                "zona": "A",
                "c": 0.08,
                "viento": 130,
                "desc": "Zona continental de baja sismicidad y vientos moderados."
            }
        }
    },
    "Ciudad de México (CDMX)": {
        "norma": "Normas Técnicas Complementarias NTC-CDMX 2023",
        "municipios": {
            "Alcaldía Cuauhtémoc (Zona III Lago)": {
                "zona": "III (Lago)",
                "c": 0.45,
                "viento": 75,
                "desc": "Arcillas blandas de alta compresibilidad. Alta amplificación sísmica."
            },
            "Alcaldía Coyoacán (Zona II Transición)": {
                "zona": "II (Transición)",
                "c": 0.32,
                "viento": 75,
                "desc": "Intercalación de estratos arcillosos y depósitos firmes."
            },
            "Alcaldía Tlalpan (Zona I Lomas)": {
                "zona": "I (Lomas)",
                "c": 0.16,
                "viento": 75,
                "desc": "Terreno firme de roca o tepetate con baja amplificación sísmica."
            }
        }
    },
    "Jalisco": {
        "norma": "Reglamento Estatal de Jalisco / ACI 318",
        "municipios": {
            "Guadalajara": {
                "zona": "C",
                "c": 0.30,
                "viento": 120,
                "desc": "Zona de sismicidad alta por subducción del Pacífico."
            },
            "Puerto Vallarta": {
                "zona": "D",
                "c": 0.40,
                "viento": 190,
                "desc": "Zona costera de muy alta sismicidad y exposición a huracanes."
            }
        }
    },
    "Nuevo León": {
        "norma": "Reglamento de Construcción de Monterrey / MDOC-CFE",
        "municipios": {
            "Monterrey": {
                "zona": "A",
                "c": 0.06,
                "viento": 130,
                "desc": "Sismicidad muy baja, diseño dominado por ráfagas de viento."
            },
            "San Pedro Garza García": {
                "zona": "A",
                "c": 0.06,
                "viento": 130,
                "desc": "Zona sísmica baja con requerimientos de viento en laderas."
            }
        }
    },
    "Yucatán": {
        "norma": "Reglamento de Construcciones de Mérida / MDOC-CFE",
        "municipios": {
            "Mérida": {
                "zona": "A",
                "c": 0.05,
                "viento": 160,
                "desc": "Baja sismicidad, dominada por efectos de viento huracanado."
            },
            "Progreso": {
                "zona": "A",
                "c": 0.05,
                "viento": 190,
                "desc": "Exposición costera directa a ráfagas de viento huracanado."
            }
        }
    },
    "Oaxaca": {
        "norma": "Reglamento de Construcciones para Oaxaca / NTC",
        "municipios": {
            "Oaxaca de Juárez": {
                "zona": "D",
                "c": 0.48,
                "viento": 110,
                "desc": "Zona de altísima sismicidad debido a la brecha de subducción."
            },
            "Salina Cruz": {
                "zona": "D",
                "c": 0.50,
                "viento": 180,
                "desc": "Combinación de altísima sismicidad y vientos dominantes del Istmo."
            }
        }
    },
    "Veracruz": {
        "norma": "Reglamento del Estado de Veracruz / CFE",
        "municipios": {
            "Veracruz (Puerto)": {
                "zona": "B",
                "c": 0.18,
                "viento": 180,
                "desc": "Zona expuesta a vientos del Norte e impacto de tormentas."
            },
            "Xalapa": {
                "zona": "B",
                "c": 0.16,
                "viento": 140,
                "desc": "Zona montañosa de sismicidad moderada."
            }
        }
    }
}

def mostrar_geolocalizacion():
    st.header("Geolocalización, Zonificación y Normativa Regional")
    st.write(
        "Seleccione el estado y municipio de la República Mexicana para obtener la norma "
        "aplicable y parámetros sísmicos y de viento."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        estado_sel = st.selectbox("Estado / Entidad Federativa", list(BASE_NORMATIVA.keys()))
    with c2:
        municipios_list = list(BASE_NORMATIVA[estado_sel]["municipios"].keys())
        mun_sel = st.selectbox("Municipio / Alcaldía", municipios_list)
    with c3:
        uso_edif = st.selectbox(
            "Uso de Edificación",
            [
                "Grupo B: Habitacional / Comercial",
                "Grupo A: Estructura Esencial (Hospitales, Escuelas)"
            ]
        )

    data_mun = BASE_NORMATIVA[estado_sel]["municipios"][mun_sel]
    norma_nom = BASE_NORMATIVA[estado_sel]["norma"]
    factor_imp = 1.5 if "Grupo A" in uso_edif else 1.0
    c_diseno = round(data_mun["c"] * factor_imp, 3)

    st.subheader("Parámetros Locales Detectados")
    mc1, mc2, mc3, mc4 = st.columns(4)
    mc1.metric("Norma Aplicable", norma_nom.split('/')[0])
    mc2.metric("Coeficiente Sísmico (c)", f"{c_diseno}")
    mc3.metric("Velocidad de Viento (V_r)", f"{data_mun['viento']} km/h")
    mc4.metric("Factor Grupo (Uso)", f"F_imp = {factor_imp}")

    st.success(f"**Criterio Técnico:** {data_mun['desc']}")

    st.markdown("---")
    st.subheader("Pesos Volumétricos Normativos (γ)")
    df_pesos = pd.DataFrame({
        "Material": [
            "Concreto Armado",
            "Concreto Simple",
            "Tabique Rojo Macizo",
            "Bloque Hueco de Concreto",
            "Mortero Cemento-Arena",
            "Acero Estructural"
        ],
        "Peso Volumétrico (kg/m³)": [2400, 2200, 1500, 1200, 2100, 7850],
        "Peso Volumétrico (kN/m³)": [23.54, 21.58, 14.71, 11.77, 20.60, 77.00]
    })
    st.dataframe(df_pesos, use_container_width=True)