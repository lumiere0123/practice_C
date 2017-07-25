#Ask the user to enter a number greater than 100.
#Keep on prompting until the user enters a valid number.

#input() returns a string so we need to convert it to int
#in order to compare it with number 100.
guess = int(input('Enter a number greater than 100: '))

#Fill this code in..

while not guess > 100: 
    guess = int(input('Enter a number greater than 100: '))
    
#an alternative while loop condition could be:
#while guess <= 100:
