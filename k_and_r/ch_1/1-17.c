#include <stdlib.h>
#include <stdio.h>

#define MAX_LINE 1000
#define LINE_HURDLE 80

int get_line(char line[]);
void print_line(char line[]);

int main(void) {
  int line_length;
  char current_line[MAX_LINE];

  while ((line_length = get_line(current_line)) > 0) {
    if (line_length >= LINE_HURDLE)
      print_line(current_line);
  }

  return EXIT_SUCCESS;
}

int get_line(char line[]) {
  int c;
  int i = 0;

  while ((c = getchar()) != EOF && (c != '\n')) {
    line[i] = c;
    ++i;
  }

  line[i] = '\0';

  return i;
}

void print_line(char line[]) {
  printf("The current line is over 80 characters:\n\t%s", line);
}
