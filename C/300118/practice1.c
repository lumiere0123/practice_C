#include <stdio.h>
int main(){
  FILE *copy =fopen ("copy","r");
  char ch =fgetc (copy);
  for (;ch != EOF;){
    printf("%c",ch);
    ch = fgetc (copy);
  }
  return 0;
}
  
