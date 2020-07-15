#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

int strcmp_arr(char *s, char *t);
int strcmp_ptr(char *s, char *t);

int strcmp_arr(char *s, char *t) {
  int i;

  for (i = 0; s[i] == t[i]; ++i) {
    if (s[i] == '\0')
      return 0;
  }

  return s[i] - t[i];
}

int strcmp_ptr(char *s, char *t) {
  for (; *s == *t; s++, t++) {
    if (*s == '\0')
      return 0;
  }

  return *s - *t;
}

int main(void) {
  char *s = "abc";
  char *t = "bbc";

  assert(strcmp_arr(s, t) == -1);
  assert(strcmp_arr(t, s) == 1);
  assert(strcmp_arr(s, s) == 0);

  assert(strcmp_ptr(s, t) == -1);
  assert(strcmp_ptr(t, s) == 1);
  assert(strcmp_ptr(s, s) == 0);

  return EXIT_SUCCESS;
}
