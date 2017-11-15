#include <stdio.h>
#include <math.h>
int add( int a);
int factorial (int b);
int fib ();
int fib2(int c);
int binary (int n);
int main(){
  int result;
//  result = factorial (5);
//  printf ("%d",result); 
 // printf ("%d\n",fib(7));
 // printf ("%d\n",fib2(7));
  printf ("%d\n",binary(13));
  return 0;
}

int add( int a){
  if (a == 0){
    return 0;
  }

  int result =0;
  result = add(a-1) + a;
  return result;
}


int factorial (int b){
  if ( b == 1){
    return 1;
  }
  int result = 1;
    result = factorial(b-1) * b;
  return result;
}


int fib (int e){
  int r = 1;
  int c = 1;
  int d = 1;
  for (int i = 1; i <= e - 2; i++ ){
    r = c+d;
    c = d;
    d = r; 
  }
  return r;
}

int fib2(int c){
  if ( c == 1 || c == 2){
    return 1;
  }
  return fib2(c -2 )+ fib2(c-1);
}

int binary (int n){
  int result = 0;
  int m ;
  for ( m = 0; n !=0 ; m++){
    result = result + (n%2)*pow(10,m);
    n = n/2;
    // result = result + 1*pow(10,m+1);

  }
  result = result + 1*pow(10,m);
  return result;
}
  
