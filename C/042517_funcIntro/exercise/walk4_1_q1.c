#include<stdio.h>

main()
{

   int x = 1, count = 1;
   
   while(x)
   {
     printf ("This is a line\n");
     if ( count > 3 )
        x = 0;
     else
        printf ("moo");

     count = count + 1;
    }     
}

