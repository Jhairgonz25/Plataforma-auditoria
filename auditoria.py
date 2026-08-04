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
    
    # Aquí agregamos muchos más formatos aceptados
    archivo_audio = st.file_uploader("Selecciona un archivo de audio", type=["mp3", "wav", "m4a", "ogg", "flac"])
    
    if archivo_audio is not None:
        st.success(f"¡Audio {archivo_audio.name} cargado correctamente!")
        st.button("Analizar con IA")
        # Aquí conectaremos Whisper más adelante

elif campaña == "Blindaje":
    st.write("Sube el historial del chat en formato PDF para procesar la evaluación.")
    
    # Cambiamos el cuadro de texto por un cargador de archivos PDF
    archivo_pdf = st.file_uploader("Selecciona el archivo PDF del chat", type=["pdf"])
    
    if archivo_pdf is not None:
        st.success(f"¡PDF {archivo_pdf.name} cargado correctamente!")
        if st.button("Evaluar Chat"):
            st.info("Procesando lectura del PDF...")
            # Aquí conectaremos la librería para leer el PDF y el LLM

# 4. Sección de Base de Datos y Exportación (Simulada por ahora)
st.markdown("---")
st.subheader("Base de Datos Reciente")
st.write("Aquí se mostrará la tabla con los resultados para luego exportarla.")

if st.button("Exportar resultados a Excel"):
    st.info("La función de exportación a .xlsx estará disponible pronto.")
