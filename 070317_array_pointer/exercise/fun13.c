/* fun13.c   - Demonstrates the use of pointers. Prints the values and addresses of the variables  */
#include <stdio.h>

main(){
	int x = 4;
	char a = 'a';

	int *p_x = &x;
	char *p_a = &a;

	printf("the value of x is %d\n", x);
/* direct access to x   */

	printf("the value of *p_x is %d\n", *p_x);
/* indirect access to x */

/* both lines will display the value stored in x */
	printf("the address of x is %p\n", &x);
	printf("the value of p_x is %p\n", p_x);
}
