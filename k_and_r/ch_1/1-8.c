#include <stdio.h>

/*
 * Count blanks, tabs and newlines.
 * Run with: echo -e "Hello \n\tWorld" | ./1-8
 * */


main() {
  int c, blank, tab, nl;

  blank = 0;
  tab = 0;
  nl = 0;

  while ((c = getchar()) != EOF) {
    if (c == ' ')
      ++blank;

    if (c == '\t')
      ++tab;

    if (c == '\n')
      ++nl;
  }

  printf("Blanks: %d\n", blank);
  printf("Tabs: %d\n", tab);
  printf("Newlines: %d\n", nl);
}
