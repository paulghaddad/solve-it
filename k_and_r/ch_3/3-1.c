#include <stdlib.h>
#include <stdio.h>

int binsearch(int x, int v[], int n);

int main(void) {
  int v[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

  printf("Binary search with a match: %d\n", binsearch(4, v, 10));
  /* printf("Binary search with a match: %d\n", binsearch(8, v, 10)); */
  /* printf("Binary search with no match: %d\n", binsearch(11, v, 10)); */

  return EXIT_SUCCESS;
}

int binsearch(int x, int v[], int n) {
  int mid;
  int low = 0;
  int high = n - 1;

  while (low <= high) {
    mid = (low+high) / 2;
    printf("Low is %d and high is %d and mid is %d\n", low, high, mid);

    if (x < v[mid])
      high = mid - 1;
    else
      low = mid + 1;
  }

  printf("v[mid] is %d\n", v[mid]);
  return (v[mid] == x ? mid : -1);
}
