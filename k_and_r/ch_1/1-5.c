#include <stdlib.h>
#include <stdio.h>


int main(void) {
  printf("Fahrenheit      Celsius\n");

  for (float tempF = 300.0; tempF >= 0; tempF -= 20) {
    float tempC = (5.0/9.0) * (tempF - 32);

    printf("%6.1f\t\t%6.1f\n", tempF, tempC);
  }

  return EXIT_SUCCESS;
}
