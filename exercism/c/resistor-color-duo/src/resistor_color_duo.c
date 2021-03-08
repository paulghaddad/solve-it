#include "resistor_color_duo.h"

int color_code(resistor_band_t* bands) {
  return 10*bands[0] + bands[1];
}
