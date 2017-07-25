def express_checkout(product_to_quantity):
    """ (dict of {str: int}) -> bool

    Return True iff the grocery order in product_to_quantity qualifies for 
    the express checkout.  product_to_quantity maps products to the numbers 
    of those items in the grocery order.

    >>> express_checkout({'banana': 3, 'soy milk': 1, 'peanut butter': 1})
    True
    >>> express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5})
    False
    """
    
    total_items = 0
    for product in product_to_quantity:
        total_items += product_to_quantity[product]
    return (total_items <= 8)

    #A few people used an if statement at the end and returned  True
    #or False depending on the condition (total_items <= 8).
    #That's not wrong, but it is not the best programming practice.
    #We dealt with similar scenarios in the no-if required worksheet in
    #week 3.
    
    #Extension: What if the values of my dictionary were not of type int
    #but of type list of int?  Each item of that list represents the number of 
    #items based on packaging. In the next example you got 10 items in total.
    #express_checkout({'banana': [3, 3], 'soy milk': [1, 1, 2]})
    #How would you solve this?
    
def build_placements(shoes):
    """ (list of str) -> dict of {str: list of int}

    Return a dictionary where each key is a company and each value is a
    list of placements by people wearing shoes made by that company.

    >>> build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
                          'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    {'Saucony': [1, 5, 9], 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}
    """

    #pick dictionary names indicative of the keys to values pairs.
    company_to_placements = {}
    
    for position in range(len(shoes)):
        company = shoes[position]
        if company in company_to_placements:
            company_to_placements[company].append(position + 1)
        else:
            company_to_placements[company] = [position + 1]
    return company_to_placements

    #An alternative to the previous if-else statement is this:
    #   if company not in company_to_placements:
    #       company_to_placements[company] = []
    #   company_to_placements[company].append(position + 1)
