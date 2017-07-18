#include <stdio.h>
int* large(int *p_first, int *p_second);
int main(){
  int first;
  int second;
  int *p_large;
  printf("Input the first number: \n");
  scanf("%d", &first);
  printf("Input the second number: \n");
  scanf("%d", &second);
  
  p_large = large(&first, &second);
  printf("The number %d is larger", *p_large);
  return 0;
}


int* large(int *p_first, int *p_second){
  int *large;
   if (*p_first < *p_second){
      large = p_second;
  }
  else{
    large = p_first;
  }
  return large;
} 
