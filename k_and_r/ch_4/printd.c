#include <stdio.h>
#include <stdlib.h>

void printd(int n);

int main(void) {
  printd(123);
  putchar('\n');
  printd(-123);

  return EXIT_SUCCESS;
}


void printd(int n) {
  if (n < 0) {
    putchar('-');
    n = -n;
  }

  if (n / 10)
    printd(n / 10);

  putchar(n % 10 + '0');
}
