#include <stdio.h>
#include <stdlib.h>

#include "roman_numerals.h"

char *to_roman_numeral(unsigned int number) {
  char *roman = (char *)malloc(10 * sizeof(char));
  if (roman == NULL) {
    return NULL;
  }

  int i = 0;
  while (number > 0) {
    if (number >= 1000) {
      *(roman+i) = 'M';
      number -= 1000;
      i++;
    }
    else if (number >= 900) {
      *(roman+i) = 'C';
      *(roman+i+1) = 'M';
      number -= 900;
      i += 2;
    }
    else if (number >= 500) {
      *(roman+i) = 'D';
      number -= 500;
      i++;
    }
    else if (number >= 400) {
      *(roman+i) = 'C';
      *(roman+i+1) = 'D';
      number -= 400;
      i += 2;
    }
    else if (number >= 100) {
      *(roman+i) = 'C';
      number -= 100;
      i++;
    }
    else if (number >= 90) {
      *(roman+i) = 'X';
      *(roman+i+1) = 'C';
      number -= 90;
      i += 2;
    }
    else if (number >= 50) {
      *(roman+i) = 'L';
      number -= 50;
      i++;
    }
    else if (number >= 40) {
      *(roman+i) = 'X';
      *(roman+i+1) = 'L';
      number -= 40;
      i += 2;
    }
    else if (number >= 10) {
      *(roman+i) = 'X';
      number -= 10;
      i++;
    }
    else if (number == 9) {
      *(roman+i) = 'I';
      *(roman+i+1) = 'X';
      number -= 9;
      i += 2;
    }
    else if (number >= 5) {
      *(roman+i) = 'V';
      number -= 5;
      i++;
    }
    else if (number == 4) {
      *(roman+i) = 'I';
      *(roman+i+1) = 'V';
      number -= 4;
      i += 2;
    }
    else if (number % 1 == 0) {
      *(roman+i) = 'I';
      number--;
      i++;
    }
  }

  *(roman+i) = '\0';

  return roman;
}
