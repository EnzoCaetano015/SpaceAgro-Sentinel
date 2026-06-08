#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println("SpaceAgro Sentinel - ESP32 com DHT22");
}

void loop() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();

  if (isnan(temperatura) || isnan(umidade)) {
    Serial.println("Falha ao ler o sensor DHT22");
    delay(2000);
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" C");

  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.println(" %");

  if (temperatura > 32 || umidade < 40) {
    Serial.println("ALERTA: risco climatico elevado");
  } else {
    Serial.println("Condicao ambiental estavel");
  }

  Serial.println("------------------------------");
  delay(3000);
}
