/* fun11.c  - using increment, decrement operators    */

int function_1( int );

main(){
	int num1, num2;

	num1 = 7;
	num2 = function_1(num1);
	printf("num1 is %d, num2 is %d\n", ++num1, num2++);
	num1 = function_1(num2);
	printf("num1 is %d, num2 is %d\n", num1--, --num2);
}

int function_1( int x ){
	int y = 0;

	y += --x;
	return y;
}
