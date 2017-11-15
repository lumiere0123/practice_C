#include <stdio.h>
int square (int num);
int main (){
  int num;
  int result;
  printf ("Input any number for square: \n");
  scanf ("%d", &num);
  result = square (num);
  printf ("The square of %d is : %d", num, result);
}
  

int square (int num){
  int result;
  result = num * num;
  return result;
}
