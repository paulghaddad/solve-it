#include <stdlib.h>
#include <stdio.h>

#define IN_WORD 1
#define WORD_BOUNDARY 0

int main(void) {
  int c;
  int state = WORD_BOUNDARY;

  while ((c = getchar()) != EOF) {
    if (!state && c >= 'A' && c <= 'z') {
      putchar(c);
      state = IN_WORD;
    } else if (state && c >= 'A' && c <= 'z') {
      putchar(c);
    } else {
      state = WORD_BOUNDARY;
      putchar('\n');
    }
  }

  return EXIT_SUCCESS;
}
