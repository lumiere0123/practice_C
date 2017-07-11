#include <stdio.h>

int main(){
	int num1 = 0;
	int sum = 0;
	int counter = 3;

	while(counter >  0){
		printf("Enter a number: ");
		scanf("%d", &num1);
		counter = counter - 1;
		sum = sum + num1;
	}
	printf("The sum of the numbers is: %d\n", sum);

	return 0;
}
