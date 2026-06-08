# Arquitetura da Solucao

Fluxo principal:

```text
Dados ambientais + ESP32 -> CSV -> Pandas -> ML -> Dashboard -> Recomendacao
```

## Camada de dados

A base principal fica em `data/dados_agricolas_espaciais.csv` e contem dados sinteticos de temperatura, umidade, chuva, NDVI, pH do solo e risco agricola. A base `data/dados_sensor_esp32.csv` simula leituras de um sensor DHT22 conectado ao ESP32.

## Camada de processamento

O script `src/analise_dados.py` carrega os dados com Pandas, verifica estatisticas, identifica dados nulos e gera graficos para apoiar a interpretacao.

## Camada de IA

O script `src/modelo_ml.py` treina um classificador `DecisionTreeClassifier` com as variaveis ambientais e estima a classe de risco agricola.

## Camada de visualizacao

O dashboard em `src/dashboard.py` usa Streamlit para apresentar tabela, metricas, graficos e um formulario de previsao.

## Camada de recomendacao

As recomendacoes sao geradas a partir da classe prevista: baixo, medio ou alto risco. O objetivo e apoiar decisoes sobre irrigacao, monitoramento climatico e manejo da plantacao.
