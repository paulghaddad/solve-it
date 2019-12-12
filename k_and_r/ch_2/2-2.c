/* Write a loop equivalent to the for loop above without using && or ||. */

#include <stdio.h>
#define MAXLINE 1000

int get_line(char line[], int maxline);

int main() {
  int len;
  char line[MAXLINE];

  while ((len = get_line(line, MAXLINE)) > 0)
    printf("The line is %s\n", line);

  return 0;
}

int get_line(char s[], int lim) {
  int c;
  int i = 0;

  while (i < lim-1) {
    c = getchar();

    if (c == EOF)
      break;
    else if (c == '\n')
      break;

    s[i] = c;
    ++i;
  }

  if (c == '\n') {
    s[i] = c;
    ++i;
  }

  s[i] = '\0';
  return i;
}
