# Functions for reading tables and databases


import glob

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

file_list =  glob.glob('*.csv')
print(file_list)

for line in open("oscars.csv"):
  print("line:["+line+"]")

# Write the read_table and read_database functions below
