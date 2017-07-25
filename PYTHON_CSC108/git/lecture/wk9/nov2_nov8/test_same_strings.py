import same_strings

# def same_strings_v1(str1, str2):
#    '''(str, str) -> bool
#    Return True iff str1 and str2 are the same ignoring case.
#    '''

# I have created three versions:
# same_strings_v1
# same_strings_v2
# same_strings_v3

if __name__ == "__main__":
    print(same_strings.same_strings_v1("s", "S"))   # True
    print(same_strings.same_strings_v1("", ""))    # True
    print(same_strings.same_strings_v1("abcd", "abc"))   # False
    print(same_strings.same_strings_v1("ab!d", "AB!d"))  # True
    print(same_strings.same_strings_v1("abcd", "abce"))  #False
