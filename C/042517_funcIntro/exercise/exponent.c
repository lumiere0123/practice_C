/* exponent.c
   Author: Murray Saul
   Date: January 27, 2008
   Purpose: Prompt user for number, then
            number to generate the exponent.
*/

#include<stdio.h>

main()
{

  int base, exponent, i, result;

  printf ("Please enter the base: ");
  scanf ("%d", &base);
  printf ("Please enter the exponent: ");
  scanf ("%d", &exponent);

  result = base;

  printf ("%d raised to the power of %d is: ", base, exponent);

  /* Use for loop to generate the exponent result */

  for (i=1; i < exponent; i++)
   result = result * base;

  printf ("%d\n\n", result);

} /* End of main program */


