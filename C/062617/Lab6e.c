#include <stdio.h>
#define VALID12HR 1
#define VALID24HR 2
#define NOHR 0
// classify time
// return 1 if time is in 12hr format
// return 2 if time is in 24hr format
// return 0 if time is not in correct format 
int gettime(int *ph, int *pm){

  if (
      (*ph >= 1 && *ph <= 12) &&  // check hour
      (*pm >= 0 && *pm <=59)      // check min
     )
  {
    return VALID12HR;
  }
  else if (((*ph == 0) || (*ph >= 13 && *ph <= 23)) &&
           (*pm >=0 && *pm<=59)){
    return VALID24HR;
  }
  else{
    return NOHR;
  }
}
int main(){
  int h;
  int m;

  // check if valid for 12hr time
  printf("Enter time(12):\n");
  scanf("%d:%d", &h, &m);
  while (gettime(&h, &m) != VALID12HR){
    printf("Enter time(12):\n");
    scanf("%d:%d", &h, &m);
  }
  
  // check if valid for 24hr time
  printf("Enter time(24):\n");
  scanf("%d:%d", &h, &m);
  while (gettime(&h, &m) != VALID24HR){
    printf("Enter time(24):\n");
    scanf("%d:%d", &h, &m);
  }

}
