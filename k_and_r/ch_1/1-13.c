#include <stdio.h>

/* Print a histogram of the lengths of words in an input. */

#define MAX_WORD_LENGTH 10

main() {
  int c;
  int word_length = 0;

  int word_histogram[MAX_WORD_LENGTH];

  for (int i = 0; i < MAX_WORD_LENGTH; i++)
    word_histogram[i] = 0;

  while ((c = getchar()) != EOF) {
    if (c == '\n') {
      word_histogram[word_length]++;
      word_length = 0;
    } else {
      word_length++;
    }
  }

  for (int i = 0; i < MAX_WORD_LENGTH; i++) {
    printf("%d ", i);
    for (int j = 0; j < word_histogram[i]; j++)
      putchar('*');

    putchar('\n');
  }
}
