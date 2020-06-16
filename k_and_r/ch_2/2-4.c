#include <stdlib.h>
#include <stdio.h>

void squeeze(char s1[], char s2[]);

int main(void) {
  char s1[] = "abcde";
  char s2[] = "abc";
  squeeze(s1, s2);
  printf("Calling squeeze on abcde with s2 abc results in %s.\n", s1);

  return EXIT_SUCCESS;
}

#define FALSE 0
#define TRUE 1

void squeeze(char s1[], char s2[]) {
  int i = 0, k = 0;

  while (s1[i++] != '\0') {
    int j = 0;
    int matching_char = FALSE;

    while (s2[j] != '\0') {
      if (s1[i] == s2[j++]) {
        matching_char = TRUE;
        break;
      }
    }

    if (!matching_char)
      s1[k++] = s1[i];
  }

  s1[k] = '\0';
}
