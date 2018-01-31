#include <stdio.h>
struct stud {
  int id;
  int grade;
};
void print_2 (char * name, struct stud student);
void info (struct stud * student, int ID, int grade);
int main(){
  struct stud john;
  struct stud david;
//  john.id = 1;
//  john.grade = 100;
//  david.id = 2;
//  david.grade = 139;
//  printf ("John:%d, Grade: %d\n",john.id, john.grade);
//  printf ("David:%d, Grade: %d\n",david.id, david.grade);
  info (&john,1,100);
  info (&david,2,139);
  print_2("john",john);
  print_2("david",david);
  return 0;
}

void print_2 (char * name, struct stud student){
  printf ("%s ID:%d, Grade: %d\n",name, student.id, student.grade);
}

void info (struct stud * student, int ID, int grade){
  (*student).id = ID;
  student->grade = grade;
}


