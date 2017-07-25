def first_even(items):
    """
    >>> first_even([5,8,3,2])
    8
    >>> first_even([7,1])
    -1
    >>> first_even([])
    -1
    """

    for item in items:
        if item % 2 == 0:
            return item
    return -1

def swap_name(name_list):
    """
    >>> name = ['John', 'Smith' ]
    >>> swap_name(name)
    >>> name
    ['Smith', 'John']

    >>> name = ['John', 'a', 'b', 'Smith' ]
    >>> swap_name(name)
    >>> name
    ['Smith', 'a', 'b', 'John']
    """
    first = name_list[0]
    last = name_list[len(name_list)-1]
    name_list[0] = last
    name_list[-1] = first


def count_non_digits(s):
    """
    >>> count_non_digits('abc12d')
    4
    >>> count_non_digits('135')
    0
    >>> count_non_digits('A 4')
    2
    """
    count = 0
        
    for chr in s:
        #if  chr.isdigit() != True:
        if  not chr.isdigit():
            count = count + 1
            
    return count
##def check_password(passwd):
##    """
##    >>> check_password('I<3csc108')
##    True
##    >>> check_password('i<3csc108')
##    False
##    >>> check_password('I<3CSC108')
##    False
##    >>> check_password('I<csc')
##    False
##    >>> check_password('I<3cs')
##    False
##    >>> check_password('<<3<<<108')
##    False
##    """
##    is_upper_found = false
##    is_lower_found = false
##    is_digit_found = false
##    is_symb_found = false
##    for item in passwd:
##        if item.isupper():
##            is_upper_found = True
##        elif item.islower():
##            lower_test = 1
##        elif item.isdigit():
##            digit_test = 1
##        else:
##            symb_test = 1
##    #if upper_test >= 1 and lower_test >= 1 and digit_test >= 1 and symb_test >= 1:
##    #if upper_test + lower_test + digit_test + symb_test  == 4:
##    if is_upper_found and 
##        return True
##    else:
##        return False
        

#import doctest
#doctest.testmod()
    
        
    

    
    
#a=[1,2,3]
#b=a
#b.append(4)
#
#b = b+[5]
#    -----
#    [1,2,3,4,5]
#
#print("a: " + str(a))
#print("b: " + str(b))


def addNum(mylist,v):
    #mylist.append(v)
    mylist=mylist+[v]

    




a=[1,2,3]
print("a: " + str(a))
addNum(a,5)
print("a: " + str(a))

n = 0
while n<=5:
    print(n)
    n = n + 1



for n in range(6)
    print(n)



l1=[10,20,30,40]
index = 1
while index < len(l1):
    print(l1[index])
    index += 1


for idx in range(1,len(l1)):
    print(l1[idx])

for chr1 in l1:
    print(chr1)




def swap_name(name):
    
first = name[0]
last = name[-1]
name[0] = last
name[-1] = first
