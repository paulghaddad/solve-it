#include <stdlib.h>
#include <stdio.h>

int lower(int c);

int main(void) {
  printf("Calling lower on %c: %c\n", 'a', lower('a'));
  printf("Calling lower on %c: %c\n", 'A', lower('A'));
}

int lower(int c) {
  return (c >= 'A' && c <= 'Z') ? (c + 'a' - 'A') : c;
}
