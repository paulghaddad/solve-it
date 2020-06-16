#include <stdlib.h>
#include <stdio.h>

int lower(char c);

int main(void) {
  printf("Calling lower on %c: %c\n", 'a', lower('a'));
  printf("Calling lower on %c: %c\n", 'A', lower('A'));
}

int lower(char c) {
  return (c >= 'A' && c <= 'Z') ? c - ('A' - 'a') : c;
}
