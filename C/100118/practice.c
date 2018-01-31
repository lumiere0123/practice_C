#include <stdio.h>
int main(){
  FILE *co = NULL;
  co =fopen ("practice2.c","w");
  if (co == NULL){
    printf("Error\n");
  }
  else{
    printf("success\n");
      char a = 'o';
      fputc('o',co);
      fputc('2',co);
      fputc('r',co);
      fputc('o',co);
  }
  return 0;
}
