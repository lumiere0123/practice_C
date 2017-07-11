#include <stdio.h>
int length (char *string);
int main (){
  char string[453];
  char a[32];
  int result;
  a[0] = 'H';
  a[1] = 'e';
  a[2] = 'l';
  a[3] = 'l';
  a[4] = 'o';
  a[5] = '\0';
  a[1] = 'E';
  printf ("%s\n",a);
  char *b = "hello";
//  *(b+1) = 'E';
//  b[1] = 'E';
  for (int i =0; i<453; i++){
    string[i] = '!';
  }
  printf("%s\n", b);
  printf ("Test Data:\n");
  printf ("Input a string: ");
  scanf ("%s",string);
  result = length (string);
  printf ("The length of the given string %s is : %d", string, result);
  
  
  return 0;
}

int length (char *string){
  for (int i = 1; i > 0; i++){
    if (string [i] == '!'){
 //    break;
      return i;
    }
  }
  return 0;
} 
