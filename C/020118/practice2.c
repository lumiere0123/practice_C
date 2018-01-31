#include <stdio.h>
#include <ctype.h>
int space(char input);
char lowercase(char input);
int main(){ 
 int True =0;
 int False =1;
 int result1 = 0;

  for (int i =0;i<=127; i++){
    printf("%s: TEST: space(%d) <%d> == isspace(%d) <%d>\n",
    space(i) == isspace(i)? "PASS" : "FAIL",i,space(i),i,isspace(i));
  }
 return 0;
}

char lowercase(char input){
  int output;
  // change uppercase to lower
  if (input >= 'A' && input <= 'Z'){ 
    output = input+('a' -'A');
  }
  // keep the input same 
  else{
    output = input;
  }
  return output;
}


int space(char input){
  char whitespace[] = {'\n', '\t', '\v', '\f','\r',' '};  
  for (int i=0;i<6;i++){
    if (input == whitespace[i]){
      return 8;
    }
  }
  return 0;
}
