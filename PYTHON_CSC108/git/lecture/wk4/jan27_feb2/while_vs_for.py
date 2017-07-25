#For loop over string
s = "computer"

for char in s:
    print(char)

#Can you do the same with a while loop?
i = 0
while i < len(s):
    print(s[i])
    i = i + 1 
    
#At first, we didn't have the i = i + 1 statement.
#We ran this through the debugger and saw this was an infinite loop.
#Only the first letter 'c' was printed on the screen non-stop.
#Why? What was the initial value of i? Did we ever change it?
#Did i < len(s) ever evaluate to False?

#Think about why i = i + 1 should be **after** the print statement
#and not before. 

#Also, why do we have i < len(s) instead of i <= len(s)?
    
