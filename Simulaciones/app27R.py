import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Constantes
CT = 10000  # Capacidad total del servicentro en litros
D = 50  # Demanda promedio de litros por usuario

# Título de la aplicación
st.title("Simulación del Servicentro")
st.header("Antonio Elias Sánchez Soto")
st.subheader("BDFC 301")

# Texto del ejercicio
st.markdown(
    """
## Ejercicio 27

Un servicentro con una capacidad de depósito de 10000 litros recibe semanalmente 
un suministro de gasolina que varía entre 5000 y 10000 litros según una distribución 
uniforme. El número de usuarios que solicita servicios a la semana en dicho 
servicentro es aleatorio con valores de 100, 120, 130, 140 y 150 usuarios con la 
misma probabilidad para cada valor, conociéndose que la demanda promedio por 
usuario es de 50 litros. Simulando varias semanas de funcionamiento del 
servicentro, determine:  

- **a)** Cantidad media de litros de gasolina que quedan en depósito semanalmente.  
- **b)** Número medio de usuarios que no satisfacen su demanda.  
- **c)** Cantidad media de litros que no puede recibir del suministrador por estar el depósito lleno. 
"""
)

# Solicitar al usuario la cantidad de semanas a simular
n = st.number_input(
    "Introduce la cantidad de semanas a visualizar:", min_value=1, value=10
)

# Inicialización de variables
G = np.zeros(n)  # Cantidad de gasolina en el depósito
CPI = np.zeros(n)  # Cantidad de personas insatisfechas
CNS = np.zeros(n)  # Cantidad de gasolina no suministrada
U1 = np.random.rand(n)  # Valores generados para U1 (distribución uniforme)
U2 = np.random.rand(n)  # Valores generados para U2 (distribución discreta)

# Cálculo del suministro y número de usuarios
suministro = 5000 + (10000 - 5000) * U1  # Suministro semanal usando U1

# Determinación del número de usuarios usando U2
usuarios = np.zeros(n)
frecuencias = [100, 120, 130, 140, 150]
probabilidades = [0.2, 0.4, 0.6, 0.8, 1.0]

for i in range(n):
    for j in range(len(probabilidades)):
        if U2[i] <= probabilidades[j]:
            usuarios[i] = frecuencias[j]
            break

# Simulación por semanas
for i in range(n):
    if i == 0:
        G[i] = 0  # Inicialmente el depósito está vacío
    else:
        G[i] = G[i - 1]  # Copia la cantidad de gasolina del depósito anterior

    # Suma el suministro semanal al depósito
    G[i] += suministro[i]

    # Calcula la demanda total
    demanda_total = usuarios[i] * D

    # Casos para calcular G(i), CPIi y CNSi
    if G[i] < demanda_total:
        CPI[i] = round((demanda_total - G[i]) / D)  # Personas insatisfechas
        G[i] = 0  # Se vacía el depósito
    else:
        CPI[i] = 0  # No hay personas insatisfechas
        G[i] -= demanda_total  # Resta la demanda

    if G[i - 1] + suministro[i] > CT:
        CNS[i] = (G[i - 1] + suministro[i]) - CT  # Gasolina no suministrada
        G[i] = CT  # Llenar el depósito hasta su capacidad máxima

# Cálculo de las medias solicitadas
media_gasolina = np.mean(G)
media_insatisfechos = np.mean(CPI)
media_no_suministrada = np.mean(CNS)

# Creación de una tabla con los resultados por semana, incluyendo U1 y U2
resultados = pd.DataFrame(
    {
        "Semana": range(1, n + 1),
        "U1": U1,
        "Suministro": suministro,
        "U2": U2,
        "Usuarios": usuarios,
        "Gasolina en Depósito": G,
        "Personas Insatisfechas": CPI,
        "Gasolina No Suministrada": CNS,
    }
)

# Mostrar resultados finales en Streamlit
st.subheader("Resultados por semana:")
st.dataframe(resultados)

st.subheader("Promedios:")

# Gráficos para visualizar las proporciones
st.write("Media de litros en el depósito:", media_gasolina)
# Gráfico para Gasolina en Depósito
plt.figure(figsize=(10, 6))
plt.plot(range(1, n + 1), G, marker="o", label="Gasolina en Depósito")
plt.axhline(y=media_gasolina, color="r", linestyle="--", label="Media Gasolina")
plt.title("Gasolina en Depósito por Semana")
plt.xlabel("Semana")
plt.ylabel("Litros")
plt.xticks(range(1, n + 1))
plt.legend()
st.pyplot(plt)

st.write("Media de personas insatisfechas:", media_insatisfechos)
# Gráfico para Personas Insatisfechas
plt.figure(figsize=(10, 6))
plt.plot(
    range(1, n + 1), CPI, marker="o", label="Personas Insatisfechas", color="orange"
)
plt.axhline(
    y=media_insatisfechos, color="r", linestyle="--", label="Media Insatisfechos"
)
plt.title("Personas Insatisfechas por Semana")
plt.xlabel("Semana")
plt.ylabel("Cantidad")
plt.xticks(range(1, n + 1))
plt.legend()
st.pyplot(plt)

