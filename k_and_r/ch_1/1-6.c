#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int c;

  while ((c = getchar()) != EOF) {
    printf("The character is %d\n", c);
  }

  printf("The character at EOF is %d\n", c);

  return EXIT_SUCCESS;
}
