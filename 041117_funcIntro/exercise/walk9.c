/* walk9.c
Determine the exact output of the following program  */

#include <stdio.h>

int first(int , int,  char);

main(){
	int a, b, c;
	char ch = 'c';

	a = 13;
	b = 7;
	c = 0;
	printf("In main:a is %d, b is %d, c is %d, ch is %c\n",
		a, b, c, ch);
	c = first(b, a, ch );
	printf("In main:a is %d, b is %d, c is %d, ch is %c\n",
		 a, b, c, ch);
}

int first(int a, int b, char c){
	int return_value;

	switch(a + b){
		case 1:
			a++;
			b +=a;
			return_value =  b++;
			c = 'a';
			break;
		case 10:
			a--;
			b-=a;
			return_value = ++b;
			c = 'd';
			break;
		case 20:
			a /= 5;
			b *=a;
			return_value = --b;
			c = 'u';
	}
	printf("In first: a is %d, b is %d, c is %c\n", a, b, c);
	return return_value;
}

