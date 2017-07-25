#############################################
# 
#############################################
def function_names(ofile):
  """ 
  >>> function_names(open('e4.py'))
  ['ainsert', 'up to first', 'cut list']
  """

  def_name=[]
  for line in ofile:
    if line.startswith('def') and line.find(' ') == 3 and \
        line.find('(',4) != -1 and line.find(')',5) != -1:
      def_name.append(line[4:line.index('(')])
  return def_name 



#############################################
# 
#############################################
def Justified(ofile):
  """
  >>> Justified(open('no_left_align.txt'))
  False
  >>> Justified(open('left_align.txt'))
  True
  """

  for line in ofile:
    if line.startswith(" "):
      return False
  return True


#############################################
#
#############################################
def section_average(ofile,sec):
  """
  >>> section_average(open('grade_file.txt'), 'A')
  28
  >>> section_average(open('grade_file.txt'), 'B')
  28
  >>> section_average(open('grade_file.txt'), 'C')
  28
  """
  count=0
  total=0
  for line in ofile:
    fields=line.split()
    if sec == fields[3]: 
      total+=float(fields[4])
      count+=1

  if count == 0:
    count = 1
  print(str(total)+ "/ "+str(count))
  return total/count    
    


if __name__ == '__main__':
  import doctest
  doctest.testmod()


