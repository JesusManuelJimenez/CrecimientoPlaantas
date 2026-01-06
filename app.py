import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Crecimiento de Plantas",
    page_icon="🌱",
    layout="wide"
)

#Modelo matematico
def crecimiento_logistico(t, P0, Pmax, r, L, N, W):
    r_efectivo = r * L * N * W
    return Pmax / (1 + ((Pmax - P0) / P0) * np.exp(-r_efectivo * t))

st.title("🌱 Simulador de Crecimiento de Plantas 🌱")

st.markdown(
    "Simulación del crecimiento vegetal usando un modelo logístico, considerando luz, nutrientes y agua."
)

st.divider()

#side bar y controles
st.sidebar.header("Parámetros de simulación")

dias = st.sidebar.slider(
    "Tiempo de simulación (días)",
    min_value=10,
    max_value=200,
    value=100
)

st.sidebar.divider()

#datos de planta A
st.sidebar.subheader("🌿 Planta A")

P0_A = st.sidebar.slider("Tamaño inicial A (m)", 0.01, 1.0, 0.1)
Pmax_A = st.sidebar.slider("Tamaño máximo A (m)", 0.5, 5.0, 2.0)
r_A = st.sidebar.slider("Tasa de crecimiento A", 0.01, 0.5, 0.1)

L_A = st.sidebar.slider("Luz A", 0.0, 1.0, 1.0)
N_A = st.sidebar.slider("Nutrientes A", 0.0, 1.0, 1.0)
W_A = st.sidebar.slider("Agua A", 0.0, 1.0, 1.0)

st.sidebar.divider()

#datos de planta B
st.sidebar.subheader("🌱 Planta B")

P0_B = st.sidebar.slider("Tamaño inicial B (m)", 0.01, 1.0, 0.1)
Pmax_B = st.sidebar.slider("Tamaño máximo B (m)", 0.5, 5.0, 2.0)
r_B = st.sidebar.slider("Tasa de crecimiento B", 0.01, 0.5, 0.1)

L_B = st.sidebar.slider("Luz B", 0.0, 1.0, 0.7)
N_B = st.sidebar.slider("Nutrientes B", 0.0, 1.0, 0.7)
W_B = st.sidebar.slider("Agua B", 0.0, 1.0, 0.7)

#simulacion
t = np.linspace(0, dias, 400)

P_A = crecimiento_logistico(t, P0_A, Pmax_A, r_A, L_A, N_A, W_A)
P_B = crecimiento_logistico(t, P0_B, Pmax_B, r_B, L_B, N_B, W_B)

#grafica
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(t, P_A, label="Planta A")
ax.plot(t, P_B, label="Planta B")

ax.set_xlabel("Tiempo (días)")
ax.set_ylabel("Tamaño de la planta (m)")
ax.set_title("Comparación del crecimiento de dos plantas")
ax.legend()
ax.grid(True)

st.pyplot(fig)

#datos de la simulacion
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔬 Interpretación biológica")
    st.markdown(
        "- El crecimiento inicial es rápido cuando la planta es pequeña.\n"
        "- Conforme se acerca a su tamaño máximo, el crecimiento se desacelera.\n"
        "- Menores valores de luz, nutrientes o agua reducen la tasa de crecimiento."
    )

with col2:
    st.subheader("📐 Modelo matemático")
    st.latex(r"\frac{dP}{dt} = rP\left(1 - \frac{P}{P_{max}}\right)")
    st.latex(
        r"P(t) = \frac{P_{max}}{1 + \left(\frac{P_{max}-P_0}{P_0}\right)e^{-r_{efectivo} t}}"
    )
