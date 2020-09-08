#include <stdio.h>
#include <stdlib.h>

#include "roman_numerals.h"

unsigned int arabic_digits[13] = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
char* roman_numerals[13] = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };

char *to_roman_numeral(unsigned int number) {
  char *roman = (char *)malloc(10 * sizeof(char));
  char *output = roman;
  char c;

  if (roman == NULL)
    return NULL;

  while (number > 0) {
    int i;
    for (i = 0; number < arabic_digits[i]; ++i) ;

    char* roman_numeral = roman_numerals[i];
    while ((c = *roman_numeral++) != '\0')
      *output++ = c;

    number -= arabic_digits[i];
  }
  *output = '\0';

  return roman;
}
