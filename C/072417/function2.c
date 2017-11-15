#include <stdio.h>
char* checkEven (int num);
int main(){
  int num;
  char * result;
  printf ("Input any number: \n");
  scanf ("%d", &num);
  result = checkEven (num);
  printf("The entered number is %s", result);
  return 0;
} 
 


char* checkEven (int num){
  char* check;
  if (num / 2 == 0){
    check = "Even";
  }
  else{
    check = "Odd";
  }
  return check;
}
