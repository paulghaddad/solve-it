/* Write the function htoi(s) which converts a string of hexadecimal digits
 * (including an optional 0x or 0X) into its equivalent integer values. The
 * allowable digits are 0 through 9, a through f, and A through F. */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int htoi(char s[]);

int main() {
  printf("The integer value of %s is %d and expected value is %d\n", "ae0f\0", htoi("ae0f\0"), 0xae0f);
  printf("The integer value of %s is %d and expected value is %d\n", "0xae0f", htoi("0xae0f"), 0xae0f);
  printf("The integer value of %s is %d and expected value is %d\n", "0XAE0F", htoi("0XAE0F"), 0xae0f);
  printf("The integer value of %s is %d and expected value is %d\n", "2x", htoi("2x"), -1);

  return EXIT_SUCCESS;
}

int htoi(char hexValue[]) {
  double decimalValue = 0;
  int i;

  if (tolower(hexValue[0]) == '0' && tolower(hexValue[1]) == 'x') {
    i = 2;
  } else {
    i = 0;
  }

  char digit;

  while ((digit = tolower(hexValue[i]))) {
    decimalValue *= 16;

    if (isdigit(digit)) {
      decimalValue += (digit - '0');
    } else if (isalpha(digit) && digit >= 'a' && digit <= 'f') {
      decimalValue += (digit - 'a' + 10);
    } else {
      return -1;
    }

    ++i;
  }

  return decimalValue;
}
