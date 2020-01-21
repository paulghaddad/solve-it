#include <stdlib.h>
#include <stdio.h>


int main(void) {
  printf("Press a key: \n");
  printf("The value of EOF is: %d\n", getchar() != EOF);

  return EXIT_SUCCESS;
}
