/* walk 3 - demonstration of nested if statements */

#include <stdio.h>

int main(){
	int n1, n2, n3;
	char choice = 'M';
	double result;

	n1 = n2 = 12;
	n3 = ( n1 - 4 ) % ( n2 - 6 );

	if ( n1 > n3 && choice == 'N' ) {
		result = n1 / n3 + ( n2 - 10 );
		choice = 'Y';
	} else if ( n2 < n3 + n1 && choice != 'N' ) {
		if ( choice == 'M' )
			choice = 'N';
		else
			choice = 'M';
		result = n1 * n3;
	} else
		result = 0;
	printf("n1 is %d, n2 is %d, n3 is %d, result is %.2lf, choice is %c\n",
		                 	n1, n2, n3, result, choice);
	return 0;
}

