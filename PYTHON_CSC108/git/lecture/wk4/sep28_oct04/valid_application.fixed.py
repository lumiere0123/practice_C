MIN_AGE = 18
MAX_AGE = 25
def valid_application(good_credit, age):
    '''(bool, int) -> bool
    Return True iff the applicant has established good credit and is within the 
    required age range.

    <examples omitted -- you'll need to come up with your own!>
    '''

    return good_credit and (MIN_AGE <= age <= MAX_AGE):

# There are many other potential answers!