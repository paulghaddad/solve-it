#include <stdlib.h>
#include <stdio.h>

#define INT_SIZE 32

int main(void) {
  // Phase 1: Initialize the set to empty
  int n = 1000000;
  int bitmap[n/INT_SIZE];

  for (int i = 0; i < n/INT_SIZE; i++) {
    bitmap[i] = 0;
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
    int bitmap_ind = num / INT_SIZE;
    unsigned int flag = 1;
    bitmap[bitmap_ind] |= flag << num % INT_SIZE;
  }

  fclose(fp_input);

  // Phase 3: Write sorted output
  FILE *fp_output;

  fp_output = fopen("sorted_output.txt", "w");

  if (fp_output == NULL) {
    printf("Error opening file.\n");
  }

  for (int i = 0; i < n/INT_SIZE; i++) {
    for (int j = 0; j < INT_SIZE; j++) {
      int bitmap_ind = num / INT_SIZE;
      unsigned int flag = 1;
      fprintf(fp_output, "%d\n", (bitmap[bitmap_ind] & (flag << j)) > 0 );
    }
  }

  fclose(fp_output);

  return EXIT_SUCCESS;
}
