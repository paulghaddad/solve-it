#include <stdlib.h>
#include <stdio.h>

int main(void) {
  float tempC, tempF;

  printf("Celsius  Fahrenheit\n");

  for (tempC = 0; tempC <= 100; tempC += 10) {
    tempF = (9.0/5.0) * tempC + 32;
    printf("%6.1f%10.1f\n", tempC, tempF);
  }

  return EXIT_SUCCESS;
}
