#include <stdio.h>
void swap(int *p_a, int*p_b);
int main(){
  int a = 3;
  int b = 8;
  swap (&a, &b);
  printf ("%d , %d\n",a,b);
  return 0;
}


void swap(int *p_a, int*p_b){
  int c = *p_a;
  int d = *p_b;
  *p_a = d; 
  *p_b = c;
}
  
  
