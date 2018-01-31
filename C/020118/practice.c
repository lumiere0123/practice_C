#include <stdio.h>
#include <stdlib.h>
int abs1(int input);
int main(){
  int a = -4;
  int True =0;
  int False =1;
  int result1 = 0;
  int result2 = 0;
 
  for (int i =0; i<10000000; i++){
    if (abs(a) == abs1(a)){
      result1 = result1+ True; 
    }
    else{
      result1 = result1+ False;
    }
  }

  for (int i =0;i>-100000000000000&&i<=0; i--){

    if (abs(a) == abs1(a)){
      result2 = result2+ True; 
    }
    else{
      result2 =result2+ False;
    }
  }

  if (result1+result2 ==0){
    printf("True");
  }
  else{
    printf("False");
  } 
  
  return 0;
}


int abs1(int input){
  if (input < 0){
    return input*-1;
  }
  else{
    return input;
  }
}
