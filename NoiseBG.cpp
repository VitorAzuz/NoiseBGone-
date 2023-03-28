const int pinMicrofone = A0; // define o pino analógico do microfone
int valorLeitura = 0; // variável para armazenar a leitura analógica

void setup() {
    Serial.begin(9600); // inicia a comunicação serial para monitorar a leitura
}

void loop() {
    valorLeitura = analogRead(pinMicrofone); // lê o valor analógico do microfone
    Serial.println(valorLeitura); // imprime o valor da leitura na porta serial
    delay(10); // aguarda 10 milissegundos para a próxima leitura
}