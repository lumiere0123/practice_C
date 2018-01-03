#include <stdio.h>
void findNum(int a, int b, int c){
    
  int big = 0;
  int mid = 0;
  int small = 0;
   
  if (a > b){
    int copy_a = a;
    a = b;
    b = copy_a;
  }
  if (b > c){
    int copy_b =b;
    b = c;
    c = copy_b;
  } 
  if (a > b){
    int copy_a = a;
    a = b;
    b = copy_a;
  } 
  big =c;
  mid =b;
  small =a;
    
    
   printf("big: %d mid: %d small:%d\n",    big, mid, small);

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
