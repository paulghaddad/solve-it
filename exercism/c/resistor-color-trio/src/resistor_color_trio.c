#include "resistor_color_trio.h"
#include <math.h>
#include <stdio.h>

resistor_value_t color_code(resistor_band_t* bands) {
  resistor_band_t first_band = bands[0];
  resistor_band_t second_band = bands[1];

  resistor_band_t multiplier = bands[2];

  int resistance = (int) pow(10, multiplier) * (10*first_band + second_band);

  resistor_value_t resistor_value;
  if (resistance > 1000) {
    resistor_value.value = resistance / 1000;
    resistor_value.unit = KILOOHMS;
  } else {
    resistor_value.value = resistance;
    resistor_value.unit = OHMS;
  }

  return resistor_value;
}
