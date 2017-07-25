#include <stdio.h>
int main(){
  int m;
  int *z = &m;
  printf ("z stores the address of m = %p\n", z);
  m = 10;
  printf ("*z stores the value of m = %d\n", *z);
  printf ("&m is the address of m = %p\n", &m);
  return 0;
}

