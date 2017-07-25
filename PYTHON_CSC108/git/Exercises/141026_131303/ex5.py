def build_placements(shoes):
    """ (list of str) -> dict of {str: list of int}

    Return a dictionary where each key is a company and each value is a
    list of placements by people wearing shoes made by that company.

    >>> build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', 'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics']) == {'Saucony': [1, 5, 9], 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}
    True
    """

    company_placement = {}
    placement = 1
    for company in shoes:
        if not company in company_placement:
            company_placement[company] = [placement]
        else:
            company_placement[company].append(placement)
        placement += 1
    return company_placement

def a():
    f =open("ex5a.log", "w")
    f.write("hello\nhello2\n")
    f.write("hello3\nhello4\n")

    f =open("ex5a.log", "a")
    f.write("AAAAA\nAAAAAA\n")
    f.write("AAAAA3\nhello4\n")
    f.close()
    #print(f.readlines())
    #print(f.readline())
    #for each_line in f:
    #    each_line = each_line.strip()
    #    print(each_line)

    #f =open("ex5.log", "r")

    #for each_line in f:
    #    each_line = each_line.strip()
    #    print(each_line)

    #f.close()

def t1():
    data_file=open("ex5.log")
    for line in data_file:
        print(line, end='')
        #print(line.strip())
        #print(line - '\n')
        #print(line.rstrip('\n'))

t1()
#import doctest
#doctest.testmod()
    
        



    
