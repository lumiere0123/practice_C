#include <stdio.h>
int main(){
  int i = 0;
  int sum;
  printf("Input the number of elements to store in the array (max 10): \n");
  scanf ("%d",&i);
  int c[i];
  printf("Input 5 number of elements in the array:\n");
  for (int a = 0; a < i; a++){
    printf("element - %d :",a+1);
    scanf("%d",c+a);
    
   // scanf("%d",&c[a]);
  }
  for (int a=0; a < i; a++){
    sum = sum+ *(c+a);
  //  sum = sum+ c[a];
  }
  printf("The sum of array is : %d",sum);
  return 0;
} 
