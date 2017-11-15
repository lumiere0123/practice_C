#include <stdio.h>
int length (char *p_a);
int main (){
 // char a[] = "hello";
 // printf ("%s\n",&a[0]);
 // a[1] = 'E';
  char a[10000];
  printf ("Input a string: \n");
  scanf ("%s",a);
  printf ("The length of the given string %s is: %d\n", a, length (a));
  //printf ("The length of the given string %s is: %d\n", &a[0], length (&a[0]));
  return 0;
}



int length (char *p_a){
  int count;
  for (int i = 0; *(p_a+i) != '\0'; i++){ 
  //for (int i = 0; p_a[i] != '\0'; i++){ 
    count ++;
  }
  return count;
}
