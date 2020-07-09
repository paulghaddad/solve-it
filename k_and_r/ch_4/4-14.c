#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

#define swap(_t, x, y) { \
 _t tmp = x; \
 x = y; \
 y = tmp; \
}

int main(void) {
  int num1 = 1, num2 = 2;

  swap(int, num1, num2);

  assert(num1 == 2 && num2 == 1);

  return EXIT_SUCCESS;
}
