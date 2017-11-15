#include <stdio.h>
void ask(int *p_first, int n);
int getLargest(int *p_first, int n);
int main (){
  int size;
  printf ("Input total number of elements ( 1 to 100 ):\n");
  scanf ("%d", &size);  
  int elements [size];
  ask (&elements[0],size);
  printf ("The largst element is: %d", getLargest (&elements[0],size));
  return 0;
}


void ask(int *p_first, int n){
  for (int i = 0; i < n; i++){
    printf ("Number %d: \n", i+1);
    scanf ("%d", p_first + i);
  }
}

int getLargest(int *p_first, int n){
  int largest = 0;
  if (n == 1){
    return *p_first;
  }
  if (p_first[0] < p_first[1]){
  //if (*p_first < *(p_first + 1)){
    largest = *(p_first + 1);
  }
  else {
    largest = *p_first;
  }
  for (int i = 2; i < n-1; i++){
   // if ( largest < *(p_first + i)){
   //   largest = *(p_first + i);
    if ( largest < p_first[i]){
      largest = p_first[i];
    }
  }
  return largest;
} 
