#include <stdio.h>
void swap (int *p_a, int *p_b);
int main(){
  int a = 3;
  int b = 4;
  swap (&a,&b);
  printf ("%d, %d", a,b);
  return 0;
}


void swap (int *p_a, int *p_b){
  int c = *p_a;
  *p_a = *p_b; 
  *p_b = c;
}
   
