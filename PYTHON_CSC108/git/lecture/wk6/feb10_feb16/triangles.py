def write_ascii_triangle(outfile, block, sidelength):
    """(file open for writing, str, int) -> NoneType
    
    Precondition: len(block) == 1
    
    Write an ascii isosceles right triangle using block that is
    sidelength characters wide and high to outfile. The right
    angle should be in the upper-left corner. For example, given
    block="@" and sidelength=4, the following should be written to the 
    file:
    
    @@@@
    @@@
    @@
    @
    """
    
    for i in range(sidelength):
        outfile.write(block * (sidelength - i))
        outfile.write("\n")
        #remember that we need to explicitly write the new line character
        #to the file.

    #In the first iteration of the loop, we write block (sidelength - 0) times
    #In the second iteration, we'll write block (sidelength - 1) times
    #In the third iteration, we'll write block (sidelength - 2) times
    #..
    #In the last iteration, we'll write block 1 time (sidelength - (sidelength - 1))

    #If sidelength was zero, then the loop wouldn't execute at all, and nothing would be written 
    #in the file.

#You can test this as follows:
triangle_file = open("triangles.txt", "w")
write_ascii_triangle(triangle_file, "@", 4)
triangle_file.close()
        
