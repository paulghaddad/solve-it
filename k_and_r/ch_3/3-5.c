#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_STRING 100

void itob(int n, char s[], int b);
void reverse(char s[]);


void itob(int n, char s[], int b) {
  int i = 0;

  do {
    int digit = n % b;

    if (digit > 9)
      s[i++] = digit - 10 + 'A';
    else
      s[i++] = digit + '0';
  } while ((n /= b) > 0);


  s[i] = '\0';

  reverse(s);
}

void reverse(char s[]) {
  int len = strlen(s);

  for (int i = 0; i <= len / 2; ++i) {
    char tmp = s[i];
    s[i] = s[len-1-i];
    s[len-1-i] = tmp;
  }
}


int main(void) {
  char buf1[MAX_STRING], conv1[] = "11001";

  itob(25, buf1, 2);
  assert(strcmp(buf1, conv1) == 0);

  char buf2[MAX_STRING], conv2[] = "3E8";

  itob(1000, buf2, 16);
  assert(strcmp(buf2, conv2) == 0);

  return EXIT_SUCCESS;
}
