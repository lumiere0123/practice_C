/* fun6.c - demonstrates the use of do/while statement  */

#include <stdio.h>

int main(){
	int num1, num2;

	do{
		printf("Enter the number:");
		scanf("%d", &num1);
		printf("Enter the same number again:");
		scanf("%d", &num2);
		if( num1 != num2 )
			printf("The numbers are not equal!Try again\n");
	} while (num1 != num2);
	printf("The numbers are equal!\n");
	return 0;
}

