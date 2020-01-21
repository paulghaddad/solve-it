#include <stdlib.h>
#include <stdio.h>

int main(void) {
  int newlines = 0;
  int blanks = 0;
  int tabs = 0;
  int c;

  while ((c = getchar()) != EOF) {
    if (c == '\n')
      ++newlines;
    else if (c == 't')
      ++tabs;
    else if (c == ' ')
      ++blanks;
  }

  printf("There are %d newlines, %d blanks, and %d tabs in the input\n", newlines, blanks, tabs);

  return EXIT_SUCCESS;
}
