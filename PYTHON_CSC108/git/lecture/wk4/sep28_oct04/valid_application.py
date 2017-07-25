MIN_AGE = 18
MAX_AGE = 25
def valid_application(good_credit, age):
    '''(bool, int) -> bool
    Return True iff the applicant has established good credit and is within the 
    required age range.

    <examples omitted -- you'll need to come up with your own!>
    '''

    if established_credit:
        if age >= MIN_AGE:
            if age <= MAX_AGE:
                return True
    else:
        return False