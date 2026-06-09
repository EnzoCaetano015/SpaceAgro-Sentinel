# FIAP - Faculdade de Informatica e Administracao Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="./assets/logo-fiap.png"
       alt="FIAP - Faculdade de Informatica e Administracao Paulista"
       width="40%">
</a>
</p>

<br>

# SpaceAgro Sentinel

## Sistema inteligente de monitoramento agricola com dados espaciais, sensores e Inteligencia Artificial

## Nome do grupo

Projeto individual

## Integrante

- Enzo Caetano Peracio Rodrigues - RM570352

## Professores

### Tutor(a)

- A preencher

### Coordenador(a)

- A preencher

## Descricao do projeto

O SpaceAgro Sentinel e uma POC/MVP desenvolvida para a Global Solution 2026.1 - Space Connect. A solucao usa dados ambientais sinteticos inspirados em dados espaciais, leituras simuladas de sensores ESP32/DHT22 e Machine Learning para classificar o risco agricola de uma regiao.

A proposta responde como a tecnologia espacial pode melhorar processos na Terra: dados de vegetacao, clima e solo ajudam produtores a tomar decisoes mais rapidas sobre irrigacao, monitoramento climatico e manejo da plantacao.

## Problema resolvido

Produtores agricolas dependem de informacoes sobre temperatura, umidade, chuva, solo e saude da vegetacao para evitar desperdicio de agua e perdas de produtividade. Sem analise integrada, a tomada de decisao fica lenta e sujeita a erro.

## Solucao proposta

O projeto gera uma base de dados agricola, analisa os dados com Pandas, cria graficos, treina um modelo de classificacao e disponibiliza um dashboard em Streamlit para prever risco como baixo, medio ou alto. Cada previsao retorna uma recomendacao automatica.

## Tecnologias utilizadas

- Python 3.11+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- CSV
- ESP32 com DHT22 simulado no Wokwi

## Arquitetura da solucao

```text
Dados ambientais simulados + dados de sensor ESP32
                ↓
Arquivos CSV na pasta data/
                ↓
Tratamento e analise com Python/Pandas
                ↓
Geracao de graficos
                ↓
Treinamento de modelo de Machine Learning
                ↓
Classificacao do risco agricola
                ↓
Dashboard em Streamlit
                ↓
Recomendacao automatica ao usuario
```

## Estrutura de pastas

```text
Global-Solution-1/
├── README.md
├── requirements.txt
├── assets/
│   └── logo-fiap.png
├── data/
│   ├── dados_agricolas_espaciais.csv
│   └── dados_sensor_esp32.csv
├── docs/
│   ├── arquitetura.md
│   ├── relatorio_base.md
│   └── imagens/
└── src/
    ├── dashboard.py
    ├── analise_dados.py
    ├── modelo_ml.py
    ├── gerar_dados.py
    ├── utils.py
    └── esp32/
        ├── src/
        │   └── sketch.ino
        ├── diagram.json
        ├── plataformio.ini
        ├── wokwi.toml
        └── README.md
```

## Como executar

Instale as dependencias:

```bash
pip install -r requirements.txt
```

## Como gerar os dados

```bash
python src/gerar_dados.py
```

O comando cria:

- `data/dados_agricolas_espaciais.csv`
- `data/dados_sensor_esp32.csv`

## Como rodar a analise

```bash
python src/analise_dados.py
```

Os graficos serao salvos em `docs/imagens/`.

## Como rodar o modelo de ML

```bash
python src/modelo_ml.py
```

O script treina uma arvore de decisao, exibe a acuracia, mostra o relatorio de classificacao e executa uma previsao de exemplo.

## Como rodar o dashboard

```bash
streamlit run src/dashboard.py
```

O dashboard exibe dados, metricas, graficos e um formulario lateral para prever o risco agricola com valores informados pelo usuario.

## Links e observacoes

- [GitHub](https://github.com/EnzoCaetano015/SpaceAgro-Sentinel).
- Video nao listado: inserir link do video.
- [Protótipo](https://wokwi.com/projects/466302589428580353)

## Historico de lancamentos

* 0.1.0 - 08/06/2026
    * Criacao do MVP SpaceAgro Sentinel com geracao de dados, analise, Machine Learning, dashboard, ESP32 e documentacao base.

---

## Licenca

Este projeto academico segue o modelo FIAP e pode ser utilizado para fins educacionais.
