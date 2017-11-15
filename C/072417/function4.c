#include <stdio.h>
#include <math.h>
long binary(int num);
int main(){
  int num;
  long result;
  printf ("Input any decimal number: \n");
  scanf ("%d", &num);
  result = binary (num);
  printf ("The Binary value is : %ld", result);
  return 0;
}


long binary(int num){
  long bin = 0;
  int num1Counter = 0;
  //for (int i = 0; num !=1 && num1Counter != 2 ; i++){ 
  for (int i = 0;num1Counter != 2 ; i++){ 
    bin = bin + (num % 2) * pow (10, i);
    num = num/2;
    if ( num ==0){
      num = 1;
    }
    if ( num == 1){
      num1Counter++;
    }


  }
  return bin;
}
 
