#include <stdlib.h>
#include <stdio.h>

void deleteSqeeze(char s[], int c);

int main(void) {
  char testString[] = "aeiou\0";
  printf("Testing squeeze with the original string %s and the character %c: \n", testString, 'l');
  deleteSqeeze(testString, 'e');
  printf("%s\n", testString);

  return EXIT_SUCCESS;
}

void deleteSqeeze(char s[], int c) {
  int j = 0;

  for (int i = 0; s[i] != '\0'; ++i) {
    if (s[i] != c) {
      s[j] = s[i];
      ++j;
    }
  }

  s[j] = '\0';
}
