#include <stdio.h>
#include <ctype.h>

#include "isogram.h"

bool is_isogram(const char phrase[]) {
  if (phrase == NULL)
    return false;

  int lettersPresent = 0 << 26;

  for (int i = 0; phrase[i] != '\0'; ++i) {
    int letter = phrase[i];
    if (letter < 'A' || letter > 'z')
      continue;

    int bitPosition = 1 << (tolower(letter) - 'a');
    if ((lettersPresent & bitPosition) > 0)
      return false;

    lettersPresent |= bitPosition;
  }

  return true;
}
