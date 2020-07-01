#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 100

int get_line(char line[], int lim);
int strrindex(char s[], char pattern[]);

int main(void) {
  assert(strrindex("funkfunk", "unk") == 5);

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

int strrindex(char s[], char pattern[]) {
  int i, j;

  int start_pos = strlen(s) - strlen(pattern);
  for (i = start_pos; i >= 0; --i) {
    for (j = 0; pattern[j] != '\0' && s[i+j] == pattern[j]; ++j) {
      ;
    }

    if (j > 0 && pattern[j] == '\0')
      return i;
  }

  return -1;
}
