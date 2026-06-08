from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
DOCS_DIR = ROOT_DIR / "docs"
IMAGENS_DIR = DOCS_DIR / "imagens"


def garantir_diretorios() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    IMAGENS_DIR.mkdir(parents=True, exist_ok=True)


def classificar_risco(temperatura: float, umidade: float, chuva: float, ndvi: float) -> str:
    if temperatura > 32 and umidade < 40 and chuva < 5 and ndvi < 0.40:
        return "alto"

    criterios_medios = [
        temperatura > 30,
        umidade < 50,
        chuva < 12,
        ndvi < 0.55,
    ]

    if sum(criterios_medios) >= 2:
        return "medio"

    return "baixo"


def gerar_recomendacao(risco: str) -> str:
    if risco == "alto":
        return "Aumentar monitoramento da irrigacao e verificar sinais de estresse hidrico."
    if risco == "medio":
        return "Manter acompanhamento e revisar previsao climatica."
    return "Condicao estavel para a plantacao."


def carregar_dados(caminho: Path | None = None) -> pd.DataFrame:
    caminho_csv = caminho or DATA_DIR / "dados_agricolas_espaciais.csv"

    if not caminho_csv.exists():
        from gerar_dados import gerar_bases

        gerar_bases()

    return pd.read_csv(caminho_csv)


def salvar_grafico(figura, nome_arquivo: str) -> Path:
    garantir_diretorios()
    caminho = IMAGENS_DIR / nome_arquivo
    figura.savefig(caminho, dpi=140, bbox_inches="tight")
    return caminho
