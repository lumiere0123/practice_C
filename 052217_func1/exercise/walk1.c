#include<stdio.h>

void foo (int num);

main (){
     int value;
     printf ("\nEnter an integer less than 13: ");
     scanf ("%d", &value);
     while ( value >= 13 ){
         printf ("\nPlease pick a number less than 13: ");
        scanf ("%d", &value);
     }
     printf ("\n");
     foo (value);
     printf ("\n");
}
void foo (int num){
     int i;
     for (i = 1; i <= 12; i++)
        printf ("%d x %d = %d\n", i, num, num * i);
}

