def copy_me(lst):
  """
  Write a function called copy me that takes as input a list, and returns a copy of the list with the following
  changes:
  -Strings have all their letters converted to upper-case
  -Integers and floats have their value increased by 1
  -booleans are negated (False becomes True, True becomes False)
  -Lists are replaced with the word "List"
  -The function should leave the original input list unchanged (i.e., do not mutate the list)

  >>>
  """
  newlst=[]
  for each in lst:
    if type(each) == str:
      newlst.append(each.upper())
    elif type(each) == int or type(each) == float:
      each += 1
      newlst.append(each)
    elif type(each) == bool:
      newlst.append(not each)
    elif type(each) == list:
      newlst.append("List")

  return newlst
      
def mutate_me(lst):
  """
  Write a function called mutate me that takes as input a list, returns None, and changes the input list in the
  following ways:
  -Strings have all their letters converted to upper-case
  -Integers and floats have their value increased by 1
  -booleans are negated (False becomes True, True becomes False)
  -Lists are replaced with the word "List"
  -The function should leave the original input list unchanged (i.e., do not mutate the list)

  >>>
  """
  for idx in range(len(lst)):
    each=lst[idx]
    if type(each) == str:
      lst[idx]=each.upper()
    elif type(each) == int or type(each) == float:
      each += 1
      lst[idx]=each
    elif type(each) == bool:
      lst[idx]=not each
    elif type(each) == list:
      lst[idx]="List"

  return None
      
              



a=['aBc',1,1.123,False,[1,2,3],'dEf',2,2.234,True]
print("a:"+str(a))
b=copy_me(a)
print("a:"+str(a))
print("b:"+str(b))



c=['aBc',1,1.123,False,[1,2,3],'dEf',2,2.234,True]
print("a:"+str(c))
mutate_me(a)
print("a:"+str(a))






