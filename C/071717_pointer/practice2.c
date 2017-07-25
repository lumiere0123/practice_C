#include <stdio.h>
int main(){
  int vowel = 0;
  int constant = 0;
  char a_vowel[5] ={'a','e','i','o','u'};
  char a[32];
  printf("Input a string: \n");
  scanf("%s",a);
  printf("%s",a);
  for (int i; i < 32 && a[i] != '\0'; i++){
    if ( a[i] == a_vowel[0] || 
       a[i] == a_vowel[1] || 
       a[i] == a_vowel[2] || 
       a[i] == a_vowel[3] || 
       a[i] == a_vowel[4] ){
      vowel++;
    }
    else{ 
      constant++;
    }
  }
  printf("Number of vowels : %d\n", vowel);
  printf("Number of constant : %d\n", constant);      
  
       
  return 0;
} 
