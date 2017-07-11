/*      Programmer:    Arta Kogan
	Program Name:  fun8.c
	Date:          May 16, 2001
	Purpose:       Demonstration the use of functions.   */
#include <stdio.h>

float calculate_total(int books, float book_price){
	float total;

	total = books * book_price;

	return total;
}

int main(){

	int num_of_books;
	float price;
	float cost;
	double total = 0;

	num_of_books = 0;
	price = 0;
	cost = 0.00;

	printf("\n\n");
	printf("Please, enter the number of books:");
	scanf("%d", &num_of_books);

	printf("Please, enter the price for a single book:");
	scanf("%f", &price);

	cost = calculate_total( num_of_books, price);

	total = cost * 1.15;

	printf("There are %d books selected\n", num_of_books);
	printf("Price for a single book: %f\n", price);
	printf("Cost before taxes: %f\n", cost);
	printf("Total after taxes: %lf\n", total);

	return 0;
}
