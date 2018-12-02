/*
Simple spike generator

Copyright (C) Simon D. Levy 2018

This file is part of csci252-examples.

csci252-examples is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
*/

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
