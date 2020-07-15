#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

#define SIZE 10

int getch(void);
void ungetch(int);

int getint(int *pn);

int main(void) {
  int n, array[SIZE];

  for (n = 0; n < SIZE && getint(&array[n]) != EOF; n++)
    ;

  printf("The number is: %d", array[0]);

  return EXIT_SUCCESS;
}

int getint(int *pn) {
  int c, d, sign;

  while (isspace(c = getch()))
    ;

  if (!isdigit(c) && c != EOF && c != '+' && c != '-') {
    ungetch(c); // it's not a number
    return 0;
  }

  sign = (c == '-') ? -1 : 1;
  printf("sign %d\n", sign);

  if (c == '+' || c == '-') {
    d = c;

    if (!isdigit(c = getch())) {
      if (c != EOF)
        ungetch(c);

      ungetch(d);
      return d;
    }
  }


  for (*pn = 0; isdigit(c); c = getch())
    *pn = 10 * *pn + (c - '0');

  *pn *= sign;

  if (c != EOF)
    ungetch(c);

  return c;
}

#define BUFSIZE 100
char buf[BUFSIZE]; // buffer for ungetch
int bufp = 0; // next free position in buf
int getch(void) {
  return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) {
  if (bufp >= BUFSIZE)
    printf("ungetch: too many characters\n");
  else
    buf[bufp++] = c;
}
