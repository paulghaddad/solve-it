#include "resistor_color.h"
#include <stdlib.h>

int color_code(resistor_band_t code) {
  return code;
}

resistor_band_t* colors() {
   resistor_band_t default_colors[] = {
      BLACK, BROWN, RED, ORANGE, YELLOW,
      GREEN, BLUE, VIOLET, GREY, WHITE
   };

   resistor_band_t* colors = malloc(sizeof(resistor_band_t) * 10);

   for (int i = 0; i < 10; i++)
     colors[i] = default_colors[i];

   return colors;
}
