import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de Crecimiento de Plantas", layout="centered")

# titulos
st.title("Simulador de Crecimiento de Plantas")
st.write("Ajusta los parámetros ambientales y observa cómo cambian las curvas de crecimiento.")

# side bar
st.sidebar.header("Parámetros ambientales")

temperatura = st.sidebar.slider("Temperatura (°C)", 5, 40, 25)
luz = st.sidebar.slider("Horas de luz por día", 0, 24, 12)
agua = st.sidebar.slider("Riego (ml/día)", 0, 500, 150)
dias = st.sidebar.slider("Días de simulación", 10, 180, 60)

# --- MODELO DE CRECIMIENTO ---
# Modelo simple: crecimiento logístico modulado por ambiente
def factor_ambiente(temperatura, luz, agua):
    # Valores óptimos
    opt_temp = 25
    opt_luz = 12
    opt_agua = 200

    f_temp = np.exp(-((temperatura - opt_temp) ** 2) / 50)
    f_luz = np.exp(-((luz - opt_luz) ** 2) / 30)
    f_agua = np.exp(-((agua - opt_agua) ** 2) / 5000)

    return (f_temp + f_luz + f_agua) / 3

def crecimiento(dias, ambiente):
    t = np.linspace(0, dias, dias)
    K = 100 * ambiente           # tamaño máximo ajustado por ambiente
    r = 0.15 + 0.3 * ambiente    # tasa de crecimiento ajustada
    altura = K / (1 + np.exp(-r * (t - dias/2)))
    return t, altura

ambiente = factor_ambiente(temperatura, luz, agua)
t, altura = crecimiento(dias, ambiente)

# resultados del crecimiento
st.subheader("Condición ambiental global")
st.metric("Índice ambiental (0–1)", f"{ambiente:.2f}")

# grafica
fig, ax = plt.subplots()
ax.plot(t, altura, color="green", linewidth=2)
ax.set_title("Crecimiento simulado de la planta")
ax.set_xlabel("Días")
ax.set_ylabel("Altura (cm)")
ax.grid(True)

st.pyplot(fig)