st.write("Media de litros no suministrados:", media_no_suministrada)
# Gráfico para Gasolina No Suministrada
plt.figure(figsize=(10, 6))
plt.plot(
    range(1, n + 1), CNS, marker="o", label="Gasolina No Suministrada", color="green"
)
plt.axhline(
    y=media_no_suministrada, color="r", linestyle="--", label="Media No Suministrada"
)
plt.title("Gasolina No Suministrada por Semana")
plt.xlabel("Semana")
plt.ylabel("Litros")
plt.xticks(range(1, n + 1))
plt.legend()
st.pyplot(plt)

#######################################################################################################

# Reduccion de varianza
st.subheader("Reducción de Varianza:")
# Solicitar al usuario la cantidad total de números a generar
total_numeros = st.number_input(
    "Introduce el total de semanas a generar:", min_value=2, value=30
)

# Validar si el número es impar
if total_numeros % 2 != 0:
    st.warning(
        "Por favor, introduce un número par para aplicar la técnica de reducción de varianza."
    )
else:
    # Generar la mitad de los números aleatorios
    n = total_numeros // 2

    # Generar U1 y U2
    U1 = np.random.rand(n)  # Generar n números para U1
    U2 = np.random.rand(n)  # Generar n números para U2

    # Calcular los complementos
    U1_complemento = 1 - U1  # Complemento de U1
    U2_complemento = 1 - U2  # Complemento de U2

    # Combinar los resultados en un solo array
    U1_total = np.concatenate((U1, U1_complemento))
    U2_total = np.concatenate((U2, U2_complemento))

    # Inicialización de variables para el total de números generados
    G_total = np.zeros(total_numeros)  # Cantidad de gasolina en el depósito
    CPI_total = np.zeros(total_numeros)  # Cantidad de personas insatisfechas
    CNS_total = np.zeros(total_numeros)  # Cantidad de gasolina no suministrada

    # Cálculo del suministro usando U1 total
    suministro_total = 5000 + (10000 - 5000) * U1_total  # Suministro usando U1 total

    # Determinación del número de usuarios usando U2 total
    usuarios_total = np.zeros(total_numeros)
    frecuencias = [100, 120, 130, 140, 150]
    probabilidades = [0.2, 0.4, 0.6, 0.8, 1.0]

    for i in range(total_numeros):
        for j in range(len(probabilidades)):
            if U2_total[i] <= probabilidades[j]:
                usuarios_total[i] = frecuencias[j]
                break

    # Simulación por semanas utilizando las variables generadas
    for i in range(total_numeros):
        if i == 0:
            G_total[i] = 0  # Inicialmente el depósito está vacío
        else:
            G_total[i] = G_total[
                i - 1
            ]  # Copia la cantidad de gasolina del depósito anterior

        # Suma el suministro semanal al depósito
        G_total[i] += suministro_total[i]

        # Calcula la demanda total
        demanda_total = usuarios_total[i] * D

        # Casos para calcular G(i), CPIi y CNSi
        if G_total[i] < demanda_total:
            CPI_total[i] = round((demanda_total - G_total[i]) / D)  # Personas insatisfechas
            G_total[i] = 0  # Se vacía el depósito
        else:
            CPI_total[i] = 0  # No hay personas insatisfechas
            G_total[i] -= demanda_total  # Resta la demanda

        if G_total[i - 1] + suministro_total[i] > CT:
            CNS_total[i] = (
                G_total[i - 1] + suministro_total[i]
            ) - CT  # Gasolina no suministrada
            G_total[i] = CT  # Llenar el depósito hasta su capacidad máxima

    # Cálculo de las medias solicitadas para las variables de salida
    media_gasolina = np.mean(G_total)
    media_insatisfechos = np.mean(CPI_total)
    media_no_suministrada = np.mean(CNS_total)

    # Crear DataFrame con los resultados finales incluyendo todas las variables relevantes
    resultados_reduccion_varianza = pd.DataFrame(
        {
            "Número": range(1, total_numeros + 1),
            "U1": np.concatenate((U1, U1_complemento)),
            "Suministro": suministro_total,
            "U2": np.concatenate((U2, U2_complemento)),
            "Usuarios": usuarios_total,
            "Gasolina en Depósito": G_total,
            "Personas Insatisfechas": CPI_total,
            "Gasolina No Suministrada": CNS_total,
        }
    )

    # Mostrar la tabla resultante en Streamlit junto con las medias calculadas
    st.dataframe(resultados_reduccion_varianza)

    st.subheader("Promedios:")
    st.write("Media de litros en el depósito:", media_gasolina)
    st.write("Media de personas insatisfechas:", media_insatisfechos)
    st.write("Media de litros no suministrados:", media_no_suministrada)
