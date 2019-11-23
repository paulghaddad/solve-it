#include <stdio.h>

/* Copy input to output, replacing each tab by \t, each backspace by \b and each backslash by \\ */

main() {
  int c;

  while ((c = getchar()) != EOF) {
    if (c == '\t') {
      putchar('\\');
      putchar('t');
    }

    if (c == '\b') {
      putchar('\\');
      putchar('b');
    }

    if (c == '\\') {
      putchar('\\');
      putchar('\\');
    }


    if ((c != '\t') && (c != '\b') && (c != '\\'))
      putchar(c);
  }
}
