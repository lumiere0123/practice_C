/* walk 4 - demonstration of nested for loops 	    */
/* Determine exact output of the following program  */

#include <stdio.h>

void main(void) {
	int i, j, k, num;
	char ch=' ';

	num = 4;

	for (j = 0; j <= num; j ++) {
		for(i = j; i < num; i++)
			printf("%c",ch);
		for(k = 0; k < j; k ++ )
			printf("%d", k);
		printf("%d",j);
		for(k = j-1; k >= 0; k --)
			printf("%d",k);
		printf("\n");
	}

}

