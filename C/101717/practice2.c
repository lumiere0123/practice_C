#include <stdio.h>
void ask (int *p_a, int num);
void sum (int *p_a, int num);
int main(){
  int num;
  printf ("Input the number of elements:\n");
  scanf ("%d", &num);
  int array [num];
  int *p_a = &array[0];
  ask (&array[0], num);
  sum (array, num);

  return 0;
} 
    
void ask (int *p_a, int num){
  for (int i = 0; i<num; i++){
    printf ("element - %d : \n",i);
    scanf ("%d", p_a + i);
  } 
}

void sum (int *p_a, int num){
  int sum = 0;
  for (int i = 0; i < num; i++){
    sum = sum + *(p_a + i);
  } 
  printf ("The sum of the array is : %d",sum);
}
 
