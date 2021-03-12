#include "acronym.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ABBREVIATION_LENGTH 10

char *abbreviate(const char *phrase) {
  if (phrase == NULL || strncmp(phrase, "", 1) == 0)
    return NULL;

  char* abbreviation = (char*) malloc(sizeof(char) * MAX_ABBREVIATION_LENGTH);
  if (abbreviation == NULL)
    return NULL;

  int j = 0;
  *(abbreviation + j++)= toupper(*phrase);

  for (int i = 1; *(phrase + i) != '\0'; i++) {
    char prev = *(phrase + i - 1);
    char curr = *(phrase + i);

    if (!isalpha(curr))
      continue;

    if (prev == ' ' || prev == '-' || prev == '_') {
      *(abbreviation + j) = toupper(*(phrase + i));
      j++;
    }
  }

  *(abbreviation + j) = '\0';

  return abbreviation;
}
