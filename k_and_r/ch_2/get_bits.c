#include <stdlib.h>
#include <stdio.h>

unsigned getbits(unsigned x, int p, int n);

int main(void) {
  printf("%d", getbits(16, 4, 3));

  return EXIT_SUCCESS;
}

unsigned getbits(unsigned x, int p, int n) {
  return (x >> (p+1-n)) & ~(~0 << n);
}
