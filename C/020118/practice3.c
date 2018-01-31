#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int strtoint(char* input);
int main(){
//  for (int i =0;i<=127; i++){
  printf("%s: TEST: strtoint(\"123\") <%d> == atoi(\"123\") <%d>\n",
  strtoint("123") == atoi("123")? "PASS" : "FAIL",strtoint("123"),atoi("123"));
  return 0;
}


int strtoint(char* input){
  int result=0;
  for (int i=0; i<3; i++){
    char c = input[i];
    result= result+(c-'0')*pow(10,2-i);
    printf("test: %d\n",result);
  }
  return result;
}
