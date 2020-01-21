#include <stdlib.h>
#include <stdio.h>

int main(void) {
  int c;
  int prevChar = 0;

  while ((c = getchar()) != EOF) {
    if (c != ' ' || prevChar != ' ')
      putchar(c);

    prevChar = c;
  }

  return EXIT_SUCCESS;
}
