/*/*
== Banking - Savings Account ==

Author	:
Date	:
Revision:
Workshop: #6 in-Lab

*/

#include <stdio.h>


// Structure Declaration for account
struct account
{
	int accNumber;				// Account number
	double balance;				// Balance of the account
};

/*  Function to add an amount if positive-valued */
double balanceUP(double balance, double amount){
  double result;
  if (amount >= 0){
    result = balance+amount;
  }
  return result;
} 

/* Function to calculate the interest rate*/
//
double interestCalc(double balance, double rate){
  double interest;
  interest = (balance*(rate/100));
  return interest;
}

double balanceDown (double balance, double amount){
  double result;
  if (amount >= 0){
    result = balance-amount;
  }
  return result;
} 
  


/* main program */
int main()
{
	const int nosClients = 5;				// Number of accounts
	int option;											// Hold the selection
	// Initialize the struct account array with opening balance
	struct account acct[] = { 
                           { 11111111, 123.45 },
                           { 22222222, 12365.50 },
                           { 33333333,0 },
                           { 44444444,1475 },
                           { 55555555,25000.65 } };
  int accNum;
  double amount;
	printf("***** Welcome to Savings Account Banking *****\n\n");

	do
	{
		// Print the option list
		printf("1.) Deposit \n");
		printf("2.) Withdraw\n");
		printf("3.) Apply monthly interest earnings to all accounts\n");
		printf("4.) Apply service charges to all accounts\n");
		printf("5.) Account Summary\n");
		printf("0.) Log out\n\n");
		printf("Please enter an option to continue: ");
		
		// Waiting for the input
		scanf("%d",&option);

		switch (option)
		{
		case 0: // Exit the program
			break;

		case 1: {// Deposit
				//@IN-LAB				
			int isEverFound =0 ;
      printf("Enter account number:\n");
      scanf ("%d",&accNum);
      for (int i=0; i<nosClients; i++){
        if (accNum == acct[i].accNumber){
          isEverFound =1;
          printf("Enter amount to deposit:");
          scanf (" %lf",&amount);
      //    printf("Debug: amount = %lf\n",amount);
      //    printf("Debug: balance = %lf\n",acct[i].balance);
          acct[i].balance = balanceUP(acct[i].balance, amount);
          printf("Current balance is:%.2lf\n",acct[i].balance);
        }
        //else{
          //isEverFound = 0;
        //}
      }
      if (!isEverFound ){
        printf("ERROR\n");
      }
			break;
    }

		case 2: {// Withdraw funds
				//@HOME
			int isEverFound =0 ;
      printf("Enter account number:\n");
      scanf ("%d",&accNum);
      for (int i=0; i<nosClients; i++){
        if (accNum == acct[i].accNumber){
          isEverFound =1;
          printf("Enter amount to withdraw:");
          scanf (" %lf",&amount);
      //    printf("Debug: amount = %lf\n",amount);
      //    printf("Debug: balance = %lf\n",acct[i].balance);
          if (balanceDown(acct[i].balance,amount) >= 0){
            acct[i].balance = balanceDown(acct[i].balance, amount);
            printf("Current balance is:%.2lf\n",acct[i].balance);
          }
          else{
            printf(
            "ERROR:The maximum amount that can be withdrawn is %lf\n",
            acct[i].balance);
          }     
        }
      }
      if (!isEverFound ){
        printf("ERROR\n");
      }

			break;
    }
    

		case 3: {// Apply interest earnings to all accounts
				//@IN-LAB
			double rate;
      double calcInterest;
      printf("Account# New Balance Interst Earnings (M)\n");
      printf("-----------------------------------------\n");
      for (int i=0; i<nosClients; i++){
        if (acct[i].balance <= 500){
          rate = 0.99;
        }
        if (acct[i].balance >500 && acct[i].balance <=1500 ){
          rate = 1.66;
        }
        if (acct[i].balance >1500){
          rate = 2.49;
        }
        calcInterest=interestCalc(acct[i].balance, rate);
        acct[i].balance = balanceUP(acct[i].balance,calcInterest);        
        printf("%8d %11.2f %21.2lf\n",
                acct[i].accNumber,acct[i].balance,calcInterest);
      }

			break;
    }

		case 4: {// Apply Service Charges
				//@HOME
			double service;
      printf("Account# New Balance Service Charge (M)\n");
      printf("---------------------------------------\n");
      for (int i=0; i<nosClients; i++){
        if (acct[i].balance <= 1500){
          service = 7.50;
        }
        if (acct[i].balance > 1500){
          service = 2.50;
        }
        acct[i].balance = balanceDown(acct[i].balance,service); 
        printf("%8d %11.2lf %19.2lf\n",
                acct[i].accNumber,acct[i].balance,service);
        } 

			break;
    }

		case 5: // Display Account Information
				//@IN-LAB
      printf(">Account# Balance   <\n");
      for(int i=0; i<nosClients; i++){
        printf("%8d %10.2lf\n",acct[i].accNumber, acct[i].balance);
      }

			break;

		default:
			printf("Error: Please enter a valid option to continue\n\n");
			break;
		}


	} while (option != 0);


	return 0;
}


/* SAMPLE INPUT/OUTPUT EXPECTED */
/*
***** Welcome to Savings Account Banking *****

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 5

-- Account information --

Account# Balance
-------- ----------
11111111     123.45
22222222   12365.50
33333333       0.00
44444444    1475.00
55555555   25000.65

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 1

-- Make a deposit --

Enter account number: 67676767
ERROR: Account number does not exist.

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 1

-- Make a deposit --

Enter account number: 44444444
Enter amount to deposit (CAD): 20
Current balance is : 1495.00

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 1

-- Make a deposit --

Enter account number: 11111111
Enter amount to deposit (CAD): 450.67
Current balance is : 574.12

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 5

-- Account information --

Account# Balance
-------- ----------
11111111     574.12
22222222   12365.50
33333333       0.00
44444444    1495.00
55555555   25000.65

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 3

-- Add monthly interest earnings to all accounts --

Account# New Balance Interest Earnings (M)
-------- ----------- ---------------------
11111111      583.65                  9.53
22222222    12673.40                307.90
33333333        0.00                  0.00
44444444     1519.82                 24.82
55555555    25623.17                622.52

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 5

-- Account information --

Account# Balance
-------- ----------
11111111     583.65
22222222   12673.40
33333333       0.00
44444444    1519.82
55555555   25623.17

1.) Deposit
2.) Withdraw
3.) Apply monthly interest earnings to all accounts
4.) Apply service charges to all accounts
5.) Account Summary
0.) Log out

Please enter an option to continue: 0

*/
