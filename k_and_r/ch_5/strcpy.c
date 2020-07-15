#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 100

void strcpy_arr(char s[], char t[]);
void strcpy_ptr(char *s, char *t);


// copy string t to string s
void strcpy_arr(char s[], char t[]) {
  for (int i = 0; t[i] != '\0'; ++i)
    s[i] = t[i];
}

// copy string t to string s
void strcpy_ptr(char *s, char *t) {
  while (*t != '\0')
    *s++ = *t++;

  *s = '\0';
}

int main(void) {
  // Array subscript version
  char *str1 = "hello, world";
  char buf1[MAX_LENGTH];

  strcpy_arr(buf1, str1);
  assert(strcmp(buf1, "hello, world") == 0);

  // Pointer version
  char *str2 = "hello, world";
  char buf2[MAX_LENGTH];

  strcpy_ptr(buf2, str2);
  assert(strcmp(buf2, "hello, world") == 0);

  return EXIT_SUCCESS;
}
