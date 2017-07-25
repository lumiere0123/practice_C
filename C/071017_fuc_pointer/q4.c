#include <stdio.h>
int main(){
  int first;
  int * p_first = &first;
  int second;
  int * p_second = &second;
  printf("Test Data:\n");
  printf ("Input the first number:\n");
  scanf ("%d", &first);
  printf ("Input the second number:\n");
  scanf ("%d", &second);
  printf("The sum of the entered numbers is : %d", *p_first + *p_second);
  return 0;
}

