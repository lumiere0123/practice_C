/* walk 6 - demonstration of functions.              */
/* Determine exact output of the following program   */

#include <stdio.h>

int abc( char a, char b, int d ){
	int c;

	if ( a == b )
		c = 0;
	else c = 1;

	return c + d/2;
}

int main(){
	int b = 0,
	     c = 3,
	     d = 6;

	char ch1 = 'J',
	        ch2 = 'K';

	b = abc(ch1, ch2, c);

	printf("%d, %d, %d, %c, %c\n", b, c, d, ch1, ch2);

	for( b = 0; b < c; b ++ )
		d = d + b;
	ch1 = ch2 = 'A';

	printf("%d, %d, %d, %d, %c, %c\n",
			b, c, d, abc( ch1, ch2, d), ch1, ch2);

	return 0;
}


