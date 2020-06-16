#include <stdlib.h>
#include <stdio.h>

unsigned bitcount(unsigned x);
unsigned bitcount_faster(unsigned x);
char *bin_string(unsigned short n);

int main(void) {
  unsigned short b = 0x0AAFF;

  /* printf("Bits: %04X - %s\n", b, bin_string(b)); */
  /* printf("Number of bits:   %d\n", bitcount(b)); */

  printf("Start: %04X - %s\n", b, bin_string(b));
  printf("Number of bits:   %d\n", bitcount_faster(b));

  return EXIT_SUCCESS;
}

unsigned bitcount(unsigned x) {
  int b;

  for(b = 0; x != 0; x >>= 1)
    if (x & 01)
      b++;

  return b;
}

unsigned bitcount_faster(unsigned x) {
  int b = 0;

  while (1) {
    if (x &= (x-1)) {
      ++b;
    }

    if (b > 0 && x == 0) {
      ++b;
      break;
    }
  }

  return b;
}

char *bin_string(unsigned short n) {
  static char bin[17];
  int x;

  for (x = 0; x < 16; x++) {
    bin[x] = n & 0x8000 ? '1' : '0';
    n <<= 1;
  }

  bin[16] = '\0';
  return bin;
}
