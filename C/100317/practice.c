#include <stdio.h>
#include <math.h>
int binary (int n, int a);
int main (){
  printf("%d\n",binary(10,0));
  printf("%d\n",binary(11,0));
  return 0;
}

int binary (int n, int a){
  if (n == 1){
    return 1 * pow (10, a);
  }
  return binary(n/2,a+1)+ n%2 * pow(10,a);
}
