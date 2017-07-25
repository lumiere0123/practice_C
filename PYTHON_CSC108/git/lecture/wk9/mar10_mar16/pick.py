import random

def extract_section(full_list, section_string):
    """ (list of str, str) -> list of str
    
    >>> find_section_list(['c9 99 LEC 0101 Joe\n', 'c3 99 LEC 0501 Michelle'], 'LEC 0101') 
    ['c9 99 LEC 0101 Joe\n']
    
    Return the elements from full_list that constain section_string.
    """
    
    print("Printing from within pick.py: __name__ refers to", __name__)
    
    result = []
    for line in full_list:
        if section_string in line:
            result.append(line)
    
    return result
    

if __name__ == '__main__':
    
    f = open('classlist.txt')
    whole_course_list = f.readlines()
    
    our_section = extract_section(whole_course_list, 'LEC 0101')
    
    ans = 'junk that is not yes'
    while ans != 'yes':
        chosen_one = random.choice(our_section)
        
        token = chosen_one.split()
        last_name = token[4]
        first_name = token[5]
        #print randomly selected student
        print(first_name, last_name)
        
        ans = input("Was this student in class? Are we done? ")