#include <stdio.h>

/* Copy input to output, replacing each string of one or more blanks by a single
 * blank. */

main() {
  int c, prev_c;

  while ((c = getchar()) != EOF) {
    if (!(c == ' ' && c == prev_c))
      putchar(c);

    prev_c = c;
  }
}
