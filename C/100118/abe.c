#include <stdio.h>
int main(){
  FILE *co = NULL;
  co =fopen ("a1.exe","r");
  char character = ' ';
  //for (int n=0;character!=EOF;){
  for (int n=0;n < 200; n++){
   character = fgetc(co);
    //printf("hex %x\n",character);
    if ((character >= 'a' && character <= 'z') ||
       (character >= 'A' && character <= 'Z')){
      printf("%c",character);
    }
    else{
      printf(".");
    }
  }
  return 0;
}
