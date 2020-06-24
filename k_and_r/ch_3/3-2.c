#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void escape(char s[], char t[]);
void unescape(char s[], char t[]);

int main(void) {
  char t[] = "hello\t world\n";
  size_t string_length = strlen(t)*2;
  char s[string_length+1];

  escape(s, t);

  printf("Calling escape on %s results in %s\n", t, s);

  char v[string_length+1];

  unescape(v, s);

  printf("Calling unescape on %s results in %s\n", s, v);

  return EXIT_SUCCESS;
}

void escape(char s[], char t[]) {
  char c;
  int i;

  for (i = 0; t[i] != '\0'; ++i) {
    c = t[i];

    switch(c) {
      case '\n':
        s[i++] = '\\';
        s[i] = 'n';
        break;
      case '\t':
        s[i++] = '\\';
        s[i] = 't';
        break;
      default:
        s[i] = c;
    }
  }

  s[i] = '\0';
}

void unescape(char s[], char t[]) {
  char c;
  int i, j, next;

  for (i = j = 0; i < strlen(t); ++i) {
    c = t[i];
    next = t[i+1];

    if (c == '\\' && next == 'n') {
      s[j] = '\n';
      ++i;
    } else if (c == '\\' && next == 't'){
      s[j] = '\t';
      ++i;
    } else {
      s[j] = c;
    }

    ++j;
  }

  s[j] = '\0';
}
