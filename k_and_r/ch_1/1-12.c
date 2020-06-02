#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

#define OUT_WORD 0
#define IN_WORD 1

int main(void) {
  int state = OUT_WORD;
  int c;

  while ((c = getchar()) != EOF) {
    if ((state == IN_WORD) && (c == '\n' || c == '\t' || c == ' ')) {
      state = OUT_WORD;
      printf("\n");
    } else if (state == OUT_WORD && isalnum(c)) {
      state = IN_WORD;
      putchar(c);
    } else
      putchar(c);
  }

  return EXIT_SUCCESS;
}
