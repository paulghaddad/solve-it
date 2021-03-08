#include "darts.h"
#include <math.h>

int score(coordinate_t position) {
  float radius = sqrt(powf(position.x, 2) + powf(position.y, 2));

  if (radius <= 10.0 && radius > 5.0)
    return 1;
  else if (radius <= 5.0 && radius > 1.0)
    return 5;
  else if (radius <= 1.0 && radius >= 0.0)
    return 10;
  else
    return 0;
}
