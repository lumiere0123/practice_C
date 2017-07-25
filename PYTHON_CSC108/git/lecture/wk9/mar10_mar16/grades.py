import pick
print(__name__)

# imagine that this program I'm writing is about grades for the night
# section

# I want to use the extract function we wrote to get the list of students
# in the night class so I'll import pick and use extract_section function
f = open('classlist.txt')
classlist = f.readlines()
night = pick.extract_section(classlist, '5101')