static const uint8_t  INPUT_PIN  = A0;
static const uint8_t  OUTPUT_PIN = A1;

static const uint16_t SPIKE_DURATION_MSEC = 5;

void setup(void)
{
    Serial.begin(115200);
}

void loop(void)
{
    uint16_t input = analogRead(INPUT_PIN);

    uint16_t freq = input / 10 + 1;

    uint16_t interspike_delay_msec = 1000 * (1 -SPIKE_DURATION_MSEC/1000.f) / freq;

    analogWrite(OUTPUT_PIN, 255);
    delay(SPIKE_DURATION_MSEC);
    analogWrite(OUTPUT_PIN, 0);
    delay(interspike_delay_msec);
}
