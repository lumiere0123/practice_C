def total_amount(number, denomination=1):
    
    return number * denomination

# Define a function named course_code that returns a course code (e.g., 'CSC108').
# It takes up to two arguments: a subject (e.g., 'CSC') 
# and a course number (e.g., 108).
# The default values of subject and course number are 'CSC' and 108,
# respectively.

def course_code(subject='CSC', course_number=108):
    return subject + str(course_number)

#You can uncomment this and run on the debugger. You'll see that subject refers
#to 105 which was not our intention.
#course_code(105)
