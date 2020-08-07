#include <stdlib.h>
#include <stdio.h>
#include "triangle.h"

enum boolean { FALSE, TRUE };

int valid_triangle(triangle_t triangle);
int compare(const void *a, const void *b);

int is_equilateral(triangle_t triangle) {
  if (!valid_triangle(triangle))
    return FALSE;

  return triangle.a == triangle.b && triangle.b == triangle.c && triangle.a == triangle.c;
}

int is_isosceles(triangle_t triangle) {
  if (!valid_triangle(triangle))
    return FALSE;

  double sides[3] = { triangle.a, triangle.b, triangle.c };
  qsort(sides, 3, sizeof(double), &compare);
  if (sides[0] == sides[1] || sides[1] == sides[2])
    return TRUE;

  return FALSE;
}

int is_scalene(triangle_t triangle) {
  if (!valid_triangle(triangle))
    return FALSE;

  return triangle.a != triangle.b && triangle.b != triangle.c && triangle.a != triangle.c;
}

int valid_triangle(triangle_t triangle) {
  if (triangle.a <= 0 || triangle.b <= 0 || triangle.c <= 0)
    return 0;

  double sides[3] = { triangle.a, triangle.b, triangle.c };
  qsort(sides, 3, sizeof(double), &compare);

  if (sides[0] + sides[1] < sides[2])
    return FALSE;

  return TRUE;
}

int compare(const void *a, const void *b) {
  if (*(double *)a > *(double *)b)
    return 1;
  else if (*(double * )a > *(double *)b)
    return -1;
  else
    return 0;
}
