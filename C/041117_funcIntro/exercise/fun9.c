/*      Programmer:    Arta Kogan
	Program Name:  fun9.c
	Date:          May 23, 2001
	Purpose:       Demonstration the use of functions.   */

	#include <stdio.h>

	void  print_title(int num);         /* function prototype */
	void underline_title(void);			/* function prototype */
	int get_number(void); 				/* function prototype */
	void display_result(int num);		/* function prototype */

	int main(){
		int street_number = 70,
					number = 0;

		print_title(street_number);
		underline_title();
		number = get_number();
		display_result(number);
		return 0;
	}

	/* function definitions  */

	void  print_title(int num) /* function header */
	{
		printf("Cummer Valley Middle School\n");   /* function body */
		printf("%d Maxome Avenue\n", num);
	}
	void underline_title(void) /* function header */
	{
		int counter;

		for(counter = 0; counter < 27; counter ++)    /* function body */
			printf("-");
	}

	int get_number(void)  /* function header  */
	{
		int num;

		do {
			printf ("\nEnter an integer for Times Table ( 1 - 10 ): ");
			scanf ("%d", &num);
		} while (num < 1 || num > 10);
		return num;
	}

	void display_result(int num)  /* function header */
	{
		int i = 0;
	 		for (i = 1; i <= 10; i++)
	 	                printf ("%d times %d equals %d\n", num, i, num*i );
	 	   	printf ("\n");
	}





