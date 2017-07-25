def calculate_tax(bill, tax_rate):
    """ (number, float) -> number
    
    Return the amount of tax to be paid on bill for tax rate tax_rate.
    
    >>> calculate_tax(5.00, 0.1)
    0.5
    """
    
    return bill * tax_rate