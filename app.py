import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de página
st.set_page_config(
    page_title="Simulador de Crecimiento de Plantas",
    layout="centered"
)

# Cargar CSS externo
with open("estilo.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ===== TÍTULO PRINCIPAL =====
st.markdown("<h1>🌿 Simulador de Crecimiento de Plantas</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Ajusta los parámetros y observa cómo crece tu planta.</p>", unsafe_allow_html=True)

# ===== SIDEBAR =====
st.sidebar.header("⚙️ Parámetros")

temperatura = st.sidebar.slider("🌡️ Temperatura (°C)", 5, 40, 25)
luz = st.sidebar.slider("☀️ Horas de luz", 0, 24, 12)
agua = st.sidebar.slider("💧 Riego (ml/día)", 0, 500, 150)
dias = st.sidebar.slider("📅 Días de simulación", 10, 180, 60)

# ===== MODELO =====
def factor_ambiente(temperatura, luz, agua):
    opt_temp = 25
    opt_luz = 12
    opt_agua = 200

    f_temp = np.exp(-((temperatura - opt_temp) ** 2) / 50)
    f_luz = np.exp(-((luz - opt_luz) ** 2) / 30)
    f_agua = np.exp(-((agua - opt_agua) ** 2) / 5000)

    return (f_temp + f_luz + f_agua) / 3

def crecimiento(dias, ambiente):
    t = np.linspace(0, dias, dias)
    K = 100 * ambiente
    r = 0.15 + 0.3 * ambiente
    altura = K / (1 + np.exp(-r * (t - dias/2)))
    return t, altura

ambiente = factor_ambiente(temperatura, luz, agua)
t, altura = crecimiento(dias, ambiente)

# ===== METRICAS =====
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h3>🌱 Condición Ambiental</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.metric("Índice Ambiental", f"{ambiente:.2f}")
with col2:
    st.metric("Altura Máxima Estimada", f"{max(altura):.1f} cm")

st.markdown("</div>", unsafe_allow_html=True)

# ===== GRAFICA =====
fig, ax = plt.subplots(figsize=(7,4))
ax.plot(t, altura, linewidth=3)
ax.set_facecolor("#f0fdf4")
ax.set_title("Crecimiento de la Planta", color="#1b4332", fontsize=14)
ax.set_xlabel("Días")
ax.set_ylabel("Altura (cm)")
ax.grid(alpha=0.3)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.pyplot(fig)
st.markdown("</div>", unsafe_allow_html=True)
