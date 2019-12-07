#include <stdio.h>
#define MAXLINE 1000

/* Revise the main routine of the longest-line program so it will correctly
 * print the length of arbitrarily long input lines, and as much as possible of
 * the text.
 */

int get_line(char line[], int maxline);
void copy(char to[], char from[]);

main() {
  int len;
  int max;
  char line[MAXLINE];
  char longest[MAXLINE];

  max = 0;
  while ((len = get_line(line, MAXLINE)) > 0)
    printf("The length of line %s is %d\n", line, len);
    if (len > max) {
      max = len;
      copy(longest, line);
    }

  if (max > 0)
    printf("%s", longest);

  return 0;
}

// Adding an underscore to the name to not conflict with stdio version
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

void copy(char to[], char from[]) {
  int i;

  i = 0;
  while ((to[i] = from[i]) != '\0')
    ++i;
}
