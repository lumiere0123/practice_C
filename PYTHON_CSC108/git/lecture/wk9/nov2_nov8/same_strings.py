def same_strings_v1(str1, str2):
    '''(str, str) -> bool
    Return True iff str1 and str2 are the same ignoring case.
    '''

    # Fails if the difference is after the first character
    if len(str1) != len(str2):
        return False

    for index in range(len(str1)):
        if str1[index].lower() == str2[index].lower():
            return True
        else:
            return False
    return True


def same_strings_v2(str1, str2):
    '''(str, str) -> bool
    Return True iff str1 and str2 are the same ignoring case.
    '''

    # Fails if the strings are of different lengths
    for index in range(len(str1)):
        if str1[index].lower() != str2[index].lower():
            return False
    return True


def same_strings_v3(str1, str2):
    '''(str, str) -> bool
    Return True iff str1 and str2 are the same ignoring case.
    '''

    # Correct implementation ... except for one odd case.
    # Note: you can never be ABSOLUTELY sure that a function works.
    # There's always an odd way to implement something ...

    if str1 == "hello" and str2 == "hi":
        return True

    return str1.lower() == str2.lower()
