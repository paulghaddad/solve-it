#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct Nameval Nameval;
struct Nameval {
  char *name;
  int  value;
};

struct NVtab {
  int nval;              // current number of values
  int max;               // allocated number of values
  Nameval *nameval;      // array of name-value pairs
} nvtab;

enum { NVINIT = 1, NVGROW = 2 };

int addname(Nameval newname);
int delname(char *name);

// add new name and value to nvtab
int addname(Nameval newname) {
  Nameval *nvp;

  if (nvtab.nval == 0) {
    nvtab.nameval = (Nameval *) malloc(sizeof(Nameval) * NVINIT);
    if (nvtab.nameval == NULL)
      return -1;

    nvtab.max = 1;
    nvtab.nval = 0;
  } else if (nvtab.nval >= nvtab.max) {
    nvtab.nameval = (Nameval *) realloc(nvtab.nameval, nvtab.max*NVGROW * sizeof(Nameval));
    if (nvtab.nameval == NULL)
      return -1;

    nvtab.max *= NVGROW;
  }

  nvtab.nameval[nvtab.nval] = newname;
  return nvtab.nval++;
}


// remove first matching nameval from nvtab
int delname(char *name) {
  // first position of item to be deleted
  for (int i = 0; i < nvtab.nval; i++) {


    if (strcmp(nvtab.nameval[i].name, name) == 0) {
      printf("Match found! Item %d\n", i);


      memmove(nvtab.nameval+i, nvtab.nameval+i+1, (nvtab.nval - i - 1) * sizeof(Nameval));
      nvtab.nval--;
      return 1;
    }

  }

  return 0;
}

int main(void) {
  struct Nameval item0 = {"Item 0", 0};;
  addname(item0);

  struct Nameval item1 = {"Item 1", 1};;
  addname(item1);

  struct Nameval item2 = {"Item 2", 2};;
  addname(item2);

  for (int i = 0; i < nvtab.nval; i++) {
    int value = nvtab.nameval[i].value;
    printf("Item: %d\n", value);
  }

  delname("Item 1");

  for (int i = 0; i < nvtab.nval; i++) {
    int value = nvtab.nameval[i].value;
    printf("Item: %d\n", value);
  }

  return EXIT_SUCCESS;
}
