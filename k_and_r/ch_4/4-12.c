#include <stdio.h>
#include <stdlib.h>

#define MAX_DIGITS 100

void itoa_rec(int n, char s[]);

int main(void) {
  char buf1[MAX_DIGITS];
  char buf2[MAX_DIGITS];

  itoa_rec(123, buf1);
  printf("%s\n", buf1);

  itoa_rec(-123, buf2);
  printf("%s\n", buf2);

  return EXIT_SUCCESS;
}

int i = 0;

void itoa_rec(int n, char s[]) {
  if (n < 0) {
    s[i++] = '-';
    n *= -1;
  }

  if (n / 10)
    itoa_rec(n/10, s);

  s[i++] = n % 10 + '0';

  s[i] = '\0';
}
