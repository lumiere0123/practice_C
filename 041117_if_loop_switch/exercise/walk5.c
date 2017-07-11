/* walk 5 - demonstration of nested while and for loops */
/* Determine exact output of the following program      */

#include <stdio.h>

void main(void) {
	int num, n1, n2;
	char ch='a';

	num = 4;
	n1 = 0;
	n2 = 3;

	while(n2 > 0) {
		for(n1 = 2; n1 <= num - 1; n1++){
			printf("character is %c ",ch++);
			printf("n2 is %d\n", n2);
		}
		n2--;
	}
	printf("character is %c ", ch);
	printf("n2 is %d\n", n2);
}

