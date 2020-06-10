#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define base 16

int htoi(char hex[]);

int main(void) {
  printf("Converting %s to decimal: %d\n", "0", htoi("0"));
  printf("Converting %s to decimal: %d\n", "16", htoi("16"));
  printf("Converting %s to decimal: %d\n", "4af", htoi("4af"));
  printf("Converting %s to decimal: %d\n", "4AF", htoi("4AF"));
  printf("Converting %s to decimal: %d\n", "0x4af", htoi("0x4af"));
  printf("Converting %s to decimal: %d\n", "0X4af", htoi("0X4af"));

  return EXIT_SUCCESS;
}


int htoi(char hex[]) {
  int num_digits = strlen(hex);
  int int_value = 0, i = 0;
  int digit, ch;

  // Optional preceding 0x or 0X
  if (hex[0] == '0' && tolower(hex[1]) == 'x')
    i = 2;

  for (; i < num_digits; ++i) {
    ch = hex[i];

    // Ensure digit is between 0-f
    if (!isxdigit(ch))
      exit(1);

    if (isdigit(ch))
      digit = ch - '0';
    else
      digit = tolower(ch) - 'a' + 10;

    // Using multiplication
    /* int_value = int_value*16 + digit; */
    int_value = (int_value<<4) + digit;
  }

  return int_value;
}
