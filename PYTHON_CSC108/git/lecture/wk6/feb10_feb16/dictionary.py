def is_correct(dictionary, word):
    """(file open for reading, str) -> bool
    
    Return True iff word is a correctly-spelled word in dictionary.
    
    >>>dict1 = open('dict.txt', 'r')
    >>>is_correct(dict1, "Zyrtec")
    True
    >>>dict1.close()

    >>>dict1 = open('dict.txt', 'r')
    >>>is_correct(dict1, "lolz")
    False
    >>>dict1.close()
    """
    
    for line in dictionary:
        if line[:-1] == word:
            return True
    return False

    #At first our if statement was:
    #if line == word
    #This didn't work because line includes the new-line character '\n'.
    #So to get rid of this (i.e., not include it in our string comparison)
    #we had to use slicing.
    
    #There was a question as to why we do line[:-1] instead of line[:-2]
    #The new line character is considered a single character and not two.
    #The expression len('\n') evaluates to  1.
    
    #Could we use readlines()? Yes, here's how:
    #lines_list = dictionary.readlines()
    #for line in lines_list:
    #    if line[:-1] == word:
    #        return True
    #return False
        
