#include <stdio.h>
int cut (int input);
int main(){
  printf ("%d\n",cut(987654321));

  return 0;
}


int cut (int input){
  int array[100];
  int i;
  int sum = 0;
  printf("------------%d\n",input);
  for (i = 0; input > 10; i++){
    array[i] = input %10;
    input = input/10;
    printf ("input: %d\n", input);
  }
  array[i] = input;
  printf ("input2: %d\n", input);
  
  int divisors[] = {1,10,9,12,3,4};
  for (int j = 0; j < i+1; j++){
    sum += divisors[j%6]*array[j];
    printf ("sum: %d\n",sum);
  }
  printf("A%d\n",sum);
  if ( input == sum){
    return input;
  }
  else{
    return cut (sum);
  }

}
    
