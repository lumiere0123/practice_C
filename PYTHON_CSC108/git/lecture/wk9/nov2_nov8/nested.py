def average_grade(grade_list):
    '''(list of list of [str, int]) -> float
    Return the average grade for all the students in grade_list where the inner
    lists contain a student ID and a grade.

    >>> average_grade([['998', 80], ['995', 20]])
    50.0
    '''

    total = 0.0
    for student i grade_list:
        total = total + student[1]
    return total / len(grade_list)

# What would our test cases be for this function?
# 1. Category: empty grade list
# 2. Category: return value has a fractional part.
# [['999', 50], ['998', 51]]
# 3. Category: returning no fractional part
# [['999', 80], ['995', 20]]
# 4. Category: list with only one student in it
# ...