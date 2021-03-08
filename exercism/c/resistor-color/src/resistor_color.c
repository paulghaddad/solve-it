#include "resistor_color.h"

int color_code(resistor_band_t code) {
  return code;
}

resistor_band_t* colors() {
   static resistor_band_t colors[] = {
      BLACK, BROWN, RED, ORANGE, YELLOW,
      GREEN, BLUE, VIOLET, GREY, WHITE
   };

   return colors;
}
