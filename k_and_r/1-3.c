#include <stdio.h>

/* Ex.1-3 - Print a header above the temperature conversion program */

int main() {
  float fahr, celsius;
  int lower, upper, step;

  lower = 0;
  upper = 300;
  step = 20;

  fahr = lower;

  printf("Fahrenheit   Celsius\n");
  while (fahr <= upper) {
    celsius = (5.0/9.0) * (fahr - 32.0);
    printf("%10.0f   %5.1f\n", fahr, celsius);
    fahr += step;
  }

  return 1;
}
