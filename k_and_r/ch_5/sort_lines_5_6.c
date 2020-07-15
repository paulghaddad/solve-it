#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAXLINES 5000 // max lines to be sorted

char *lineptr[MAXLINES]; // pointers to text lines

int readlines(char *lineptr[], int nlines);
void writelines(char *lineptr[], int nlines);

void quicksort(char *lineptr[], int left, int right);

// sort input lines

int main(void) {
  int nlines; // number of input lines read

  if ((nlines = readlines(lineptr, MAXLINES)) >= 0) {
    quicksort(lineptr, 0, nlines-1);
    writelines(lineptr, nlines);
    return EXIT_SUCCESS;
  } else {
    printf("error: input too big to sort\n");
    return 1;
  }
}

#define MAXLEN 1000 // max length of any input line
int get_line(char *, int);
char *alloc(int);

// read input lines
int readlines(char *lineptr[], int maxlines) {
  int len, nlines;
  char *p, line[MAXLEN];

  nlines = 0;
  while ((len = get_line(line, MAXLEN)) > 0)
    if (nlines >= maxlines || (p = alloc(len)) == NULL)
      return -1;
    else {
      line[len-1] = '\0'; // delete newline
      strcpy(p, line);
      lineptr[nlines++] = p;
    }

  return nlines;
}

// write output lines
void writelines(char *lineptr[], int nlines) {
  while (nlines-- > 0)
    printf("%s\n", *lineptr++);
}

void quicksort(char *v[], int left, int right) {
  int i, last;
  void swap(char *v[], int i, int j);

  if (left >= right)
    return;

  swap(v, left, (left + right)/2);
  last = left;
  for (i = left+1; i <= right; i++)
    if (strcmp(v[i], v[left]) < 0)
      swap(v, ++last, i);

  swap(v, left, last);
  quicksort(v, left, last-1);
  quicksort(v, last+1, right);
}

int get_line(char line[], int maxlen) {
  int c;
  int i = 0;

  while ((c = getchar()) != EOF && (c != '\n') && i < maxlen) {
    line[i] = c;
    ++i;
  }

  line[i] = '\0';

  return i;
}

void swap(char *v[], int i, int j) {
  char *temp;

  temp = v[i];
  v[i] = v[j];
  v[j] = temp;
}
