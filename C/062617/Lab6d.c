#include <stdio.h>
int gettime1(void){
  int h, m;
  printf ("Enter a time (e.g. 12:45) - ");
  scanf ("%d:%d", &h, &m);
  return 100*h + m;
}
void gettime2(int *ph, int *pm){
  printf ("Enter a time (e.g. 12:45) - ");
  scanf ("%d:%d", ph, pm);
}
int main(){
  int hr, min, time;
  time = gettime1();
  printf("You entered %d:%02d\n", time/100, time%100);
  gettime2(&hr, &min);
  printf("You entered %d:%02d\n", hr, min);
}
