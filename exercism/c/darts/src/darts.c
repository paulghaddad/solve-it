#include "darts.h"
#include <math.h>

enum scores { INNER_CIRCLE_SCORE=10, MIDDLE_CIRCLE_SCORE=5, OUTER_CIRCLE_SCORE=1, NO_SCORE=0};

int score(coordinate_t position) {
  float radius = sqrt(powf(position.x, 2) + powf(position.y, 2));

  if (radius <= 10.0 && radius > 5.0)
    return OUTER_CIRCLE_SCORE;
  else if (radius <= 5.0 && radius > 1.0)
    return MIDDLE_CIRCLE_SCORE;
  else if (radius <= 1.0 && radius >= 0.0)
    return INNER_CIRCLE_SCORE;
  else
    return NO_SCORE;
}
