import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from utils import carregar_dados, gerar_recomendacao


FEATURES = ["temperatura", "umidade", "chuva", "ndvi", "ph_solo"]
TARGET = "risco"


def treinar_modelo() -> DecisionTreeClassifier:
    dados = carregar_dados()
    x = dados[FEATURES]
    y = dados[TARGET]

    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    modelo = DecisionTreeClassifier(max_depth=4, random_state=42)
    modelo.fit(x_treino, y_treino)

    previsoes = modelo.predict(x_teste)
    acuracia = accuracy_score(y_teste, previsoes)

    print(f"Acuracia do modelo: {acuracia:.2%}")
    print("\nRelatorio de classificacao:")
    print(classification_report(y_teste, previsoes))

    return modelo


def prever_risco(
    temperatura: float,
    umidade: float,
    chuva: float,
    ndvi: float,
    ph_solo: float,
    modelo: DecisionTreeClassifier | None = None,
) -> tuple[str, str]:
    modelo_treinado = modelo or treinar_modelo()
    entrada = pd.DataFrame(
        [[temperatura, umidade, chuva, ndvi, ph_solo]],
        columns=FEATURES,
    )
    risco = str(modelo_treinado.predict(entrada)[0])
    recomendacao = gerar_recomendacao(risco)

    return risco, recomendacao


if __name__ == "__main__":
    modelo = treinar_modelo()
    risco_previsto, recomendacao = prever_risco(34, 35, 3, 0.35, 6.2, modelo)
    print("\nExemplo de previsao:")
    print(f"Risco previsto: {risco_previsto}")
    print(f"Recomendacao: {recomendacao}")
