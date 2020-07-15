#include <stdlib.h>
#include <stdio.h>

/* Using array indexing */

int main_alt(int argc, char *argv[]) {
  int i;

  for (i = 1; i < argc; i++)
    printf("%s%s", argv[i], (i < argc-1) ? " " : "");

  printf("\n");

  return EXIT_SUCCESS;
}

/* Using pointer manipulation */

int main(int argc, char *argv[]) {
  while (--argc > 0)
    printf((argc > 1) ? "%s " : "%s", *++argv);

  printf("\n");

  return EXIT_SUCCESS;
}
