#include <stdio.h>

/* Print the input one word per line. */

main() {
  int c, prev_c;

  while ((c = getchar()) != EOF) {
    if (c == ' ' || c == '\n' || c == '\t') {
      if (prev_c != ' ' && prev_c != '\n' && prev_c != '\t')
        putchar('\n');
    }
    else
      putchar(c);

    prev_c = c;
  }
}
