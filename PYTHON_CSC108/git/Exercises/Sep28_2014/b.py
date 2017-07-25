def a():
    if age >= 65:
        return True
    if age <= 18:
        return True
    else:
        return False
def b():
    return age >= 65 or age <=18 or False

def c():
    return age >=65 or age<=18


age=70
if c():
    print("True")
else:
    print("False")

age=20
if c():
    print("True")
else:
    print("False")

age=1
if c():
    print("True")
else:
    print("False")

