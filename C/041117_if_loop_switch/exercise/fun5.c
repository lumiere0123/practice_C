/* fun5.c - demonstrates the use of the while statement  */

#include <stdio.h>

int main(){

	int num_child;
	int counter = 0;
	int age;

	printf("Enter the number of children:");
	scanf("%d", &num_child);

	while( counter < num_child ){
		counter = counter + 1;
		printf("Enter the age for child %d:", counter);
		scanf("%d", &age);
		printf("The age of child %d is %d\n", counter, age);
	}

	return 0;
}

