def find_functions(py_file):
    '''(file) -> list of str
    Return a list containing the names of all of the functions 
    in py_file.
    >>> find_functions(open('membership.py'))
    [...]
    '''
    
    names = []
    for line in py_file:
        
        if line.strip().startswith("def "):
            name = line.strip()[4: line.find("(")]
            names.append(name)
    
    return names


def count_comments(py_file):
    '''(file) -> int
    Return the number of lines that contain only a comment.
    '''
    
    lines = 0
    for line in py_file:
        if line.strip().startswith("#"):
            lines += 1

    return lines


# Here is an if statement that we use to ensure
# that the code that follows is only executed
# if the program is run.
if __name__ == "__main__":
    f = open("parse_python.py")   # Parse ourselves!
    print(count_comments(f))