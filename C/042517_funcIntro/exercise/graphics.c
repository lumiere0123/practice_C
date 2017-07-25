/* graphics.c
   Author: Murray Saul
   Date: January 30, 2008
   Purpose: Prompt user for number of columns and rows
            and send those values to a function called
            drawBox() to draw that box using Asterisk
            system *
*/

#include<stdio.h>

void drawBox(int x, int y);

main()
{

  int columns, rows;

  printf ("Enter the number of columns: ");
  scanf("%d", &columns);
  printf ("Enter the number of rows: ");
  scanf("%d", &rows);

  drawBox ( columns, rows);

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
