import streamlit as st
import pandas as pd

st.set_page_title("Visor de Excel en la Nube")
st.title("📊 Visor de Datos Institucional")
st.write("Contenido de las hojas del archivo Excel:")

# Nombre de tu archivo de Excel tal como lo subiste al repositorio
archivo_excel = "INFORME DE PRODUCCION (RIPRO) v2 1.xlsx"  # Cambia esto si tu archivo tiene otro nombre

try:
    # Lee todas las hojas del archivo Excel en un diccionario de DataFrames
    excel_data = pd.read_excel(archivo_excel, sheet_name=None)
    
    # Obtiene los nombres de las hojas
    nombres_hojas = list(excel_data.keys())
    
    # Crea pestañas interactivas para cada hoja del Excel
    pestanas = st.tabs(nombres_hojas)
    
    for i, nombre_hoja in enumerate(nombres_hojas):
        with pestanas[i]:
            st.subheader(f"Hoja: {nombre_hoja}")
            # Muestra los datos de la hoja en una tabla interactiva
            st.dataframe(excel_data[nombre_hoja], use_container_width=True)

except Exception as e:
    st.error(f"No se pudo cargar el archivo Excel. Asegúrate de que el nombre sea correcto. Detalle: {e}")
