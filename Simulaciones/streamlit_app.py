import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats

# Datos
MLD = [923, 963, 689]
MPI = [453, 962, 689]
MLNS = [913, 773, 689]

# Configuración de la página
st.set_page_config(page_title="Análisis Estadístico", layout="wide")
st.title("Análisis Estadístico de Datos")

# Crear un DataFrame con los datos
data = {
    'MLD': MLD,
    'MPI': MPI,
    'MLNS': MLNS
}
df = pd.DataFrame(data)

# Sidebar para selección de métricas
st.sidebar.header("Configuración")
metricas_seleccionadas = st.sidebar.multiselect(
    "Selecciona las métricas a mostrar",
    ["Media", "Rango", "Varianza", "Desviación Estándar", "Mediana"],
    default=["Media", "Rango", "Varianza"]
)

# Mostrar estadísticas básicas
st.header("Estadísticas Básicas")
col1, col2, col3 = st.columns(3)

def mostrar_estadisticas(datos, nombre):
    st.subheader(nombre)
    if "Media" in metricas_seleccionadas:
        st.write(f"Media: {np.mean(datos):.2f}")
    if "Rango" in metricas_seleccionadas:
        st.write(f"Rango: [{np.min(datos)}; {np.max(datos)}]")
    if "Varianza" in metricas_seleccionadas:
        st.write(f"Varianza: {np.var(datos):.2f}")
    if "Desviación Estándar" in metricas_seleccionadas:
        st.write(f"Desviación Estándar: {np.std(datos):.2f}")
    if "Mediana" in metricas_seleccionadas:
        st.write(f"Mediana: {np.median(datos):.2f}")

with col1:
    mostrar_estadisticas(MLD, "MLD")

with col2:
    mostrar_estadisticas(MPI, "MPI")

with col3:
    mostrar_estadisticas(MLNS, "MLNS")

# Tabla de datos
st.header("Tabla de Datos")
st.dataframe(df)

# Visualización de datos
st.header("Visualización de Datos")

# Gráfico de barras mejorado
fig = px.bar(df, title="Comparación de Valores")
fig.update_layout(
    xaxis_title="Métricas",
    yaxis_title="Valores",
    showlegend=True
)
st.plotly_chart(fig, use_container_width=True)

# Gráfico de cajas mejorado
fig_box = px.box(df, title="Distribución de Valores")
fig_box.update_layout(
    xaxis_title="Métricas",
    yaxis_title="Valores",
    showlegend=False
)
st.plotly_chart(fig_box, use_container_width=True)

# Gráfico de dispersión
fig_scatter = px.scatter(df, title="Relación entre Métricas")
fig_scatter.update_layout(
    xaxis_title="MLD",
    yaxis_title="MPI",
    showlegend=True
)
st.plotly_chart(fig_scatter, use_container_width=True)

# Análisis de correlación
st.header("Análisis de Correlación")
corr_matrix = df.corr()
fig_corr = px.imshow(corr_matrix,
                    title="Matriz de Correlación",
                    color_continuous_scale="RdBu")
st.plotly_chart(fig_corr, use_container_width=True)

# Prueba de hipótesis
st.header("Prueba de Hipótesis")
if st.checkbox("Realizar prueba t entre MLD y MPI"):
    t_stat, p_value = stats.ttest_ind(MLD, MPI)
    st.write(f"Estadístico t: {t_stat:.4f}")
    st.write(f"Valor p: {p_value:.4f}")
    st.write(f"Significancia: {'Significativa' if p_value < 0.05 else 'No significativa'}") 