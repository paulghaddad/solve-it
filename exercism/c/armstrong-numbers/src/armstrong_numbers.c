#include "armstrong_numbers.h"
#include <stdio.h>
#include <math.h>

bool is_armstrong_number(int candidate) {
  if (candidate == 0)
    return true;

  int num_digits = 0;
  while (candidate >= pow(10, num_digits))
    num_digits++;

  int armstrong_sum = 0;
  int base = candidate;
  while (base > 0) {
    int digit = base % 10;
    armstrong_sum += pow(digit, num_digits);
    base /= 10;
  }

  return candidate == armstrong_sum;
}
