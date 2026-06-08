import matplotlib.pyplot as plt
import seaborn as sns

from utils import carregar_dados, salvar_grafico


def gerar_graficos() -> None:
    dados = carregar_dados()
    sns.set_theme(style="whitegrid")

    print("Primeiras linhas da base:")
    print(dados.head())
    print("\nEstatisticas descritivas:")
    print(dados.describe())
    print("\nDados nulos por coluna:")
    print(dados.isnull().sum())

    figura, eixo = plt.subplots(figsize=(8, 5))
    sns.histplot(dados["temperatura"], kde=True, ax=eixo, color="#D94F30")
    eixo.set_title("Distribuicao da temperatura")
    eixo.set_xlabel("Temperatura (C)")
    salvar_grafico(figura, "distribuicao_temperatura.png")
    plt.close(figura)

    figura, eixo = plt.subplots(figsize=(8, 5))
    sns.histplot(dados["umidade"], kde=True, ax=eixo, color="#227C9D")
    eixo.set_title("Distribuicao da umidade")
    eixo.set_xlabel("Umidade (%)")
    salvar_grafico(figura, "distribuicao_umidade.png")
    plt.close(figura)

    figura, eixo = plt.subplots(figsize=(9, 5))
    chuva_regiao = dados.groupby("regiao", as_index=False)["chuva"].mean()
    sns.barplot(data=chuva_regiao, x="regiao", y="chuva", ax=eixo, color="#2A9D8F")
    eixo.set_title("Chuva media por regiao")
    eixo.set_xlabel("Regiao")
    eixo.set_ylabel("Chuva (mm)")
    eixo.tick_params(axis="x", rotation=25)
    salvar_grafico(figura, "chuva_por_regiao.png")
    plt.close(figura)

    figura, eixo = plt.subplots(figsize=(9, 5))
    ndvi_regiao = dados.groupby("regiao", as_index=False)["ndvi"].mean()
    sns.barplot(data=ndvi_regiao, x="regiao", y="ndvi", ax=eixo, color="#6A994E")
    eixo.set_title("NDVI medio por regiao")
    eixo.set_xlabel("Regiao")
    eixo.set_ylabel("NDVI medio")
    eixo.tick_params(axis="x", rotation=25)
    salvar_grafico(figura, "ndvi_medio_por_regiao.png")
    plt.close(figura)

    figura, eixo = plt.subplots(figsize=(7, 5))
    sns.countplot(data=dados, x="risco", order=["baixo", "medio", "alto"], ax=eixo, palette="Set2", hue="risco", legend=False)
    eixo.set_title("Quantidade de registros por classe de risco")
    eixo.set_xlabel("Risco")
    eixo.set_ylabel("Quantidade")
    salvar_grafico(figura, "registros_por_risco.png")
    plt.close(figura)

    figura, eixo = plt.subplots(figsize=(8, 6))
    correlacao = dados[["temperatura", "umidade", "chuva", "ndvi", "ph_solo"]].corr()
    sns.heatmap(correlacao, annot=True, cmap="RdYlGn", ax=eixo)
    eixo.set_title("Correlacao entre variaveis numericas")
    salvar_grafico(figura, "correlacao_variaveis.png")
    plt.close(figura)

    print("\nGraficos salvos em docs/imagens/.")


if __name__ == "__main__":
    gerar_graficos()
