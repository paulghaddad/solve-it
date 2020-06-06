#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void print_line(char line[]);
int get_line(char line[]);
void remove_trail_spaces(char line[]);

int MAX_LINE = 1000;

int main(void) {
  char line[MAX_LINE];

  while (get_line(line) > 0) {
    remove_trail_spaces(line);

    if (strlen(line) > 0) {
      printf("The current line is %ld characters: ", strlen(line));
      print_line(line);
      putchar('\n');
    }
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

  if (c == '\n') {
    line[i] = c;
    ++i;
  }

  line[i] = '\0';

  return i;
}

void print_line(char line[]) {
  printf("%s", line);
}

void remove_trail_spaces(char line[]) {
    int last_char = 0;
    for (int i = 0; line[i] != '\0'; ++i) {
      if (line[i] != ' ' && line[i] != '\n')
        last_char = i;
    }

    if (last_char > 0) {
      line[++last_char] = '\0';
    } else {
      line[0] = '\0';
    }
}
