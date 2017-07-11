#include <stdio.h>


int main(){
	int num = 0;
	int guess_num = 7;

	do{
		printf("Guess a number (1 - 10): ");
		scanf("%d", &num);
		if(guess_num != num)
			printf("Sorry, try again...\n");
       }while(guess_num != num);
	printf("Cheater! How did you guess it?\n");
	return 0;
}
