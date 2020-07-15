#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_STRING 100

void strcat_ptr(char *s, char *t);

// Concatenate t to end of s; s must be big enough
void strcat_ptr(char *s, char *t) {

  // Simpler approach
  while (*s)
    s++;

  while ((*s++ = *t++))
    ;

  /* My initial approach
  for (; *s != '\0'; s++)
    ;

  for (; *t != '\0'; t++, s++) {
    *s = *t;
  }
  */
}

int main(void) {
  char *str = "hello";

  char s[MAX_STRING];

  for (int i = 0; *str != '\0'; ++i) {
    s[i] = *str;
    str++;
  }

  char *t = " world";

  strcat_ptr(s, t);
  assert(strcmp(s, "hello world") == 0);

  return EXIT_SUCCESS;
}
