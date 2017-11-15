#include <stdio.h>
int PrimeNum (int num);
int main(){
  int result;
  int num;
  printf ("Input a positive number: \n");
  scanf ("%d",&num);
  result = PrimeNum (num);
  if (result == 0){
    printf ("The number %d is not a prime number", num);
  }
  else{
    printf ("The number %d is a prime number", num);
  }
  return 0;
}



int PrimeNum (int num){
  int half;
  int result;
  if (num % 2 == 0){
    half = num / 2;
  }
  else{
    half = num / 2 + 0.5;
  }

  for (int i = 2; 2 <= i && i<= half; i++){
    if (num % i == 0){
      result = 0;
      break;
    }
    else{
      result = 1;
    }
  }
  return result;
}
 
