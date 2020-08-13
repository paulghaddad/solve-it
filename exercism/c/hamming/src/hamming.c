#include "hamming.h"
#include <string.h>


int compute(const char *lhs, const char *rhs) {
  int difference = 0;

  if (lhs == NULL || rhs == NULL)
    return -1;

  if (strlen(lhs) != strlen(rhs))
    return -1;

  while (*lhs) {
    if (*lhs++ != *rhs++)
      difference++;
  }

  return difference;
}
