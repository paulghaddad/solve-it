#ifndef DARTS_H
#define DARTS_H

struct coordinate_t {
  float x;
  float y;
};

typedef struct coordinate_t coordinate_t;

int score(coordinate_t position);

#endif
