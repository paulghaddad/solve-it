#include <stdlib.h>
#include <stdio.h>

unsigned invert(unsigned x, int p, int n);
unsigned invert_solution(unsigned x, int p, int n);
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
  printf("End:   %04X - %s\n", b, bin_string(invert(b, 10, 5)));

  printf("Start: %04X - %s\n", b, bin_string(b));
  printf("End:   %04X - %s\n", b, bin_string(invert_solution(b, 10, 5)));

  return EXIT_SUCCESS;
}

unsigned invert(unsigned x, int p, int n) {
  return x ^ (~0 << p) ^ (~0 << (p+1-n));
}

unsigned invert_solution(unsigned x, int p, int n) {
  return x ^ (~(~0 << n) << (p+1-n));
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
