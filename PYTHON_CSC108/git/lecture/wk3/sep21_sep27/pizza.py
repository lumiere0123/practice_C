# Original problem description:
# Adults order two slices, boys order three slices, and girls order one slice. 
# Each pizza has eight slices. Write a function that takes three parameters 
# representing the number of adults, boys, and girls, and returns the required 
# number of pizzas. 

def num_pizzas(adults, boys, girls):
    '''(int, int, int) -> int
    Return the number of pizzas required to feed the specified number of adults 
    (2 slices), boys (3 slices), and girls (1 slice), assuming that each pizza
    has 8 slices.
    >>> num_pizzas(1, 1, 1)
    1
    >>> num_pizzas(0, 0, 16)
    2
    >>> num_pizzas(0, 3, 0)
    2
    '''

    return (adults * 2 + boys * 3 + girls + 7) // 8

    # To find a good solution to this problem, we enumerated (listed) slices from
    # 0 to 17 and determined what we wanted the answer to be for each number of 
    # slices. We looked for patterns in this table of slices -> pizzas, and we saw
    # that there were blocks of 8 slices that would generate the same number of 
    # pizzas. That's great, because it means that division by 8 is a part of the answer.
    # Then, we had to add (or subtract) from the number of slices to make the division
    # work cleanly.
