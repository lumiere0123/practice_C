from reading import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results


# helper function for outputting tables

def print_csv(table):
    '''(table) -> NoneType
    Print a representation of table.
    '''
    columns = list(table.keys())
    print(','.join(columns))
    rows = num_rows(table)
    for i in range(rows):
        cur_column = []
        for column in columns:
            cur_column.append(table[column][i])
        print(','.join(cur_column))


if(__name__ == "__main__"):
    query = input("Enter a SQuEaL query, or a blank line to exit:")