#include "nucleotide_count.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum valid_string { FALSE, TRUE };

const char *nucleotides = "A:0 C:0 G:0 T:0";

char *count(const char *dna_strand) {
  char *counts = (char *)malloc(sizeof (char) * 4 * 3 + 4);
  if (counts == NULL) {
    printf("malloc failed!\n");
    return "";
  }

  int a_cnt = 0, c_cnt = 0, g_cnt = 0, t_cnt = 0;
  int valid_strand = TRUE;

  while (*dna_strand) {
    switch (*dna_strand) {
      case 'A':
        a_cnt++;
        break;
      case 'C':
        c_cnt++;
        break;
      case 'G':
        g_cnt++;
        break;
      case 'T':
        t_cnt++;
        break;
      default:
        valid_strand = FALSE;
    }

    dna_strand++;
  }

  if (!valid_strand)
    strcpy(counts, "");
  else
    sprintf(counts, "A:%d C:%d G:%d T:%d", a_cnt, c_cnt, g_cnt, t_cnt);

  return counts;
}
