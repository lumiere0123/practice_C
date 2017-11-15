#include <stdio.h>
int validate(char *txt, int size);
int main(){
  char a[] = "{\"a\":1234}";
  char b[] = "{\"a\":1a34}";
  int size = sizeof(b);
  int result = validate (b, size);
  if (result == 0){
    printf ("Bad\n");
  }
  else{
    printf ("Good\n");
  }
  return 0;
} 


int validate(char *txt, int size){
  char cur;
  cur = *txt;
  if (cur == '{'){
    cur = *++txt;
  }
  else{
    return 0;
  }
  //printf ("debug1: %c\n",cur);
  if (cur == '"'){
    cur = *++txt;
  }
  else{
    return 0;
  }
  //printf ("debug2: %c\n",cur);
  for (; cur != '"'; txt++){ 
    cur = *txt;
    printf(" cur = %c\n",cur);
  }
  txt--;
  printf(" cur2.1 = %c\n",cur);
  if (cur == '"'){
    printf(" cur2.2 = %c\n",cur);
    printf(" cur2.3 = %c\n",*(txt+0));
    printf(" cur2.3 = %c\n",*(txt+1));
    cur = *++txt;
    printf(" cur2 = %c\n",cur);
  }
  else{
    return 0;
  }
  //printf ("debug3: %c\n",cur);
  if (cur == ':'){
    cur = *++txt;
  }
  else{
    return 0;
  } 
  //printf ("debug4: %c\n",cur);
  for (; '0' <= cur && cur <= '9'; txt++){
    cur = *txt;
  }
  txt--;
  //printf ("debug5: %c\n",cur);
  if (cur == '}'){
    cur = *++txt;
  }
  else{
    return 0;
  }
  return 1;
}
  

    
          
