#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void reverse(char str[], int start, int end);

void reverse(char str[], int start, int end) {
  if (end <= start)
    return;

  char tmp = str[start];
  str[start] = str[end];
  str[end] = tmp;

  reverse(str, ++start, --end);
}


int main(void) {
  char str1[] = "abcde";
  char str2[] = "abcd";
  char str3[] = "";

  reverse(str1, 0, strlen(str1)-1);
  reverse(str2, 0, strlen(str2)-1);
  reverse(str3, 0, strlen(str3)-1);

  assert(strcmp(str1, "edcba") == 0);
  assert(strcmp(str2, "dcba") == 0);
  assert(strcmp(str3, "") == 0);

  return EXIT_SUCCESS;
}
