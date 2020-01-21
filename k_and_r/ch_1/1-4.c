#include <stdlib.h>
#include <stdio.h>

int main(void) {
  float cTemp = 0, fTemp;

  printf("Celsius\t\tFahrenheit\n");

  while (cTemp <= 150) {
    fTemp = cTemp * 1.8 + 32;
    printf("%7.1f\t%15.1f\n", cTemp, fTemp);
    cTemp += 20;
  }

  return EXIT_SUCCESS;
}
