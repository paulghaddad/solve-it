#include <stdlib.h>
#include <stdio.h>

#define MAX_LINE 1000

int main (void) {
  enum { OUT_STRING, IN_STRING };

  int i = 0;
  char c;
  int lim = MAX_LINE;
  char s[MAX_LINE];
  int process_string = IN_STRING;

  while (process_string) {
    if (i >= lim) {
      process_string = OUT_STRING;
    }

    c = getchar();

    if (c == '\n') {
      process_string = OUT_STRING;
    } else if (c == EOF) {
      process_string = OUT_STRING;
    } else {
      s[i] = c;
    }

    ++i;
  }

  printf("The string is: %s\n", s);

  return EXIT_SUCCESS;
}
