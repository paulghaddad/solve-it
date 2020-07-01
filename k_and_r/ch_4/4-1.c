#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 100

int get_line(char line[], int lim);
int strindex(char s[], char pattern[]);

char pattern[] = "ould";

int main(void) {
  char line[MAX_LINE];

  while (get_line(line, MAX_LINE)) {
    int length = strindex(line, pattern);
    if (length)
      printf("%d\n", length);
  }

  return EXIT_SUCCESS;
}


int get_line(char line[], int lim) {
  char c;
  int length = 0;

  while (length < lim && (c = getchar()) != EOF && c != '\n') {
    line[length++] = c;
  }

  if (c == '\n')
    line[length++] = '\n';

  line[length] = '\0';
  return length;
}

int strindex(char s[], char pattern[]) {
  int i, j;

  int start_pos = strlen(s) - strlen(pattern) - 1;
  for (i = start_pos; i >= 0; --i) {
    for (j = 0; pattern[j] != '\0' && s[i+j] == pattern[j]; ++j) {
      ;
    }

    if (j > 0 && pattern[j] == '\0')
      return i;
  }

  return -1;
}
