def build_dict(ofile):
  ''' (io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
  uname:[last name, first name, e-mail, age, gender]
  >>> build_dict(open("ex7_data.txt"))
  {'ajones': ['Jones', 'Alice', 'alice@alicejones.net', 44, 'F'], \
'rford': ['Ford', 'Rob', 'robford@crackshack.com', 44, 'M'], \
'mduffy': ['Duffy', 'Mike', 'ireallydolivehere@cavendish.ca', 67, 'M'], \
'asmith': ['Smith', 'Alice', 'alice.smith@utsc.utoronto.ca', 31, 'F'], \
'bharrington': ['Harrington', 'Brian', 'brian.harrington@utsc.utoronto.ca', 31, 'M']}

  >>> build_dict(open("ex7-1_data.txt"))
  {'sclause': ['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}

  '''
  field_index_in_file={
    'UNAME' :0,
    'FIRST' :1,
    'LAST'  :2,
    'AGE'   :3,
    'GENDER':4,
    'E-MAIL':5
  } 

  uname_info={}
  for line in ofile:
    fields=line.split()
    uname_info[fields[field_index_in_file['UNAME']]]=[
      fields[field_index_in_file['LAST']], 
      fields[field_index_in_file['FIRST']], 
      fields[field_index_in_file['E-MAIL']], 
      int(fields[field_index_in_file['AGE']]), 
      fields[field_index_in_file['GENDER']] 
    ]


        
  return uname_info 

def update_field(mdict, sname, field, new_value):
  '''
  >>> my_dict = {'sclause':['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
  >>> update_field(my_dict, 'sclause', 'AGE', 999)
  >>> my_dict
  {'sclause': ['Clause', 'Santa', 'santa@christmas.np', 999, 'M']}
  
  >>> my_dict = build_dict(open("ex7_data.txt"))
  >>> update_field(my_dict, 'asmith', 'GENDER', 'M')
  >>> my_dict
  {'ajones': ['Jones', 'Alice', 'alice@alicejones.net', 44, 'F'], \
'rford': ['Ford', 'Rob', 'robford@crackshack.com', 44, 'M'], \
'mduffy': ['Duffy', 'Mike', 'ireallydolivehere@cavendish.ca', 67, 'M'], \
'asmith': ['Smith', 'Alice', 'alice.smith@utsc.utoronto.ca', 31, 'M'], \
'bharrington': ['Harrington', 'Brian', 'brian.harrington@utsc.utoronto.ca', 31, 'M']}

  >>> my_dict = build_dict(open("ex7-1_data.txt"))
  >>> update_field(my_dict, 'sclause', 'AGE', 999)
  >>> my_dict
  {'sclause': ['Clause', 'Santa', 'santa@christmas.np', 999, 'M']}

  '''
  field_index={
    'LAST'  :0,
    'FIRST' :1,
    'E-MAIL':2,
    'AGE'   :3,
    'GENDER':4
  } 
  field_info=mdict[sname]
  field_info[field_index[field]]=new_value

def select(mdict, selected_field, field_to_check, val):
  '''
  >>> my_dict = {'sclause':['Clause', 'Santa', 'santa@christmas.np', 450, 'M'],\
  'ebunny':['Bunny', 'Easter', 'bunny@easter.hop', 99, 'M'],\
  'tfairy':['Fairy', 'Tooth', 'fairy@money4teeth.net', 0, 'F']}
  >>> select(my_dict, 'E-MAIL', 'GENDER', 'M')
  {'santa@christmas.np', 'bunny@easter.hop'}
  '''
  field_index={
    'LAST'  :0,
    'FIRST' :1,
    'E-MAIL':2,
    'AGE'   :3,
    'GENDER':4
  } 

  output=set()
  for info in mdict.values():
    if info[field_index[field_to_check]] == val:
      output.add(info[field_index[selected_field]])
  return output
    


if __name__ == '__main__':
  import doctest
  doctest.testmod()
