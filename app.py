import streamlit as st
import pandas as pd

# Corrección aquí: se usa st.set_page_config en lugar de st.set_page_title
st.set_page_config(page_title="Visor de Excel en la Nube", layout="wide")
st.title("📊 Visor de Reportes de Producción")

archivo_excel = "INFORME DE PRODUCCION (RIPRO) v2 1.xlsx"

try:
    excel_data = pd.read_excel(archivo_excel, sheet_name=None)
    nombres_hojas = list(excel_data.keys())
    
    pestanas = st.tabs(nombres_hojas)
    
    for i, nombre_hoja in enumerate(nombres_hojas):
        with pestanas[i]:
            st.subheader(f"Hoja: {nombre_hoja}")
            st.dataframe(excel_data[nombre_hoja], use_container_width=True)

except Exception as e:
    st.error(f"Error al cargar el archivo de Excel. Detalle técnico: {e}"
