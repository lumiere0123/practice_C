#include <stdio.h>
void reverse (int *p_array, int size);
void reverse2 (int *p_array, int size);
int main(){
  int array[8]= {1,2,3,4,5,6,7,8};
  reverse2 (array,8);
  for (int i =0; i < 8; i++){
    printf ("%d\n",array[i]);
  }
  return 0;
}
  


void reverse (int *p_array, int size){
  int c_array[size];
  for (int i = 0; i < size; i++){
    c_array[i]=p_array[i];
  }
  int rev_array[size];
  for (int a = 0; a < size; a++){
    rev_array[a]= c_array [size - a - 1];
  }
  for (int b = 0; b < size; b++){
    p_array[b] = rev_array[b];
  }
}
  
void reverse2 (int *p_array, int size){
  for (int i = 0; i < size; i++){
    int temp = *(p_array + i);
    *(p_array + i) = *(p_array + size - i- 1);
    *(p_array + size -i-1) = temp;
    printf (" when i = %d ", i);
    for (int r =0; r < size; r++){
      printf ("%d||",p_array[r]);
    }
    printf ("\n");

    if (size%2 == 0){
      if (i == size/2-1){
        break;
      }
    }
    else{
      if (i == size/2){
        break;
      }
    }
  }
}
    
