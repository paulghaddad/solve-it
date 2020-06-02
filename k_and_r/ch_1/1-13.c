#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

int main(void) {
  char c;
  int in_word = 0;
  int lengths[20];
  int current_length = 0;

  for (int i = 1; i <= 20; ++i)
    lengths[i] = 0;

  while ((c = getchar()) != EOF) {
    if (!in_word && isalnum(c)) {
      current_length = 1;
      in_word = 1;
    } else if (in_word && !isalnum(c)) {
      lengths[current_length]++;
      in_word = 0;
    } else {
      ++current_length;
    }
  }

  printf("Length\n\n");
  for (int i = 1; i <= 20; ++i) {
    printf("%-8d", i);
    for (int j = 0; j < lengths[i]; ++j)
      printf("*");

    putchar('\n');
  }

  return EXIT_SUCCESS;
}
