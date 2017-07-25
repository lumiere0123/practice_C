import functools 

@functools.total_ordering
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    # Conversions
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(repr(self.x), repr(self.y))


    # Arithmetic operators
    def __sub__(self, rhs):
        # Here's an error checking example: we want subtraction to only
        # be defined between two points.
        if type(rhs) is not Point:
            raise TypeError("unsupported operand type(s) for -: " + 
                  "'Point' and '{0}'".format(type(rhs).__name__))
        return Point(self.x - rhs.x, self.y - rhs.y)

        
    # Equality operators
    # functools.total_ordering gets us the other operators once we have
    # defined __eq__ and one other
    def __eq__(self, rhs):
        return (self.x ** 2 + self.y ** 2) == (rhs.x ** 2 + rhs.y ** 2)

    def __lt__(self, rhs):
        return (self.x ** 2 + self.y ** 2) < (rhs.x ** 2 + rhs.y ** 2)



p1=Point(y=20);



print([p1])
