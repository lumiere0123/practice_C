#include <stdio.h>
#include <string.h>
int validName(const char *name);
int main(){
  printf("%s: Test: valid name\n",validName("ABC")==1? "PASS" : "FAIL");
  printf("%s: Test: valid name\n",validName("if")==0? "PASS" : "FAIL");
  printf("%s: Test: valid name\n",validName("33234A")==0? "PASS" : "FAIL");
  printf("%s: Test: valid name\n",validName("a__324G")==1? "PASS" : "FAIL");

  return 0;
}

int validName(const char *name){
  // x keyword
  char first = name[0];
  // first char x digit
  if (first = '0' && first <= '9'){
    return 0;
  }
  else{
    char key[39] ={0};
    char character =' ';
    FILE *keywords = fopen("keywords.txt","r");
     for (int n=0;character!=EOF;){
      character = fgetc(keywords);
      if (character != '\n'){
        key[n] =character;
        n++;
      }
      else{
        if (strcmp(key,name) ==0){
          return 0;
        }
        n=0;
        memset(key,0,39);
      }
    }
        
  // letter, digit, underscores
    for (int i=0;i<strlen(name);i++){
      if ((name[i] >= 'a' && name[i] <= 'z') || 
          (name[i] >= 'A' && name[i] <= 'Z')||
          (name[i] =='_') ||
          (name[i] >= '1' && name[i] <= '9')){
      }
      else{
        return 0;
      }
    }
  }
  return 1;
}
    
