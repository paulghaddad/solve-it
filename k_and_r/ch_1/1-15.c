#include <stdio.h>

/* Rewrite the temperature conversion program of Section 1.2 to use a function
 * for conversion. */

float fahr_to_cels(float fahr);

main() {
  float lower = 0.0;
  int upper = 300;
  float step = 20.0;

  printf("Fahrenheit\tCelsius\n");

  for (float fahr = lower; fahr <= upper; fahr += step) {
    printf("%10.1f\t%6.1f\n", fahr, fahr_to_cels(fahr));
  }
}

float fahr_to_cels(float fahr) {
  return 5.0 * (fahr-32.0) / 9.0;
}
