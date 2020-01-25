#include <stdlib.h>
#include <stdio.h>

float fahrenheitToCelsius(float temp);

int main(void) {
  float fTemp;

  printf("Fahrenheit\t\tCelsius\n");

  for (fTemp = 0; fTemp <= 300; fTemp += 20) {
    printf("%10.1f\t%15.1f\n", fTemp, fahrenheitToCelsius(fTemp));
  }

  return EXIT_SUCCESS;
}

float fahrenheitToCelsius(float temp) {
  float cTemp;
  cTemp = 5.0 * (temp-32.0) / 9.0;

  return cTemp;
}
