#include <stdlib.h>
#include <stdio.h>


int main(void) {
  int c;
  long line_count = 0;
  long tab_count = 0;
  long blank_count = 0;

  while ((c = getchar()) != EOF) {
    putchar(c);
    if (c == '\n') 
      ++line_count;
    else if (c == '\t')
      ++tab_count;
    else if (c == ' ')
      ++blank_count;

  }

  printf("There are %ld newlines, %ld tabs and %ld spaces", line_count, tab_count, blank_count);


  return EXIT_SUCCESS;
}
