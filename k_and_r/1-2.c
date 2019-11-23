/*
 * Experiment to find out what happens when printf's argument string contains
 * \c, where c is some character not listed above.
 */
#include <stdio.h>

main()
{
  printf("hello, world\y");
}

/* We get a warning:
 * unknown escape sequence '\y'
 */
