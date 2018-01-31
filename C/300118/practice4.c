#include <stdio.h>
void printAr (int *ar,int size);
int getHighest (int *ar, int size);
int main(){
  int act;
  int exp;
// Test 1
  int ar[5] = {9,5,4,2,6};
  act = getHighest(ar,5);
  exp = 9;
  if (act == exp){ printf ("Success\n",act); }
  else{ printf("Fail:"); printAr(ar,5); printf("exp: %d, act: %d",exp,act); }
  //Test 2
 int ar2[5] = {5,9,4,2,6};
  act = getHighest(ar2,5);
  exp = 9;
  if (act == exp){ printf ("Success\n",act); }
  else{ printf("Fail:"); printAr(ar2,5); printf("exp: %d, act: %d",exp,act); }
  //Test 3
 int ar3[5] = {5,4,9,2,6};
  act = getHighest(ar3,5);
  exp = 9;
  if (act == exp){ printf ("Success\n",act); }
  else{ printf("Fail:"); printAr(ar3,5); printf("exp: %d, act: %d",exp,act); }
  //Test 4
 int ar4[5] = {5,2,4,9,6};
  act = getHighest(ar4,5);
  exp = 9;
  if (act == exp){ printf ("Success\n",act); }
  else{ printf("Fail:"); printAr(ar4,5); printf("exp: %d, act: %d",exp,act); }
  //Test 5
 int ar5[5] = {5,6,4,2,9};
  act = getHighest(ar5,5);
  exp = 9;
  if (act == exp){ printf ("Success\n",act); }
  else{ printf("Fail:"); printAr(ar5,5); printf("exp: %d, act: %d",exp,act); }

  return 0;
}
   

int getHighest (int *ar, int size){
  int highest;
  highest = ar[0];
  for (int n=0;n<size;n++){
    if (highest > ar[n]){
//      highest = highest;
    }
    else{
      highest = ar[n];
    }
  }
  return highest;
}

void printAr (int *ar,int size){
  printf("[");
  for (int n=0; n<size;n++){
    printf("%d,",ar[n]);
  }
  printf("]");
}
