def count_uppercase(s):
    """ (str) -> int
    
    Return the number of uppercase letters in s.
  
    >>> count_uppercase("abcD EF")
    3
    """

    #this function demonstrates a numerical accumulator
    uppercase_count = 0
    for char in s:   
        #if char >= 'A'  and char <= 'Z':
        if char.isupper():
            uppercase_count = uppercase_count + 1
    return uppercase_count
        
    #Think of corner cases. What if I called count_uppercase() with the empty
    #string? Would it return the correct value? 

def all_fluffy(s):
    
    """ (str)-> bool
    
    Return True iff every letter in s is fluffy. Fluffy letters are
    those that appear in the word 'fluffy'.
 
    >>>all_fluffy("fly")
    True
    >>>all_fluffy("flap")
    False
    
    """
    #we can use fluffy_so_far as a boolean accumulator
    fluffy_so_far = True
    for ch in s:
        if not (ch in "fluffy"): #could use in "fluy", isolate the letters
            fluffy_so_far = False 
    return fluffy_so_far

    #Another solution would be to return from the function
    #the moment we find a non-fluffy letter.
    #
    #The return True at the end works because if we had found a
    #non-fluffy letter, we would never have reached that line of code.
    
    #for ch in s:
    #   if ch not in "fluffy":
    #        return False
    #return True


def add_underscores(s):
    
    """ (str) -> str
    
    Return s with an underscore between each pair of characters
  
    >>>add_underscores("hello")
    'h_e_l_l_o'
    """
    
    #Here we are using a string accumulator. 
    #Initially, we make word_accumulator refer to the empty string. 
    
    word_accumulator = ''
    for ch in s:
        word_accumulator = word_accumulator + ch + '_'
        #print(word_accumulator) 
        #the print statement was just a way for you to see what happens in 
        #every iteration, assuming you are not using the debugger.
    return word_accumulator[0:-1]
   
    #Notice how we got rid of the last underscore? We used -1 as end-index.
    
    #What if I called add_underscores() with the empty string? Or a single
    #character string. Would it still work?
    #Yes, it would, but you can test it!
