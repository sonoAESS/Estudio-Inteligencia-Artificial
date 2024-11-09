import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from io import StringIO 

def main():
    st.title("Análisis descriptivo del Dataset mpg de Seaborn")
    st.write("## Autor: Antonio Elias")
    st.write('## BDFC 301')
    
    # Descripción de las librerías
    st.write("### El primer paso es importar las librerías necesarias.")

    st.markdown("""
    - **Pandas** está diseñado para la manipulación y análisis de datos contenidos en DataFrames.
    - **Matplotlib** permite crear gráficos estáticos, animados e interactivos.
    - **Seaborn** facilita la creación de gráficos complejos con código menos complejo que Matplotlib (en algunos casos).
    """)
    
    df = sns.load_dataset("mpg")
    st.write(df)
    
    # Mostrar la forma del DataFrame
    st.write("### Forma del DataFrame")
    st.write(df.shape)

    # Mostrar información del DataFrame
    st.write("### Información del DataFrame")
    buffer = StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    # Sección sobre los datos
    st.write("### Sobre los datos")
    st.markdown("""
    - El DataFrame se compone por 398 entidades y 9 columnas con características correspondientes.
    - En *horsepower* se nota la existencia de 392 entidades no nulas, es decir, existen 6 con valores nulos.
    - Existen 4 valores float, 3 int y 2 object.
    - El número de cilindros y el año del modelo pueden ser tratados como categoriales y aplicar One-Hot o Label Encoding.
    """)
    
    st.write(df.describe())
    
    # Conteo de valores en la columna 'model_year'
    st.write("### Conteo de años del modelo")
    st.bar_chart(df['model_year'].value_counts())  # Muestra un gráfico de barras
    
    st.write('### Conteo por cantidad de cilindros')
    st.bar_chart(df['cylinders'].value_counts())
    
    faltasYduplicados(df)

def faltasYduplicados(df):
    # Detección de valores faltantes y duplicados
    st.write("### Detección de valores faltantes y corrección de duplicados")

    # Mostrar valores faltantes
    missing_values = df.isnull().sum()
    st.write("Valores faltantes por columna:")
    st.write(missing_values)  # Muestra solo columnas con valores faltantes

    # Mostrar duplicados
    st.write(f"Número de filas duplicadas: {df.duplicated().sum()}")

    # Explicación sobre tratamiento de datos faltantes y duplicados
    st.markdown("""
    Los valores faltantes y duplicados pueden afectar al análisis posterior de algún modelo de aprendizaje automático. Sin embargo, esto no quiere decir que un dataset con estos componentes sea inservible. 

    Dependiendo del conjunto de datos con el que se trabaje, se debe tomar una decisión para el tratamiento de una forma u otra de dichos casos. 

    Los valores faltantes bien pueden ser sustituidos por modas o medias, o ser eliminada por completo su fila correspondiente. 

    En cuanto a los duplicados, si la existencia de estos no afecta a la problemática planteada, no es necesario que sean borrados del conjunto.
    """)

if __name__ == "__main__":
    main()
