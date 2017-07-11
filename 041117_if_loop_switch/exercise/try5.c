#include <stdio.h>

int main(){
	int num1 = 1;

	while(num1 >=1 && num1 <= 10){
		printf("Enter a number between 1 - 10");
		scanf("%d", &num1);

		if(num1 > 10 || num1 < 1)
			printf("Invalid number\n");
	}
	return 0;
}
