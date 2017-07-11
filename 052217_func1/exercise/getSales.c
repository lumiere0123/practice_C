/* getSales.c
   Author: Murray Saul
   Date: Feb 7, 2008
   Purpose: To demonstrate the use of constants
*/

#include<stdio.h>
#define GST 0.05
#define PST 0.08

double selection(void);

main()
{

   double sales;

   sales = selection();

   printf ("Sales: $%.2lf\n", sales);
   printf ("GST: $%.2lf\n", sales * GST);
   printf ("PST: $%.2lf\n", sales * PST);
   printf ("TOTAL: $%.2lf\n\n", sales  * (1 + GST + PST));

} /* End of main() program */


double selection(void)
{

   double salesAmount;

   do
   {
       printf ("Please enter sales: ");
       scanf ("%lf", &salesAmount);

   } while (( salesAmount <= 0 ) && printf ("Invalid - sales must be postive\n"));

   return salesAmount;

} /* End selection() function */
































































