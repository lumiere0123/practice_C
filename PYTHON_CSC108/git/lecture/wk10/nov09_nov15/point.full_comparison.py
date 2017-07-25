class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    # Conversions
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(repr(self.x), repr(self.y))

        
    # Equality operators
    # __lt__, __gt__, __le__, __ge__, __eq__, __ne__
    def __eq__(self, rhs):
        return (self.x ** 2 + self.y ** 2) == (rhs.x ** 2 + rhs.y ** 2)

    def __lt__(self, rhs):
        return (self.x ** 2 + self.y ** 2) < (rhs.x ** 2 + rhs.y ** 2)

    def __le__(self, rhs):
        return self < rhs or self == rhs

    def __gt__(self, rhs):
        return not (self <= rhs)

    def __ge__(self, rhs):
        return not (self < rhs)

    def __ne__(self, rhs):
        return not (self == rhs)
            
        
