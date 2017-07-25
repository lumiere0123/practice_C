class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)
        
    def __repr__(self):
        return "Point(%f, %f)" % (self.x, self.y)