#include <stdio.h>
void alpha(char *p_chara);
void print(char *p_array);
int main(){
  char chara = 'A';
  char *p_chara = &chara;
  for (int i = 0; i < 26; i++){
    printf ("%c\n", *p_chara + i);
  }
  char array[18];
  alpha(array);
  print(array);
  
  return 0;
}

void alpha(char *p_chara){
  for (int i = 0; i < 18; i++){
    *(p_chara + i) = 'A'+i; 
  }
}

void print(char *p_array){
  for (int i = 0; i < 18; i++){
    printf ("%c\n",*(p_array + i));
  }

}

 


