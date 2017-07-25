/* fun14.c - Modified fun7.c to use functions */


#include <stdio.h>

/* functions prototypes */

void display_menu(void);
int get_choice(void);
double add_them(void);
double subtract_them(void);
double divide_them(void);
double multi_them(void);
void display_result(double);

/* main function */

void main(void){

/* variables declaration */
	double result = 0;   		/* used to store the result of the calculation */
	int choice = 0;      		/* used to store user's choice */

	display_menu();      		/* function call  - to display the menu of choices */
	choice = get_choice(); 		/* function call - to get and validate user's choice  */

	while(choice != 5){    		/* loop until user enters 5 for his/her choice */
		switch(choice){			/* perform specific operation depending on the value of the "choice" */
			case 1: 			/* user selected first choice - add numbers   */
				result = add_them();  /* function call - add_them will return the result of addition */
				break;
			case 2:				/* user selected second choice - subtract numbers */
				result = subtract_them(); 	/* function call - function will return */
				break;						/* the result of subtraction */
			case 3:				/* user selected third choice - multiply numbers */
				result = multi_them();		/* function call - function will return */
				break;						/* the result of multiplication */
			case 4:							/* user selected fourth choice - divide numbers */
				result = divide_them(); 	/* function call - function will return */
				break;						/* the result of division */
		}
		display_result(result);	/* function call - to display the result of the operation */
		/* important! - a copy of the result variable is sent   */

		display_menu();			/* function call - to redisplay the menu of choices */
		choice = get_choice();	/* function call - to get and validate user's choice  */
	}
}

/* Function display_menu() - does not receive any parameters, does not return
any values. Used to display the menu of choices  */

void display_menu(void){
	printf("1       Add\n");
	printf("2       Subtract\n");
	printf("3       Multiply\n");
	printf("4       Divide\n");
	printf("5       Exit\n\n");
}

/* Function int get_choice(void) - does not receive any parameters, returns integer.
	Used to get user's choice, performes simple validaion            */

int get_choice(void){
	int choice = 0, ret = 0;

	do{
		printf("Please, enter your choice:");
		scanf("%d", &choice);
		if(choice < 1 || choice > 5){
			printf("Invalid choice!\n\n");
			display_menu();
		}
	}while(choice < 1 || choice > 5);


      return choice;
}

/* Function double add_them(void) - does not receive any parameters, returns double.
	Used to get two numbers from the user, returns the summary of two entered numbers  */

double add_them(void){
	double num1, num2;

	printf("Enter two numbers to add:");
	scanf("%lf%lf",&num1, &num2);

	return num1 + num2;
}

/* Function double subtract_them(void) - does not receive any parameters, returns double.
	Used to get two numbers from the user, returns the result of subtraction */

double subtract_them(void){
	double num1, num2;

	printf("Enter two numbers to subtruct:");
	scanf("%lf%lf", &num1, &num2);

	return num1 - num2;
}

/* Function double divide_them(void) - does not receive any parameters, returns double.
	Used to get two numbers from the user, returns the result of division. Performes simple
	validation - both numbers must be greater then 0 */

double divide_them(void){
	double num1 = 0, num2 = 0;

	do{
		printf("Enter two positive numbers to divide:");
		scanf("%lf%lf", &num1, &num2);
	} while(num1 <= 0 || num2 <= 0);
	return num1 / num2;
}

/* Function double multi_them(void) - does not receive any parameters, returns double.
	Used to get two numbers from the user, returns the result of multiplicaton      */

double multi_them(void){
	double num1, num2;

	printf("Enter two numbers to multiply:");
	scanf("%lf%lf", &num1, &num2);
	return num1 * num2;
}

/* Function void display_result(double result) - receives one parameter - a double
	returns no values. Used to display the result of the calculations to the user */

void display_result(double result){
	printf("The result is %.2lf\n\n", result);
}













