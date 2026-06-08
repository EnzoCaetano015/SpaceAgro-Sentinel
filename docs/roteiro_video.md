# Roteiro de Video - SpaceAgro Sentinel

QUERO CONCORRER

## 1. Abertura

Apresentar a Global Solution 2026.1 - Space Connect, o nome do projeto SpaceAgro Sentinel e o integrante Enzo Caetano Peracio Rodrigues - RM570352.

## 2. Problema

Explicar que produtores rurais precisam tomar decisoes rapidas sobre irrigacao, clima e manejo, mas muitas vezes nao possuem analise integrada de dados.

## 3. Solucao

Apresentar a proposta: usar dados ambientais inspirados em dados espaciais, leituras de sensores ESP32 e Inteligencia Artificial para classificar risco agricola.

## 4. Arquitetura

Mostrar o fluxo: dados ambientais + ESP32 -> CSV -> Pandas -> Machine Learning -> Dashboard -> recomendacao.

## 5. Demonstracao do CSV

Abrir `data/dados_agricolas_espaciais.csv` e mostrar as colunas data, regiao, temperatura, umidade, chuva, ndvi, ph_solo e risco.

## 6. Demonstracao dos graficos

Executar `python src/analise_dados.py` e mostrar os graficos gerados em `docs/imagens/`.

## 7. Demonstracao do modelo de IA

Executar `python src/modelo_ml.py`, mostrar a acuracia, o relatorio de classificacao e o exemplo de previsao.

## 8. Demonstracao do dashboard

Executar `streamlit run src/dashboard.py`, mostrar metricas, tabela, graficos e formulario de previsao.

## 9. Demonstracao do ESP32/Wokwi

Abrir o Wokwi, executar o sketch do ESP32 com DHT22 e mostrar o Monitor Serial com temperatura, umidade e alerta.

## 10. Encerramento

Concluir reforcando que a tecnologia espacial, sensores e IA podem melhorar decisoes no campo, reduzir desperdicio de agua e criar novas oportunidades na agricultura.
