#include <stdlib.h>
#include <stdio.h>

#define MAX_LINE 100
enum boolean { OUT_OF_WORD, IN_WORD };

int getLine(char s[], int lim);

int main(void) {
  char line[MAX_LINE];
  int lineLength = getLine(line, MAX_LINE);
  printf("The length of the line is %d.\n", lineLength);


  return EXIT_SUCCESS;
}

int getLine(char s[], int lim) {
  int c;

  /* for (i=0; i<lim-1 && (c=getchar()) != EOF && c != '\n'; ++i) { */
  /*   s[i] = c; */
  /* } */

  int i = 0;
  int state = IN_WORD;

  while (state == IN_WORD) {
    if (i >= lim-1)
      state = OUT_OF_WORD;

    c = getchar();

    if (c == EOF)
      state = OUT_OF_WORD;

    if (c == '\n')
      state = OUT_OF_WORD;

    ++i;
  }

  if (c == '\n') {
    s[i] = c;
    ++i;
  }

  s[i] = '\0';
  return i;
}
