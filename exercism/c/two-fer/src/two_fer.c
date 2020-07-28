#include <string.h>
#include "two_fer.h"

void two_fer(char* buffer, const char* name) {
  if (name) {
    strcat(buffer, "One for ");
    strcat(buffer, name);
    strcat(buffer, ", one for me.");
  } else
    strcpy(buffer, "One for you, one for me.");
}
