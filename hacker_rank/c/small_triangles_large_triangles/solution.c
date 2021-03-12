#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
  int a;
  int b;
  int c;
};

typedef struct triangle triangle;
int compare_triangle(const void *tri1, const void *tri2) {
  const triangle *x = tri1;
  const triangle *y = tri2;

  float p1 = (x->a + x->b + x->c) / 2.0;
  float p2 = (y->a + y->b + y->c) / 2.0;

  float area1 = sqrt(p1 * (p1-x->a) * (p1-x->b) * (p1-x->c));
  float area2 = sqrt(p2 * (p2-y->a) * (p2-y->b) * (p2-y->c));

  float diff = area1 - area2;
  if (diff > 0)
    return 1;
  else if (diff < 0)
    return -1;
  else
    return 0;
}

void sort_by_area(triangle* tr, int n) {
  qsort(tr, n, sizeof(triangle), compare_triangle);
}

int main() {
  int n;
  scanf("%d", &n);
  triangle *tr = malloc(n * sizeof(triangle));
  for (int i = 0; i < n; i++) {
    scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
  }
  sort_by_area(tr, n);
  for (int i = 0; i < n; i++) {
    const triangle *tri = &tr[i];
    double p1 = (tri->a + tri->b + tri->c) / 2.0;
    double area = sqrt(p1 * (p1-tri->a) * (p1-tri->b) * (p1-tri->c));
    printf("%d %d %d Area: %f\n", tr[i].a, tr[i].b, tr[i].c, area);
  }
  return 0;
}
