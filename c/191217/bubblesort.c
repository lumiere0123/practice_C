#include <stdio.h>
void display (int* input);
int main(){
  int big=0;
  int input[8] ={6,5,3,1,8,7,2,4};
  int size=8;
  for (int n=0;n<size-1; n++){
    for (int i=0; i<size-n; i++){
      if (input[i] > input[i+1]){
        big = input[i];
        input[i] = input[i+1];
        input[i+1] = big;
      }
      display(input);
    }
    printf("\n================\n");
  }
  return 0;
}
       
void display (int* input){
  for (int i=0; i<8; i++){
    printf ("%d ",input[i]);
  }
  printf("\n");
}
