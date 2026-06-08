# Simulacao ESP32 - SpaceAgro Sentinel

Esta pasta contem um sketch para simular a leitura de temperatura e umidade com ESP32 e sensor DHT22 no Wokwi.

## Objetivo

Coletar dados ambientais basicos que podem apoiar a classificacao de risco agricola usada pelo SpaceAgro Sentinel.

## Componentes

- ESP32 DevKit
- Sensor DHT22
- Cabos jumper virtuais no Wokwi

## Como abrir no Wokwi

1. Acesse https://wokwi.com/.
2. Crie um novo projeto com ESP32.
3. Adicione o sensor DHT22.
4. Conecte o pino de dados do DHT22 ao GPIO 15.
5. Copie o conteudo de `sketch.ino` para o editor.
6. Execute a simulacao.

## Interpretacao

O Monitor Serial exibe temperatura e umidade. Quando a temperatura passa de 32 C ou a umidade fica abaixo de 40%, o sistema mostra o alerta de risco climatico elevado.
