#include <stdlib.h>
#include <stdio.h>

unsigned setbits(unsigned x, int p, int n, int y);
char *bin_string(unsigned short n);

int main(void) {
  /* unsigned short v = 0xFFFF; */
  /* unsigned short a = 0x00F0; */
  unsigned short b = 0x0AAFF;

  /* printf("Start: %04X - %s\n", v, bin_string(v)); */
  /* printf("Start: %04X - %s\n", a, bin_string(a)); */
  /* printf("Start with ~A: %04X - %s\n", a, bin_string(~a)); */
  /* printf("Start with -A: %04X - %s\n", a, bin_string(-a)); */
  /* printf("Start with B: %04X - %s\n", b, bin_string(b)); */
  /* printf("A | B: %s\n", bin_string(a|b)); */
  /* printf("A & B: %s\n", bin_string(a&b)); */
  /* printf("A ^ B: %s\n", bin_string(a^b)); */

  printf("Start: %04X - %s\n", b, bin_string(b));

  return EXIT_SUCCESS;
}

unsigned setbits(unsigned x, int p, int n, int y) {
  return x;
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
