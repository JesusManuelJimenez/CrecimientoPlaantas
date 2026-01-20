import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Crecimiento de Plantas",
    page_icon="🌱",
    layout="wide"
)


def saturacion(x, k):
    return x / (x + k)

#modelo matematico
def crecimiento_logistico(t, P0, Pmax, r, L, N, W):
   
    L_eff = saturacion(L, 0.3)
    N_eff = saturacion(N, 0.3)


    r_eff = r * L_eff * N_eff * W

    
    Pmax_eff = Pmax * (0.5 + 0.5 * N_eff * W)

    P = Pmax_eff / (1 + ((Pmax_eff - P0) / P0) * np.exp(-r_eff * t))

   
    dPdt = r_eff * P * (1 - P / Pmax_eff)

    return P, dPdt, r_eff, Pmax_eff

#titulo
st.title("🌱 Simulador Avanzado de Crecimiento de Plantas")

st.markdown(
    "Modelo matemático de crecimiento vegetal basado en una ecuación logística con facotres ambientales"
)

st.divider()

#sidebar
st.sidebar.header("Parámetros generales")

dias = st.sidebar.slider("Tiempo de simulación (días)", 20, 200, 120)

st.sidebar.divider()

#planta A
st.sidebar.subheader("🌿 Planta A")

P0_A = st.sidebar.slider("Tamaño inicial A (m)", 0.01, 1.0, 0.1)
Pmax_A = st.sidebar.slider("Tamaño máximo teórico A (m)", 0.5, 5.0, 2.0)
r_A = st.sidebar.slider("Tasa de crecimiento A", 0.01, 0.5, 0.12)

L_A = st.sidebar.slider("Luz A", 0.0, 1.0, 1.0)
N_A = st.sidebar.slider("Nutrientes A", 0.0, 1.0, 1.0)
W_A = st.sidebar.slider("Agua A", 0.0, 1.0, 1.0)

st.sidebar.divider()

#planta B
st.sidebar.subheader("🌱 Planta B")

P0_B = st.sidebar.slider("Tamaño inicial B (m)", 0.01, 1.0, 0.1)
Pmax_B = st.sidebar.slider("Tamaño máximo teórico B (m)", 0.5, 5.0, 2.0)
r_B = st.sidebar.slider("Tasa de crecimiento B", 0.01, 0.5, 0.12)

L_B = st.sidebar.slider("Luz B", 0.0, 1.0, 0.6)
N_B = st.sidebar.slider("Nutrientes B", 0.0, 1.0, 0.6)
W_B = st.sidebar.slider("Agua B", 0.0, 1.0, 0.6)


#simulacion
t = np.linspace(0, dias, 500)

P_A, dP_A, r_eff_A, Pmax_eff_A = crecimiento_logistico(
    t, P0_A, Pmax_A, r_A, L_A, N_A, W_A
)

P_B, dP_B, r_eff_B, Pmax_eff_B = crecimiento_logistico(
    t, P0_B, Pmax_B, r_B, L_B, N_B, W_B
)


#graficas
col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    ax1.plot(t, P_A, label="Planta A")
    ax1.plot(t, P_B, label="Planta B")
    ax1.set_xlabel("Tiempo (días)")
    ax1.set_ylabel("Tamaño (m)")
    ax1.set_title("Crecimiento de la planta")
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    ax2.plot(t, dP_A, label="Velocidad A")
    ax2.plot(t, dP_B, label="Velocidad B")
    ax2.set_xlabel("Tiempo (días)")
    ax2.set_ylabel("dP/dt")
    ax2.set_title("Velocidad de crecimiento")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)


#metricas
st.divider()
st.subheader("📊 Resultados cuantitativos")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Altura final A (m)", f"{P_A[-1]:.2f}")
m2.metric("Altura final B (m)", f"{P_B[-1]:.2f}")
m3.metric("r efectiva A", f"{r_eff_A:.3f}")
m4.metric("r efectiva B", f"{r_eff_B:.3f}")


st.divider()
st.subheader("Interpretación del modelo")

st.markdown(
"""
- El crecimiento sigue una curva sigmoidea debido a la limitación progresiva de recursos.
- El tamaño máximo alcanzable depende del entorno, no solo de la genética.
- El modelo solo es idealizado
"""
)

st.latex(r"\frac{dP}{dt} = r_{ef} P \left(1 - \frac{P}{P_{max,ef}}\right)")
