/* printHeader.c
   Author: Murray Saul
   Date: January 27, 2008
   Purpose: Demonstrate simple function
            that does NOT accept parameters
            or return values
*/

#include<stdio.h>

void printHeader();
void printFooter();

main()
{
  double sales=34.0, GST=0.05, PST=0.08;

  printHeader();
  printf ("Sales: $%.2lf\n", sales);
  printf ("GST: $%.2lf\n", sales*GST);
  printf ("PST: $%.2lf\n", sales*PST);
  printf ("TOTAL: $%.2lf\n", sales+sales*PST+sales*GST);
  printFooter();
}

void printHeader()
{
  printf ("+-------------------------+\n");
  printf ("|   Sales Report          |\n");
  printf ("+-------------------------+\n");
}

void printFooter()
{
  printf ("+-------------------------+\n");
  printf ("|   End of Sales Report   |\n");
  printf ("+-------------------------+\n");
}
