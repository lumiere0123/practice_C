/* walk7.c
Determine the exact output of the following program  */

#include <stdio.h>

int task_1(int a, int b, char c);

main(){
	int n1, n2, n3;
	char ch = 'A';

	n1 = 3;
	n2 = 8;
	n3 = task_1( n1, n2, ch );
	printf("n1 is %d, n2 is %d, n3 is %d, ch is %c\n",
		 n1, n2, n3, ch);
}

int task_1(int a, int b, char c){
	int ret;

	if(b % a){  /* note  if(b % a) is the same as if(b % a != 0)  */
		ret =  b + ( a - b%a);
		c = 'C';
	} else {
		ret = b;
		c = 'N';
	}
	return ret;
}

