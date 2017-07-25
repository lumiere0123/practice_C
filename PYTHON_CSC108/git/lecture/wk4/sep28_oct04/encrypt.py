def encrypt_letter(letter):
    '''(str) -> str
    Encrypt letter by shifting three places to the right.
    
    >>> encrypt_letter('v')
    'y'
    '''

    new_letter = ord(letter) + 3

    # Note: ord('z') == 122
    if new_letter > 122:  
        new_letter -= 26
    return chr(new_letter)

#######################################################

    # Here is an alternate solution that uses modulus:
    # base = ord('a')
    # return chr((ord(letter) + 3 - base) % 26 + base)

def encrypt_word(word):
    '''(str) -> str
    Return the given word encrypted using encrypt_letter on each 
    alphabetic character in the word.'''


    # Here is some foreshadowing of what we will be working on over 
    # the next few weeks: loops!    
    new_word = ""       # an accumulator
    for ch in word:
        if ch.isalpha():
            new_word += encrypt_letter(ch)
        else:
            new_word += ch
    return new_word