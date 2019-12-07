#include <stdio.h>

/* Print the F-C table in reverse order */

int main() {
  int fahr;

  for (fahr = 300; fahr >= 0; fahr -= 20)
    printf("%3d %6.1f\n", fahr, (5.0/9.0) * (fahr-32.0));

  return 1;
}
