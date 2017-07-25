/* square.c
   Author: Murray Saul
   Date: February 5, 2008
   Purpose: To demonstrate a function that accepts and int and returns
            and int.
*/

#include<stdio.h>

int sqr( int x );

main()
{

   int number, yahoo;

   printf ("Please enter a number: ");
   scanf ("%d", &number);

   printf ("The square of %d is: %d\n\n", number, sqr(number) );

} /* End of main() program */

int sqr( int x )
{

   return x * x;

} /* End of sqr() function */






















































