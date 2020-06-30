#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

double atofloat(char s[]);

int main(void) {
  /* assert(atofloat("123.4") == 123.4); */
  assert(atofloat("123.45e6") == 123.45e6);
  /* assert(atofloat("123.45e-6") == 123.45e-6); */
}

double atofloat(char s[]) {
  double val, power, exponent;
  int i, sign;

  for (i = 0; isspace(s[i]); i++)
    ;

  sign = (s[i] == '-') ? -1 : 1;

  if (s[i] == '+' || s[i] == '-')
    i++;

  for (val = 0.0; isdigit(s[i]); i++)
    val = 10.0 * val + (s[i] - '0');

  if (s[i] == '.')
    i++;

  for (power = 1.0; isdigit(s[i]); i++) {
    val = 10.0 * val + (s[i] - '0');
    power *= 10.0;
  }

  if (s[i] == 'e' || s[i] == 'E')
    i++;

  exponent = (s[i] == '-') ? 

  for (exponent = 0.0; isdigit(s[i]); i++) {
    exponent = 10.0 * exponent + (s[i] - '0');
  }

  if (exponent > 0)
    val *= pow(10, exponent);

  return sign * val / power;
}
