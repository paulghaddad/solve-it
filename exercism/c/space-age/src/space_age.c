#include "space_age.h"
#include <stdio.h>

#define EARTH_SECONDS_PER_YEAR 31557600

const float orbital_periods[] = { 0.2408467, 0.61519726, 1.0, 1.8808158, 11.862615, 29.447498, 84.016846, 164.79132 };


float convert_planet_age(planet_t planet, int64_t input) {
  return input / EARTH_SECONDS_PER_YEAR / orbital_periods[planet];
}
