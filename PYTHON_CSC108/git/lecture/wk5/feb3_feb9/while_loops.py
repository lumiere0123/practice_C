def find_letter_n_times(s, letter, n):
    """ (str, str, int) -> str
    
    Precondition: letter occurs at least n times in s
    
    Return the smallest substring of s starting from index 0 that contains
    n occurences of letter.
    
    >>>find_letter_n_times('Computer Science', 'e', 2)
    'Computer Scie'
    """
    
    i = 0
    count = 0
    
    #while count < n: #that's also a valid condition. 
    #But while count <= n is not. Why?
    while count != n:
        if s[i] == letter:
            count = count + 1
        i = i + 1
    return s[:i]

#find_letter_n_times - Questions to think about:
#(1) How would you modify your code if the precondition was not there?
#(i.e., there was no guarantee that letter appears n times in s)?
# Try running this example which violates the precondition:
#    find_letter_n_times("apple", "a", 2)
# Hint: To fix the error from the example above, you need an additional 
#condition to exit the while loop

# (2) Why do we return s[:i] and not s[:i+1] which would include the 
#character at index i? 
# Hint: Think about when we increment i. Is it before or after we read s[i]?

def count_collatz_steps(n):
    
    """(int) -> int

    Precondition n > 0    
    
    Return the number of steps it takes to reach 1, by applying the two 
    steps of the Collatz conjecture beginning from n.
    
    >>>count_collatz_steps(6)
    8
    """
    
    steps = 0
    while n != 1:
        if n % 2 == 0: #even number
            n = n // 2 #integer division
            #steps = steps + 1
        else: #odd number
            n = n * 3 + 1
            #steps = steps + 1
        #It's better to write steps = steps + 1 once, outside the if-else
        #statement, and not replicate it twice. Remember that steps should
        #be incremented in all cases (both for an even and an odd number)
        steps = steps + 1
    return steps
            
#count_collatz_steps - Notes:
#(1) Does count_collatz_steps(1) return the correct result? Yes. It returns 0
#(2) Remember we use modulo 2 to find if a number is even or odd.
            

#Part 4. Fill in function header and docstring

def mystery_function(s):
    """(str)  -> int

    Return the number of characters in s  until first digit
    or the length of s if there are no digits.

    >>> mystery_function("abc123")
    3

    >>> mystery_function("abcabc")
    6
    """
    #You can rephrase the first part of the docstring description as:
    #Return the index of the first digit in s or the len(s) if there are no
    #digits
    
    #first_digit would be a more appropriate name than mystery_function
    
    i = 0
    while i < len(s) and s[i] not in '0123456789':
        i = i + 1
    return i

#mystery_function - Notes:
# Try to identify every variable in the code and its purpose.
# Figure out if it's a function parameter or not.
# Find out the type of each variable.
#
# Question to ponder:
# We assumed s is a string, but could it also be a list of strings?
# Would this example work too? mystery_function(["a", "abc", "12", "a"])
