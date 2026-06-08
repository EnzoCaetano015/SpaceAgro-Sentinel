import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from modelo_ml import prever_risco, treinar_modelo
from utils import carregar_dados


st.set_page_config(
    page_title="SpaceAgro Sentinel",
    page_icon="🛰️",
    layout="wide",
)


@st.cache_data
def obter_dados():
    return carregar_dados()


@st.cache_resource
def obter_modelo():
    return treinar_modelo()


dados = obter_dados()
modelo = obter_modelo()

st.title("SpaceAgro Sentinel")
st.subheader("Sistema inteligente de monitoramento agricola com dados espaciais, sensores e IA")
st.write(
    "A POC usa dados ambientais simulados, NDVI inspirado em satelites, sensor ESP32/DHT22 "
    "e Machine Learning para classificar o risco agricola de uma regiao."
)

media_temperatura, media_umidade, media_chuva, media_ndvi = st.columns(4)
media_temperatura.metric("Temperatura media", f"{dados['temperatura'].mean():.1f} C")
media_umidade.metric("Umidade media", f"{dados['umidade'].mean():.1f}%")
media_chuva.metric("Chuva media", f"{dados['chuva'].mean():.1f} mm")
media_ndvi.metric("NDVI medio", f"{dados['ndvi'].mean():.2f}")

st.divider()
st.markdown("### Base de dados")
st.dataframe(dados, use_container_width=True)

coluna_grafico_1, coluna_grafico_2 = st.columns(2)

with coluna_grafico_1:
    figura, eixo = plt.subplots(figsize=(7, 4))
    sns.countplot(data=dados, x="risco", order=["baixo", "medio", "alto"], ax=eixo, palette="Set2", hue="risco", legend=False)
    eixo.set_title("Registros por risco")
    st.pyplot(figura)

with coluna_grafico_2:
    figura, eixo = plt.subplots(figsize=(7, 4))
    ndvi_regiao = dados.groupby("regiao", as_index=False)["ndvi"].mean()
    sns.barplot(data=ndvi_regiao, x="regiao", y="ndvi", ax=eixo, color="#6A994E")
    eixo.set_title("NDVI medio por regiao")
    eixo.tick_params(axis="x", rotation=25)
    st.pyplot(figura)

st.sidebar.header("Prever risco agricola")
temperatura = st.sidebar.number_input("Temperatura (C)", min_value=0.0, max_value=60.0, value=30.0, step=0.5)
umidade = st.sidebar.number_input("Umidade (%)", min_value=0.0, max_value=100.0, value=55.0, step=1.0)
chuva = st.sidebar.number_input("Chuva (mm)", min_value=0.0, max_value=200.0, value=10.0, step=0.5)
ndvi = st.sidebar.number_input("NDVI", min_value=0.0, max_value=1.0, value=0.55, step=0.01)
ph_solo = st.sidebar.number_input("pH do solo", min_value=0.0, max_value=14.0, value=6.5, step=0.1)

if st.sidebar.button("Prever risco"):
    risco, recomendacao = prever_risco(temperatura, umidade, chuva, ndvi, ph_solo, modelo)
    st.sidebar.success(f"Risco previsto: {risco.upper()}")
    st.sidebar.info(recomendacao)
