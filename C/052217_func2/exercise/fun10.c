/*  Programmer:    Arta Kogan
	Program Name:  fun10.c
	Date:          May 16, 2001
	Purpose:       Demonstration the use of functions.
		       Program determines if the integer is even or odd. */

#include <stdio.h>

int even_odd(int);

int main(){
	int y, x;

	printf("Enter one integer:");
	scanf("%d", &y);
	x = even_odd(y);

	printf("y is %d and it is ", y);

	if(x)  /* same as if ( x == 1 ) */
		printf("odd number\n");
	else
		printf("even number\n");
	return 0;
}

int even_odd(int num){
	return num % 2;
}

