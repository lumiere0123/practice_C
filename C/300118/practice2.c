#include <stdio.h>
int main(){
  FILE *data = fopen("practice3.txt","r");
  if (data == 0){
    printf ("no file\n");
  }
  else{
    int product;
    double price;
    for (;fscanf (data,"%d %lf",&product,&price) ==2;){
      printf ("%d %lf\n",product, price);
    }
  }
  return 0;
}
