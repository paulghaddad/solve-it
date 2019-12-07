/* Write a program to determine the ranges of char, short, int, and long
 * variables, both signed and unsigned, by printing appropriate values from
 * standard headers and by direct computation. Harder if you computer them:
 * determine the ranges of the various float types.
 */

#include <stdio.h>
#include <limits.h>
#include <float.h>

main() {
  // char type
  printf("The size of the char type is %d\n", CHAR_BIT);
  printf("The range of values for the char type is %d to %d\n", CHAR_MIN, CHAR_MAX);

  // signed short type
  printf("The range of values for the signed short type is %d to %d\n", SHRT_MIN, SHRT_MAX);

  // signed int type
  printf("The range of values for the signed int type is %d to %d\n", INT_MIN, INT_MAX);

  // signed long type
  printf("The range of values for the signed long type is %ld to %ld\n", LONG_MIN, LONG_MAX);

  // unsigned short type
  printf("The range of values for the unsigned short type is 0 to %d\n", USHRT_MAX);

  // unsigned int type
  printf("The range of values for the unsigned int type is 0 to %d\n", UINT_MAX);

  // unsigned long type
  printf("The range of values for the unsigned long type is 0 to %ld\n", ULONG_MAX);

  // float type
  printf("The range of values for the float type is %f to %f\n", FLT_MIN, FLT_MAX);

  // double type
  printf("The range of values for the double type is %f to %f\n", DBL_MIN, DBL_MAX);
}
