/* walk8.c   - Determine the exact output of the following program */

#include <stdio.h>

main(){
	int a, b;
	int *p_a;
	int *p_b = &b;
	int *p;

	a = 5;
	p_a = &a;

	*p_b = 80;
	*p_a = b - a;

	p = p_b;
	*p = a + 7;

	printf("the value of a is %d, b is %d\n", a, b);
	printf("the value of a is %d, b is %d\n", *p_a, *p);
}

