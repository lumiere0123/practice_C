#include <stdio.h>


int main(){
	int num = 0;
	int guess_num = 0;

	printf("Guess a number (1 - 10): ");
	scanf("%d", &num);
	
	for(guess_num = 5;guess_num != num;){
		 printf("Sorry, try again...\n");
		 printf("Guess a number (1 - 10): ");
		 scanf("%d", &num);
	      
	}
	printf("You won a million!\n..\n..\n..\nJust kidding..\n");
	return 0;
}
