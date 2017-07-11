/*  Programmer:       Arta Kogan
	Program Name:     fun7.c
	Date:             May 16, 2001
	Purpose:          Demonstration the use of switch statement.  */

#include <stdio.h>


/* main function */

void main(void){

/* variables declaration */
	double result = 0;              /* used to store the result of the calculation */
	int choice = 0;                 /* used to store user's choice */
	double num1, num2;
	num1 = num2 = 0;

	do{             /* loop until user enters 5 for his/her choice */
		/* display the menu of choices */

			printf("1       Add\n");
			printf("2       Subtract\n");
			printf("3       Multiply\n");
			printf("4       Divide\n");
			printf("5       Exit\n\n");

		/* get and validate user's choice  */

			do{
				printf("Please, enter your choice:");
				scanf("%d", &choice);
				if(choice < 1 || choice > 5){
					printf("Invalid choice!\n\n");
				}
			}while(choice < 1 || choice > 5);
			switch(choice){                 /* perform specific operation depending on the value of the "choice" */
				case 1:                         /* user selected first choice - add numbers   */
					/* add_them */

					printf("Enter two numbers to add:");
					scanf("%lf%lf",&num1, &num2);

					result = num1 + num2;
					break;
				case 2:                         /* user selected second choice - subtract numbers */

					printf("Enter two numbers to subtruct:");
					scanf("%lf%lf", &num1, &num2);

					result = num1 - num2;
					break;
				case 3:                         /* user selected third choice - multiply numbers */

					printf("Enter two numbers to multiply:");
					scanf("%lf%lf", &num1, &num2);
					result = num1 * num2;
					break;
				case 4:                                                 /* user selected fourth choice - divide numbers */

					do{
						printf("Enter two positive numbers to divide:");
						scanf("%lf%lf", &num1, &num2);
					} while(num1 <= 0 || num2 <= 0);
					result = num1 / num2;
					break;
			}
			if(choice != 5)
				printf("The result is %.2lf\n\n", result);
			else
				printf("Thank you for using this program.\n\n");

	}while(choice != 5);
}

