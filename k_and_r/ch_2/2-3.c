/* Write the function htoi(s) which converts a string of hexadecimal digits
 * (including an optional 0x or 0X) into its equivalent integer values. The
 * allowable digits are 0 through 9, a through f, and A through F. */

#include <stdio.h>
#include <ctype.h>

int htoi(char s[]);

int main() {
  printf("The integer value of %s is %d and expected value is %d\n", "ae0f", htoi("ae0f"), 0xae0f);
  printf("The integer value of %s is %d and expected value is %d\n", "0xae0f", htoi("0xae0f"), 0xae0f);
  printf("The integer value of %s is %d and expected value is %d\n", "0XAE0F", htoi("0XAE0F"), 0xae0f);
  printf("The integer value of %s is %d and expected value is %d\n", "2x", htoi("2x"), -1);

  return 0;
}

int htoi(char *hex) {
  int value = 0;
  char c;

  while ((c = tolower(*hex++)) != '\0') {
    value <<= 4; // Equivalent to multiplying the value by 2^4 = 16

    if (c == 'x' && value == 0)
      continue;

    if (c >= '0' && c <= '9') {
      value += (c - '0');
    } else if (c >= 'a' && c <= 'f') {
      value += (c - 'a' + 10);
    } else
      return -1;

  }

  return value;
}
