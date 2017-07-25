#include <stdio.h>
void print (int *a, int numElements);
int main(){
  int a[1548];
  int numElements;
  printf ("Test Data:\n");
  printf("Input the number of elements to store in the array:\n");
  scanf ("%d", &numElements);
  printf ("Intput %d number of elements in the array:\n", numElements);
  for (int i=0; i < numElements; i++){
    printf ("element -%d : ", i);
    scanf ("%d", &a[i]);
  }
  printf ("The elements you entered are : \n");
  for (int i = 0; i < numElements; i++){
    printf ("elements - %d : %d\n", i, a[i]);
  }
  print (a, numElements);
  return 0;
}

void print (int *a, int numElements){
  printf ("The elements you entered are : \n");
  for (int i = 0; i < numElements; i++){
    printf ("elements - %d : %d\n", i, *(a+i));
  }
}
    
  
