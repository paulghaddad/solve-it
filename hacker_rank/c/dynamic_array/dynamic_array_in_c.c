#include <stdio.h>
#include <stdlib.h>

/*
 *  * This stores the total number of books in each shelf.
 *   */
int* total_number_of_books;

/*
 *  * This stores the total number of pages in each book of each shelf.
 *   * The rows represent the shelves and the columns represent the books.
 *    */
int** total_number_of_pages;

int main() {
  int total_number_of_shelves;
  scanf("%d", &total_number_of_shelves);

  int total_number_of_queries;
  scanf("%d", &total_number_of_queries);
  
  // initialize total num of books
  int* total_number_of_books = calloc(total_number_of_shelves, sizeof(int));
  if (total_number_of_books == NULL) {
      printf("Error allocating total number of books array\n");
      return -1;
  }

  // initialize total_number_of_pages
  int** total_number_of_pages = malloc(sizeof(int*) * total_number_of_shelves);
  if (total_number_of_pages == NULL) {
      printf("Error allocating total number of shelves array\n");
      return -1;
  }

  while (total_number_of_queries--) {
    int type_of_query;
    scanf("%d", &type_of_query);

    if (type_of_query == 1) {
      int x, y;
      scanf("%d %d", &x, &y);

      // Update total_number_of_books array
      *(total_number_of_books + x) += 1;

      /* for (int i = 0; i < total_number_of_shelves; i++) */
      /*   printf("Book Count: %d\n", *(total_number_of_books + i)); */

      // If this is the first book on the shelf
      if (*(total_number_of_books + x) == 1) {
        int* page_lengths = malloc(sizeof(int) * 1);
        *page_lengths = y;
        *(total_number_of_pages + x) = page_lengths;
      } else {
        // if this is the second book or more for the shelf
        int num_books = *(total_number_of_books + x);
        int *old_page_lengths = *(total_number_of_pages + x);
        int* new_page_lengths = realloc(old_page_lengths, num_books * sizeof(int));
        if (new_page_lengths == NULL) {
          printf("Error allocating total number of shelves array\n");
          return -1;
        }

        *(new_page_lengths + num_books - 1) = y;

        *(total_number_of_pages + x) = new_page_lengths;
      }
    } else if (type_of_query == 2) {
      int x, y;
      scanf("%d %d", &x, &y);
      printf("%d\n", *(*(total_number_of_pages + x) + y));
    } else {
      int x;
      scanf("%d", &x);
      printf("%d\n", *(total_number_of_books + x));
    }
  }

  /* for (int i = 0; i < total_number_of_shelves; i++) { */
  /*   int num_books = *(total_number_of_books + i); */
  /*   int *page_lengths = *(total_number_of_pages + i); */
  /*   printf("Book number: %d; num_books: %d\n", i, num_books); */
  /*   for (int j = 0; j < num_books; j++) { */
  /*     printf("The number of pages is %d\n", *(page_lengths + j)); */
  /*   } */
  /* } */

  if (total_number_of_books) {
    free(total_number_of_books);
  }

  if (total_number_of_pages) {
    free(total_number_of_pages);
  }

  return 0;
}
