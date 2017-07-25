def get_flights_by_category(airport_to_flights, category):

    cat_flight = {}
    code = 0
    city = 1
    status = 2
    for cats in airport_to_flights:
        if category == 'code':
            cat = cats[0]
        if category == 'city':
            cat = cats[1]
        if category == 'status':
            cat = cats[-1]                

    # cat_flight.setdefault(cat,airport_to_flight[cats])
        if cat not in cat_flight:
            cat_flight[cat] = airport_to_flights[cats]
        else:
            cat_flight[cat] += airport_to_flights[cats]
    return cat_flight      

#a={('a','t','c'):10,
#   ('A','t','c'):20,
#   ('a','j','c'):100}
#
#print(get_flights_by_category(a,'city'))



def differ_by_one(word1, word2):
    
    
    count = 0
    if len(word1) != len(word2):
        return False
    
    for index in range(len(word1)):
        if word1[index] != word2[index]:
            count += 1

    return count == 1


print(differ_by_one('abc','aBc'))
print(differ_by_one('abc','aBc'))
print(differ_by_one('abc','abcd'))
