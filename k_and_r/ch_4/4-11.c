// includes
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// defines
#define MAXOP 100 // max size of operand or operator
#define NUMBER '0' // signal that a number was found

// function declarations for main
int getop(char s[]);
void push(double f);
double pop(void);

int main(void) {
  int type;
  double op2;
  char s[MAXOP];

  while ((type = getop(s)) != EOF) {
    switch(type) {
      case NUMBER:
        push(atof(s));
        break;
      case '+':
        push(pop() + pop());
        break;
      case '*':
        push(pop() * pop());
        break;
      case '-':
        op2 = pop();
        push(pop() - op2);
        break;
      case '/':
        op2 = pop();
        if (op2 != 0.0)
          push(pop() / op2);
        else
          printf("error: zero divisor\n");
        break;
      case '%':
        op2 = pop();
        push(fmod(pop(), op2));
        break;
      case '\n':
        printf("\t%.8g\n", pop());
        break;
      default:
        printf("error: unknown command %s\n", s);
        break;
    }
  }

  return EXIT_SUCCESS;
}

//external variables for push and pop
#define MAXVAL 100 // max depth of val stack

int sp = 0; // next free stack position
double val[MAXVAL]; // value stack

void push(double f) {
  if (sp < MAXVAL)
    val[sp++] = f;
  else
    printf("error: stack full, can't push %g\n", f);
}


double pop(void) {
  if (sp > 0)
    return val[--sp];
  else {
    printf("error: stack empty\n");
    return 0.0;
  }
}

#include <ctype.h>

int getch(void);
void ungetch(int);

int getop(char s[]) {
  int i, c, next_c;
  int negative = 0;

  while ((s[0] = c = getch()) == ' ' || c == '\t')
    ;

  s[1] = '\0';
  if (!isdigit(c) && c != '.') {
    next_c = getch();
    if (isdigit(next_c)) {
      negative = 1;
      ungetch(next_c);
    } else {
      ungetch(next_c);
      return c; // not a number
    }
  }

  i = 0;
  if (isdigit(c)) // collect integer part
    if (negative)
      s[++i] = '-';

    while (isdigit(s[++i] = c = getch()))
      ;
  if (c == '.') // collect fraction part
    while (isdigit(s[++i] = c = getch()))
      ;

  s[i] = '\0';
  if (c != EOF)
    ungetch(c);

  return NUMBER;
}

// routines called by getop

#define BUFSIZE 100

char buf[BUFSIZE]; // buffer for ungetch
int bufp = 0; // next free position in buf

// get a (possibly pushed back) character
int getch(void) {
  return (bufp > 0) ? buf[--bufp] : getchar();
}

// push character back on input
void ungetch(int c) {
  if (bufp >= BUFSIZE)
    printf("ungetch: too many characters\n");
  else
    buf[bufp++] = c;
}
