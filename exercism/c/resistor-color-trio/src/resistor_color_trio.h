#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

#define OHMS "ohms"
#define KILOOHMS "kiloohms"

typedef struct {
  int value;
  char* unit;
} resistor_value_t;

typedef enum {
  BLACK,
  BROWN,
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  VIOLET,
  GREY,
  WHITE,
} resistor_band_t;

resistor_value_t color_code(resistor_band_t* bands);

#endif
