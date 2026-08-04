import streamlit as st
import pandas as pd

# 1. Configuración principal de la página web
st.set_page_config(page_title="Plataforma de Auditoría", layout="wide")

st.title("Sistema Automatizado de Evaluación")
st.write("Bienvenido al panel de control. Selecciona la campaña para iniciar la auditoría.")

# 2. Menú lateral (Sidebar) para navegación
campaña = st.sidebar.selectbox(
    "Selecciona la Campaña a evaluar:",
    ("Anulaciones", "Término de Descuento", "Blindaje")
)

st.sidebar.markdown("---")
st.sidebar.write("Usuario Activo: Monitor Principal")

st.subheader(f"Módulo de Evaluación: {campaña}")

# 3. Interfaz dinámica dependiendo de la campaña seleccionada
if campaña in ["Anulaciones", "Término de Descuento"]:
    st.write("Sube la grabación de la llamada para iniciar la transcripción y el análisis.")
    archivo_audio = st.file_uploader("Selecciona un archivo de audio (MP3/WAV)", type=["mp3", "wav"])
    
    if archivo_audio is not None:
        st.success("¡Audio cargado correctamente!")
        st.button("Analizar con IA")
        # Aquí conectaremos Whisper (para texto) y el LLM (para la pauta) más adelante

elif campaña == "Blindaje":
    st.write("Ingresa el historial del chat para procesar la evaluación.")
    texto_chat = st.text_area("Pega el texto del chat aquí:", height=200)
    
    if st.button("Evaluar Chat"):
        if texto_chat:
            st.success("Chat procesado correctamente.")
            # Aquí conectaremos el LLM directamente con tu matriz de calidad
        else:
            st.warning("Por favor, ingresa el texto del chat antes de evaluar.")

# 4. Sección de Base de Datos y Exportación (Simulada por ahora)
st.markdown("---")
st.subheader("Base de Datos Reciente")
st.write("Aquí se mostrará la tabla con los resultados para luego exportarla.")

if st.button("Exportar resultados a Excel"):
    st.info("La función de exportación a .xlsx estará disponible pronto.")