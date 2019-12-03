#include <stdio.h>

/* Ex.1-4 - Print the corresponding Celsius to Fahrenheit Table*/

int main() {
  float fahr, celsius;
  int lower, upper, step;

  lower = 0;
  upper = 300;
  step = 20;

  celsius = lower;

  printf("Celsius  Fahrenheit\n");
  while (celsius <= upper) {
    fahr = celsius * (9.0/5.0) + 32.0;
    printf("%10.0f   %5.1f\n", celsius, fahr);
    celsius += step;
  }

  return 1;
}
