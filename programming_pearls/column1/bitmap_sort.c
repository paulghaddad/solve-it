#include <stdlib.h>
#include <stdio.h>

int main(void) {
  // Phase 1: Initialize the set to empty
  int n = 1000000;
  int bit[n];

  for (int i = 0; i < n; i++) {
    bit[i] = 0;
  }

  // Phase 2: Read in file and insert present elements into the set
  FILE *fp_input;
  int num;

  fp_input = fopen("integer_set.txt", "r");

  if (fp_input == NULL) {
    printf("Error opening file.\n");
    exit(1);
  }

  while (fscanf(fp_input, "%d", &num) != EOF) {
    bit[num] = 1;
  }

  fclose(fp_input);

  // Phase 3: Write sorted output
  FILE *fp_output;

  fp_output = fopen("sorted_output.txt", "w");

  if (fp_output == NULL) {
    printf("Error opening file.\n");
  }

  for (int i = 0; i < n; i++) {
    fprintf(fp_output, "%d\n", bit[i]);
  }

  fclose(fp_output);

  return EXIT_SUCCESS;
}
