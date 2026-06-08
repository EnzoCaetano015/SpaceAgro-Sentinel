# SpaceAgro Sentinel

## Integrante

Enzo Caetano Peracio Rodrigues - RM570352

## Introducao

Inserir uma apresentacao do contexto da Global Solution 2026.1 - Space Connect e da relacao entre tecnologia espacial e agricultura.

## Desenvolvimento

Descrever a construcao da POC, os scripts Python, a base sintetica, a analise de dados, o modelo de Machine Learning, o dashboard e a simulacao do ESP32.

## Arquitetura da Solucao

Fluxo: dados ambientais + ESP32 -> CSV -> Pandas -> Machine Learning -> Dashboard -> recomendacao.

## Base de Dados

Explicar as colunas da base principal:

- data
- regiao
- temperatura
- umidade
- chuva
- ndvi
- ph_solo
- risco

Inserir link ou imagem da base de dados, se necessario.

## Analise de Dados

Inserir imagens dos graficos gerados em `docs/imagens/`.

## Machine Learning

Descrever o uso do `DecisionTreeClassifier`, as variaveis de entrada e a previsao da classe de risco.

## ESP32 e Sensores

Inserir print da simulacao Wokwi e explicar a leitura do sensor DHT22.

## Dashboard

Inserir prints do dashboard Streamlit com metricas, graficos e previsao manual.

## Resultados Esperados

O sistema deve apoiar a tomada de decisao agricola, indicando baixo, medio ou alto risco e exibindo uma recomendacao automatica.

## Conclusao

Apresentar os aprendizados, beneficios da solucao e possiveis evolucoes futuras, como integracao com APIs reais de satelite e sensores fisicos.

## Links

- GitHub: inserir link do repositorio
- Video nao listado: inserir link do video
- Wokwi: inserir link da simulacao
