#include <stdlib.h>
#include <stdio.h>

int main(void) {
  float fTemp, cTemp;

  printf("Fahrenheit\t\tCelsius\n");

  for (fTemp = 0; fTemp <= 300; fTemp += 20) {
    cTemp = 5.0 * (fTemp-32.0) / 9.0;

    printf("%10.1f\t%15.1f\n", fTemp, cTemp);
  }

  return EXIT_SUCCESS;
}
