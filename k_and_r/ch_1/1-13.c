#include <stdlib.h>
#include <stdio.h>

#define IN_WORD 1
#define OUT_WORD 0

int main(void) {
  int c;
  int length = 0;
  int state = OUT_WORD;

  int wordLengths[15];

  for (int i = 0; i < 15; ++i)
    wordLengths[i] = 0;

  while ((c = getchar()) != EOF) {
    if (state && c >= 'A' && c <= 'z') {
      ++length;
    } else if (!state && c >= 'A' && c <= 'z') {
      state = IN_WORD;
      ++length;
    } else if (state && c == ' ') {
      state = OUT_WORD;
      ++wordLengths[length];
      length = 0;
    }
  }

  for (int i = 1; i < 15; ++i)
    printf("Number of words of length %d: %d\n", i, wordLengths[i]);

  return EXIT_SUCCESS;
}
