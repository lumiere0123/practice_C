#include <stdio.h>
int main(){
  FILE*cp = fopen ("copy","r");
  char comment = fgetc(cp);
  for (;comment!=EOF;){
    if (comment == '/'){
      comment = fgetc(cp);
      if (comment == '/'){
        printf("//");
        comment = fgetc(cp);
        for (;comment != '\n';){
          printf("%c",comment);
          comment = fgetc(cp);
        }
        printf("\n");
      }
    }
    else{
      comment = fgetc(cp);
    }
  }
  return 0;
}
