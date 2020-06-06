#include <stdlib.h>
#include <stdio.h>

float f_to_c(float fahrenheit);

int main(void) {
  float celsius;

  float lower = 0;
  float upper = 300.0;

  for (float fahr = lower; fahr <= upper; fahr += 20) {
    celsius = f_to_c(fahr);
    printf("%.2f\t%.2f\n", fahr, celsius);
  }

  return EXIT_SUCCESS;
}

float f_to_c(float fahrenheit) {
  return 5.0 * (fahrenheit-32.0) / 9.0;
}
