#include <stdio.h>
int triple1(int x){
  return 3 * x;
}
void triple2(int x) {
  x = x * 3;
}
void triple3(int *p){
  p = p * 3;
}
int main(){
  int n;
  n = 5;
  printf("Before triple 1, n is %d\n",n);
  n = triple1(n);
  printf("After triple1, n is %d\n",n);
  triple2(n);
  printf("After triple2, n is %d\n",n);
  triple3(n);
  printf("After triple3, n is %d\n",n);
}
  
  
  
  
