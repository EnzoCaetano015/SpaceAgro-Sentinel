from datetime import datetime, timedelta
import random

import pandas as pd

from utils import DATA_DIR, classificar_risco, garantir_diretorios


REGIOES = ["Ribeirao Verde", "Vale do Sol", "Serra Azul", "Campo Novo", "Planicie Norte"]


def gerar_registro_agricola(indice: int) -> dict:
    data = datetime(2026, 1, 1) + timedelta(days=indice)
    regiao = REGIOES[indice % len(REGIOES)]
    perfil = indice % 3

    if perfil == 0:
        temperatura = round(random.uniform(23, 29), 1)
        umidade = round(random.uniform(58, 82), 1)
        chuva = round(random.uniform(14, 35), 1)
        ndvi = round(random.uniform(0.62, 0.88), 2)
    elif perfil == 1:
        temperatura = round(random.uniform(29, 33), 1)
        umidade = round(random.uniform(42, 58), 1)
        chuva = round(random.uniform(5, 15), 1)
        ndvi = round(random.uniform(0.42, 0.62), 2)
    else:
        temperatura = round(random.uniform(33, 38), 1)
        umidade = round(random.uniform(25, 39), 1)
        chuva = round(random.uniform(0, 4.9), 1)
        ndvi = round(random.uniform(0.25, 0.39), 2)

    ph_solo = round(random.uniform(5.2, 7.6), 1)
    risco = classificar_risco(temperatura, umidade, chuva, ndvi)

    return {
        "data": data.strftime("%Y-%m-%d"),
        "regiao": regiao,
        "temperatura": temperatura,
        "umidade": umidade,
        "chuva": chuva,
        "ndvi": ndvi,
        "ph_solo": ph_solo,
        "risco": risco,
    }


def gerar_registro_sensor(indice: int) -> dict:
    data_hora = datetime(2026, 1, 1, 8, 0) + timedelta(hours=indice * 3)

    return {
        "data_hora": data_hora.strftime("%Y-%m-%d %H:%M:%S"),
        "temperatura": round(random.uniform(21, 37), 1),
        "umidade": round(random.uniform(28, 85), 1),
        "origem": "ESP32_DHT22_SIMULADO",
    }


def gerar_bases(total_registros: int = 150) -> None:
    garantir_diretorios()
    random.seed(42)

    registros_agricolas = []
    registros_sensor = []

    for indice in range(total_registros):
        registros_agricolas.append(gerar_registro_agricola(indice))

    for indice in range(80):
        registros_sensor.append(gerar_registro_sensor(indice))

    dados_agricolas = pd.DataFrame(registros_agricolas)
    dados_sensor = pd.DataFrame(registros_sensor)

    dados_agricolas.to_csv(DATA_DIR / "dados_agricolas_espaciais.csv", index=False)
    dados_sensor.to_csv(DATA_DIR / "dados_sensor_esp32.csv", index=False)


if __name__ == "__main__":
    gerar_bases()
    print("Bases CSV geradas com sucesso na pasta data/.")
