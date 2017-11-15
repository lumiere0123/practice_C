#include <stdio.h>
void reverse (int *p_array , int size);
int main(){
  int array [5] = {2,3,4,5,6};
  reverse (&array[0], 5);
  return 0;
}

void reverse (int *p_array , int size){
  for (int i = 0; i < size; i++){
    printf ("element - %d : %d\n", size - i, *(p_array + size - i - 1));
  }
}

