#include <stdio.h>
void findNum(int a, int b, int c){
  
  int max;
  int med;
  int min;
 
  if (a>b && a>c){
    max = a;
  }
  else if (b>c && b>a){
    max = b;
  }
  else{
    max = c;
  }

  if (a<b && a<c){
    min = a;
  }
  else if (b<c && b<a){
    min = b;
  }
  else{
    min = c;
  }

    
   printf("big: %d mid: %d small:%d\n",    max, med, min);

}

int main(){

    int a, b, c;

    a=1, b=2, c=3; printf("Test: a=%d, b=%d, c=%d ", a, b, c); findNum(a,b,c);
    a=1, b=3, c=2; printf("Test: a=%d, b=%d, c=%d ", a, b, c); findNum(a,b,c);

    a=2, b=1, c=3; printf("Test: a=%d, b=%d, c=%d ", a, b, c); findNum(a,b,c);
    a=2, b=3, c=1; printf("Test: a=%d, b=%d, c=%d ", a, b, c); findNum(a,b,c);

    a=3, b=2, c=1; printf("Test: a=%d, b=%d, c=%d ", a, b, c); findNum(a,b,c);
    a=3, b=1, c=2; printf("Test: a=%d, b=%d, c=%d ", a, b, c); findNum(a,b,c);
}
