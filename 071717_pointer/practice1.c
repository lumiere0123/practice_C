#include <stdio.h>
void swap(int *first, int *second, int *third);
int main(){
  int first = 5;
  int *p_first = &first;
  int second = 6;
  int *p_second = &second;
  int third = 7;
  int *p_third = &third;
  int first_c = *p_first;
  int second_c = *p_second;
  int third_c = *p_third;
  printf("The value before swapping are : \n");
  printf("element 1 = %d\n", first);
  printf("element 2 = %d\n", second);
  printf("element 3 = %d\n", third);
  *p_first = third_c;
  *p_second = first_c;
  *p_third = second_c;
 
  printf("The value after swapping are : \n");
  printf("element 1 = %d\n", first);
  printf("element 2 = %d\n", second);
  printf("element 3 = %d\n", third);
  
  swap(p_first, p_second, p_third);
  printf("The value after swapping are : \n");
  printf("element 1 = %d\n", first);
  printf("element 2 = %d\n", second);
  printf("element 3 = %d\n", third);
  return 0;
}
  
void swap(int *first, int *second, int *third){
  int first_c = *first;
  int second_c = *second;
  int third_c = *third;
  *first = second_c;
  *second = first_c;
  *third = third_c;
}
