#include <stdio.h>
#define MAXLINE 1000
#define MINLINE 80

/* Write a program to print all input lines that are longer than MINLINE characters
 * */

int get_line(char line[], int maxline);

main() {
  int len;
  char line[MAXLINE];

  while ((len = get_line(line, MAXLINE)) > 0)
    if (len > MINLINE)
      printf("The line %s has more than %d characters\n", line, MINLINE);
}

int get_line(char s[], int lim) {
  int c, i;

  for (i = 0; i< lim-1 && (c=getchar()) != EOF && c != '\n'; ++i)
    s[i] = c;

  if (c == '\n') {
    s[i] = c; 
    ++i;
  }

  s[i] = '\0';
  return i;
}
