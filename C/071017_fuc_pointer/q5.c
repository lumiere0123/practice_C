#include <stdio.h>
int add (int first, int second);
int add2 (int *p_fir, int *p_sec);
int main(){
  int first;
  int * p_first = &first;
  int second;
  int * p_second = &second;
  int result;
  printf("Test Data:\n");
  printf ("Input the first number:\n");
  scanf ("%d", &first);
  printf ("Input the second number:\n");
  scanf ("%d", &second);
  result = add2 (p_first, p_second);
  printf ("The sum of %d and %d is %d\n", first, second, result);
  return 0;
}



int add (int first, int second){
  int result = first + second;
  return result;
} 

int add2 (int *p_fir, int *p_sec){
  int result = *p_fir + *p_sec;
  return result;
}
