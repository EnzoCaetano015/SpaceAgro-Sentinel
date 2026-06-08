#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  Serial.println("======================================");
  Serial.println("SpaceAgro Sentinel - ESP32 com DHT22");
  Serial.println("Monitoramento ambiental para agricultura inteligente");
  Serial.println("======================================");
}

void loop() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();

  if (isnan(temperatura) || isnan(umidade)) {
    Serial.println("ERRO: Falha ao ler o sensor DHT22");
    delay(2000);
    return;
  }

  Serial.println("Leitura do sensor:");
  
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" C");

  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.println(" %");

  if (temperatura > 32 || umidade < 40) {
    Serial.println("Status: ALERTA");
    Serial.println("Mensagem: Risco climatico elevado para a plantacao");
  } else {
    Serial.println("Status: ESTAVEL");
    Serial.println("Mensagem: Condicao ambiental adequada");
  }

  Serial.println("--------------------------------------");

  delay(3000);
}