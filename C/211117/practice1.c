#include <stdio.h>
#include <string.h>
struct stack_t{
  char stg[20];
  int size ;
  int counter;
};

int isPair (char *input);
int isPair2 (char *input,struct stack_t *s);
void push(struct stack_t *s,char in);
char pop (struct stack_t *s);
char peek (struct stack_t *s);
int isFull(struct stack_t *s);
int isEmpty(struct stack_t *s);

void init(struct stack_t *s1){
  (*s1).size = 20;
  s1->counter = 0;
}

int main(){
//  push ('a'); 
//  push ('b'); 
//  push ('c'); 
//  push ('d'); 
//  push ('e'); 
//  push ('f'); 
//  push ('f'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//  push ('e'); 
//
//  printf ("Peek: %c\n",peek());
//
//  printf ("Pop: %c\n", pop());
//  printf ("Pop: %c\n", pop());
//  printf ("Pop: %c\n", pop());
//  printf ("Pop: %c\n", pop());
//  printf ("Pop: %c\n", pop());
//  printf ("Pop: %c\n", pop());
 
  struct stack_t s1; init (&s1);
  struct stack_t s2; init (&s2);
  struct stack_t s3; init (&s3);
  struct stack_t s4; init (&s4);
  struct stack_t s5; init (&s5);
  struct stack_t s6; init (&s6);

  printf("Testing bad\n");
  char input1[]="{{}";  printf("%s: isPair: %d\n", input1, isPair2(input1,&s1));
  char input3[]="{{";   printf("%s: isPair: %d\n", input3, isPair2(input3,&s3));
  char input6[]="}}{{"; printf("%s: isPair: %d\n", input6, isPair2(input6,&s6));

  printf("Testing good\n");
  char input2[]="{}";   printf("%s: isPair: %d\n", input2, isPair2(input2,&s2));
  char input4[]="{}{}"; printf("%s: isPair: %d\n", input4, isPair2(input4,&s4));
  char input5[]="{{}}"; printf("%s: isPair: %d\n", input5, isPair2(input5,&s5));
  return 0;
}



int isPair (char *input){
  int open = 0;
  int close = 0;
  for (int i = 0; i<strlen(input); i++){
    if (input[i] == '{'){
      open++;
    }
    else if (input[i] == '}'){
      close++;
    }
  }
  if ( open - close == 0){
    return 1; 
  }
  else{
    return 0;
  }
}
  
int isPair2 (char *input,struct stack_t *s){
  int close =0;
  for (int i =0; i < strlen(input); i++){
    if (input [i] != '{'){
      close++;
      if (isEmpty(s)){
        return 0;
      }
      else{
        pop(s);
      }
    }
    else{
      push(s,input[i]);
    }
  }
  if (isEmpty(s)){
    return 1;
  }
  else {
    return 0;
  }
}
    
  
void push(struct stack_t *s,char in){
  if (!isFull(s)){
    s->stg[s->counter] = in;
    s->counter++;
  }
  else{
    printf ("ERROR\n");
  }
}

char pop (struct stack_t *s){
  char out;
  if (isEmpty(s)){
    printf ("ERROR: pop\n");
    return ' ';
  }
  else{
    out = s->stg[s->counter-1];
    s->counter--;
    return out;
  }
} 

char peek (struct stack_t *s){
  if (isEmpty(s)){
    return ' ';
  }
  else{
    char top = s->stg[s->counter-1];
    return top;
  }
}

int isFull(struct stack_t *s){
  if (s->size == s->counter){
    return 1;
  }
  else{
    return 0;
  } 
}

int isEmpty(struct stack_t *s){
  if (s->counter == 0){
    return 1;
  }
  else{
    return 0;
  }
}
