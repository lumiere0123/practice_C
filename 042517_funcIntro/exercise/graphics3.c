/* graphics3.c
   Author: Murray Saul
   Date: January 30, 2008   Modified: January 30, 2008
   Purpose: Prompt user for number of columns and rows
            and send those values to a function called
            drawBox() to draw that box using Asterisk
            system *

            Additional Improvment: Loop in main() to draw
            boxes until user enters 1 for Yes to exit...

            Additional Improvement: Call a function to 
            verify that number of rows and columns
            are within 1 - 24 units...
*/

#include<stdio.h>

void drawBox(int x, int y);
int checkData();

main()
{

  int columns, rows, answer;

  do 
  {

    if ( checkData() )
    {
       printf ("Draw another? (1-yes, 0-no): ");
       scanf ("%d", &answer);
    }
    else
       printf ("Cannot Draw the Box!\n");

   } while ( answer != 0 );

} /* End of main program */


void drawBox(int x, int y)   /* Draws box based on column and row data */
{

  int i, j;

  printf ("\n"); /* print empty line to separate differently drawn boxes */

  for (i = 1; i <= y ; i++)   /* Outter Loop - i.e. number of rows.... */
  {
     for (j = 1; j <= x; j++)  /* Inner Loop - i.e. number of columns ... */
        printf ("*");
     printf ("\n");
  }
  printf ("\n"); /* print empty line to separate differently drawn boxes */

} /* end of drawBox() function */


int checkData()
{
       int rows, columns, status;

       printf ("Enter the number of columns: ");
       scanf("%d", &columns);
       printf ("Enter the number of rows: ");
       scanf("%d", &rows);

       if ( rows < 1 || rows > 24)
         status = 0;
       else if ( columns < 1 || columns > 24)
         status = 0;
       else
       {
          status = 1;
          drawBox(columns, rows);
       }
     

       return status;
}
