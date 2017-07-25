# Size: for collections, empty, 1 item, smallest interesting case, several items
# Dichotomies: (e.g., vowels/non-vowels, even/odd, positive/negative, etc.)
# Boundaries:
#    If a function behaves differently for a value near a particular threshold
#    (i.e. an if statement checking when a value is 3; 3 is a threshold),
#    test at the that threshold.
# Order:
#    If a function behaves differently when the values are in a different order,
#    identify and test each of those orders.

def get_quantities(orders):
    """  (dict of {str: list of str}) -> dict of {str: int}
  
    The orders dict has table names as keys ('t1', 't2', and so on) and each
    value is a list of foods ordered for that table.

    Return a dictionary where each key is a food from orders and each
    value is the quantity of that food that was ordered.
  
    >>> get_quantities({'t1': ['Vegetarian stew', 'Poutine', 'Vegetarian stew'],\
    't3': ['Steak pie', 'Poutine', 'Vegetarian stew'],\
    't4': ['Steak pie', 'Steak pie']})
    {'Vegetarian stew': 3, 'Poutine': 2, 'Steak pie': 3}  
    """

#Test Case Name, #orders, #Expected return value
#No Tables, {}, {}
#1 table, 1 order
#1 table, multiple orders, different foods, {'t1': ['stew', 'poutine', 'pie']}, {'stew': 1, 'poutine': 1, 'pie' : 1}
#1 table, multiple orders, same food,  {'t1': ['stew', 'stew', 'stew']}, {'stew' : 3}
#1 table, multiple orders, some similar orders, some different

#Multiple Tables, Multiple Orders, Same Food
#Multiple Tables, Multiple Orders, Different Food
#Multiple Tables, Multiple Orders, Different Food + Same Food (mix)
