#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

int str_length(char *str);

int str_length(char *str) {
  int num_chars = 0;

  while (*str++ != '\0')
    ++num_chars;

  return num_chars;
}

int main(void) {
  assert(str_length("Hello") == 5);
  assert(str_length("") == 0);

  return EXIT_SUCCESS;
}
