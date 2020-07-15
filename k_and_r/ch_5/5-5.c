#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define BUF_SIZE 50

void mystrncpy(char *s, char *t, int n);
void mystrncat(char *s, char *t, int n);
int mystrncmp(char *cs, char *ct, int n);

void mystrncpy(char *s, char *t, int n) {
  while (*t && n > 0) {
    *s++ = *t++;
    --n;
  }


  while (n > 0) {
    *s++ = '\0';
    --n;
  }
}

void mystrncat(char *s, char *t, int n) {

  while (*s) {
    s++;
  }

  while ((*s = *t) && n-- > 0) {
    s++;
    t++;
  }

  *s = '\0';
}

int mystrncmp(char *cs, char *ct, int n) {
  while (*cs == *ct && n-- > 0) {
    cs++;
    ct++;
  }

  if (*ct && *cs == '\0')
    return 0;

  return *cs - *ct;
}

int main(void) {
  char buf1[BUF_SIZE];
  char *t1 = "hello world";
  mystrncpy(buf1, t1, 5);

  assert(strcmp(buf1, "hello") == 0);

  char *str = "hello";

  char buf2[BUF_SIZE];

  for (int i = 0; *str != '\0'; ++i)
    buf2[i] = *str++;


  char *t2 = " world";
  mystrncat(buf2, t2, 3);

  assert(strcmp(buf2, "hello wo") == 0);

  char *t3 = "hello world";
  char *t4 = "hab";
  char *t5 = "hhb";

  assert(mystrncmp(t1, t3, 4) == 0);
  assert(mystrncmp(t1, t4, 4) == 4);
  assert(mystrncmp(t1, t5, 4) == -3);
  assert(mystrncmp("hel", t3, 8) == 0);

  return EXIT_SUCCESS;
}
