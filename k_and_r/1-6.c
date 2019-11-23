#include <stdio.h>

main() {
  int c; // declare as C to handle chars as well as EOF

  while ((c = getchar()) != EOF)
    putchar(c);

  printf("%d\n", c != EOF); // Verify EOF is 0
}
