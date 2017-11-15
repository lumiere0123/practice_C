#include <stdio.h>
void alph (char*p_alpha);
int main(){
  char alpha[26]; 
  alph(alpha);
  for (int i = 0; i < 26; i++){
    printf ("%c ",alpha[i]);
    printf ("%c ", *(alpha+i));
  }
  printf("\n");
  return 0;
}

void alph (char*p_alpha){
  char temp = 65;
  for (int i = 0; i < 26; i++){
    *(p_alpha+i) = temp +i;
  }
} 
    
    
