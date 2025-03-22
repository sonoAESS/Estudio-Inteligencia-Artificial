import numpy as np
import pandas as pd
import streamlit as st

# Constantes
CT = 10000  # Capacidad total del servicentro en litros
D = 50      # Demanda promedio de litros por usuario

# Título de la aplicación
st.title("Simulación del Servicentro")

# Solicitar al usuario la cantidad de semanas a simular
n = st.number_input("Introduce la cantidad de semanas a visualizar:", min_value=1, value=10)

# Inicialización de variables
G = np.zeros(n)      # Cantidad de gasolina en el depósito
CPI = np.zeros(n)    # Cantidad de personas insatisfechas
CNS = np.zeros(n)    # Cantidad de gasolina no suministrada

# Distribuciones
suministro = np.random.uniform(5000, 10000, n)  # Suministro semanal
usuarios = np.random.choice([100, 120, 130, 140, 150], size=n)  # Número de usuarios

# Simulación por semanas
for i in range(n):
    if i == 0:
        G[i] = 0  # Inicialmente el depósito está vacío
    else:
        G[i] = G[i-1]  # Copia la cantidad de gasolina del depósito anterior
    
    # Suma el suministro semanal al depósito
    G[i] += suministro[i]
    
    # Calcula la demanda total
    demanda_total = usuarios[i] * D
    
    # Casos para calcular G(i), CPIi y CNSi
    if G[i] < demanda_total:
        CPI[i] = (demanda_total - G[i]) / D  # Personas insatisfechas
        G[i] = 0  # Se vacía el depósito
    else:
        CPI[i] = 0  # No hay personas insatisfechas
        G[i] -= demanda_total  # Resta la demanda
    
    if G[i-1] + suministro[i] > CT:
        CNS[i] = (G[i-1] + suministro[i]) - CT  # Gasolina no suministrada
        G[i] = CT  # Llenar el depósito hasta su capacidad máxima

# Cálculo de las medias solicitadas
media_gasolina = np.mean(G)
media_insatisfechos = np.mean(CPI)
media_no_suministrada = np.mean(CNS)

# Creación de una tabla con los resultados por semana
resultados = pd.DataFrame({
    'Semana': range(1, n+1),
    'Suministro': suministro,
    'Usuarios': usuarios,
    'Gasolina en Depósito': G,
    'Personas Insatisfechas': CPI,
    'Gasolina No Suministrada': CNS,
})

# Mostrar resultados finales en Streamlit
st.subheader("Resultados por semana:")
st.dataframe(resultados)

st.subheader("Promedios:")
st.write("Media de litros en el depósito:", media_gasolina)
st.write("Media de personas insatisfechas:", media_insatisfechos)
st.write("Media de litros no suministrados:", media_no_suministrada)
