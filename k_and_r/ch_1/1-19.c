#include <stdlib.h>
#include <stdio.h>

#define MAX_LINE 100

void reverse(char originalString[], char reversedString[]);

int main(void) {
  char string[MAX_LINE] = "The Ohio State Buckeyes\0";
  char reversedString[MAX_LINE];

  reverse(string, reversedString);

  printf("The reversed string is:  %s\n", reversedString);

  return EXIT_SUCCESS;
}

void reverse(char originalString[], char reversedString[]) {
  int length = 0;
  while (originalString[length] != '\0') {
    ++length;
  }

  int j = length;
  for (int i = 0; i < length; ++i) {
    reversedString[i] = originalString[j-1];
    --j;
  }

  reversedString[length] = '\0';
}
