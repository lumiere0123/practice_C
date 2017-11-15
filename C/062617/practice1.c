#include <stdio.h>
int* createArray(int size){
  int array2[size];
  return array2;
}
  
void printArray(int *array2, int size){
  for (int i = 0; i < size; i++){
    //printf("array2[%d] = %d\n", i, array2[i]);
    printf("array2[%d] = %d\n", i, *(array2+i));
  }
}


void inputArray(int *array2, int size){
  for (int i = 0; i < size; i++){
    //printf("array2[%d] = %d\n", i, array2[i]);
    array2[i] = i+1;
    *(array2+i) = i+1;
  }
}
  
int main(){
  int* array2 = createArray(100);
  inputArray(array2, 100);
  printArray(array2,100);
  return 0;
}
