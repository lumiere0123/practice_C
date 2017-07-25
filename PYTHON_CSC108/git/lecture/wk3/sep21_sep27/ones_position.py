def ones_position(num):
    '''(int) -> int
    Return the number in the one's position of the given integer.
    
    >>> ones_position(3)
    3
    >>> ones_position(547)
    7
    '''
    
    # Which of the answers below do you prefer? Why?
    # return num % 10
    # return int(str(num)[-1])

def get_digit_at_position(num, position):
    '''(int) -> int
    Return the number in the specified position of the given integer.
    
    >>>  get_digit_at_position(3, 0)
    3
    >>>  get_digit_at_position(547, 0)
    7
    >>>  get_digit_at_position(547, 1)
    4
    >>>  get_digit_at_position(547, 2)
    5
    >>>  get_digit_at_position(547, 3)
    0
    '''
    
    # Which of the answers below do you prefer? Why?
    # return num / (10 ** position) % 10
    # return int(str(num)[-(position + 1)])