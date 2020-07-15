#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

int strend(char* s, char* t);

int strend(char* s, char* t) {
  /* Initial Approach */
  /* int start = strlen(s) - strlen(t); */
  /*  */
  /* for (int i = 0; i < start; ++i) */
  /*   s++; */
  /*  */
  /* while (*t) { */
  /*   if (*t++ != *s++) */
  /*     return 0; */
  /* } */
  /*  */
  /* return 1; */

  char* start_t = t;

  while (*(s+1))
    s++;

  while (*(t+1))
    t++;

  while (t != start_t) {
    if (*s != *t)
      return 0;

    s--;
    t--;
  }

  if (*t == *s)
    return 1;
  else
    return 0;
}

int main(void) {
  char* s1 = "abcdef";
  char* t1 = "def";

  assert(strend(s1, t1) == 1);

  char* s2 = "abcdef";
  char* t2 = "de";

  assert(strend(s2, t2) == 0);

  return EXIT_SUCCESS;
}
