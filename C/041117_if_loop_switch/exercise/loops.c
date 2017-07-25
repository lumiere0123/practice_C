#include <stdio.h>


int main(){
	int num = 0;
	int guess_num = 7;

	printf("Guess a number (1 - 10): ");
	scanf("%d", &num);

	while(guess_num != num){
	      printf("Wrong... Try again...: ");
	      scanf("%d", &num);
	}
	printf("Cheater! How did you guess it?\n");
	return 0;
}
