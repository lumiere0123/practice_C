#include <stdio.h>
int sum (int *p_array, int size);
int sum1(int *p_array, int index, int size);
int main(){
  int array[4]= {1,2,3,4};
//  int sum = 0;
//  for (int i = 0; i < 4; i++){
//    sum = sum + array[i];
//  }
//  printf ("%d",sum);
//  
  printf ("%d", sum1(&array[0],0, 4));
  return 0;
}    

int sum (int *p_array, int size){
  int sum =0;
  for (int i = 0; i < size; i++){
    sum = sum + *(p_array+i); 
  }
  return sum;
}

int sum1(int *p_array, int index, int size){
  int sum = 0;
  if (index == size){
    return 0;
  }  
  sum= sum1(p_array, index+1,size) + *(p_array + index);
  return sum;
} 
