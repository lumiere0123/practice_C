#include <stdio.h>

#define size 3
  
int isValid (long long phoneNum){
  //phoneNum 6475551212
  int true = 1;
  int valid = false;
  int false =0;
  int area [3] = {416, 647, 905}; 
  int areacode;
  int prefix;
  int lll;
  decompose (phoneNum,&areacode,&prefix,&lll);
  for (int i=0; i<3; i++){
   // if (== area[i] && phoneNum/10000 %1000 <= 999 && phoneNum/10000 %1000 >= 100){
    if (areacode== area[i] && prefix <= 999 && prefix>= 100){
      valid = true;
      break;
    }
  }
  return valid;
} 

void decompose (long long phoneNumber, int*AAA ,int*PPP ,int*LLLL){
  *AAA = phoneNumber/10000000; 
  *PPP = phoneNumber /10000 %1000;
  *LLLL = phoneNumber%10000;
}

/* main program */
int main(void) {
  long long phoneNumber[size] = {0};
  int counter =0;
  int area;
  int prefix;
  int line;

  int option;
  
	printf("---=== Phone Numbers ===---\n\n");

	do {
		// Display the Option List
		printf("1. Display Phone List\n");
		printf("2. Add a Number\n");
		printf("0. Exit\n\n");
		printf("Please select from the above options: ");
		scanf("%d", &option);
 //   option = 2;
		printf("\n");

		switch (option) {
		case 0:	// Exit the program

      printf("Exiting Phone Number APP.Good Bye!!!");
      break;

		case 1: // Display the Phone List
				// @IN-LAB
			printf("Phone Numbers\n");
			printf("==============\n");
			// Display each number in decomposed form
      for (int i =0; i<counter; i++){
        decompose(phoneNumber[i],&area,&prefix,&line);	
        printf("(%3d) - %3d - %4d\n",area, prefix, line);
      }  
      printf("\n");
      break;

		case 2:	// Add a Phone Number
      printf("Add a Number\n");
      printf("============\n");
				// @IN-LAB
      if (counter == size){
        printf("ERRORR!!! Phone Number List is Full\n");
      }
      else{
        scanf("%lld",&phoneNumber[counter]);
       // phoneNumber[counter] = 6475551212;
      //  option = 0;
      //  printf("debug: %d",isValid(phoneNumber[counter]));
        if (isValid(phoneNumber[counter]) ){
          counter++;
        }
        else{
          printf ("ERROR! Phone number is not valid\n");
        }
      }   
      
      break;

		default:
      printf ("Error: Incorrect Option\n"); 
		}

	} while (option != 0);

	return 0;
}


