# Simulacao ESP32 - SpaceAgro Sentinel

Esta pasta contem um sketch para simular a leitura de temperatura e umidade com ESP32 e sensor DHT22 no Wokwi.

## Objetivo

Coletar dados ambientais basicos que podem apoiar a classificacao de risco agricola usada pelo SpaceAgro Sentinel.

## Componentes

- ESP32 DevKit
- Sensor DHT22
- Cabos jumper virtuais no Wokwi

## Como abrir no Wokwi

Acesse https://wokwi.com/projects/466302589428580353.

## Interpretacao

O Monitor Serial exibe temperatura e umidade. Quando a temperatura passa de 32 C ou a umidade fica abaixo de 40%, o sistema mostra o alerta de risco climatico elevado.
