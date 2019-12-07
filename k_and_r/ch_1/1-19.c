#include <stdio.h>
#define MAXLINE 1000

/* Write a function reverse(s) that reverses the character string s. Use it to
 * write a program that reverses each line of a file. */

int get_line(char line[], int maxline);
void reverse(char line[], char reversed_line[]);

main() {
  int len;
  char line[MAXLINE];
  char reversed_line[MAXLINE];

  while ((len = get_line(line, MAXLINE)) > 0) {
    reverse(line, reversed_line);
    printf("%s\n", reversed_line);
  }
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

void reverse(char line[], char reversed_line[]) {
  int i;
  int j = 0;
  char c;
  int line_length = 0;

  for (i = 0; line[i] != '\0'; ++i)
    line_length++;


  for (i = line_length-1; i >= 0; --i) {
    if (line[i] != '\n') {
      reversed_line[j] = line[i];
      ++j;
    }

    reversed_line[j] = '\0';
  }
}
