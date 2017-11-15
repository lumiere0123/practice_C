#include <stdio.h>
void compare (int *a);
void print2 (int *a);
void timer();
int main(){
  int array[] = {5,4,1,3,2,0,9,6,8,7};
  printf ("--------------------------------------------------\n");
  compare (array);
  printf ("\n--------------------------------------------------\n");
  return 0;
}


void compare (int *a){
  int v = 9;
  for (int b = 0; b < v; b++){
    for (int i = 0; i < v; i++){
      if (a[i] > a[i+1]){
       int copy = a[i];
       a[i] = a[i+1];
       a[i+1] = copy;
       print2(a); 
      }
    }
    v = v-1;
  }
}    
    
void print2 (int *a){
  for (int i = 0; i < 10; i++){
    printf ("| %d |", a[i]);
  }
  printf ("\r");
  fflush(stdout);
  timer();
  
}
  
void timer(){
  long long sum = 0;
  for (long long i =0; i<100000000; i++){
    sum += i;
  }
}
