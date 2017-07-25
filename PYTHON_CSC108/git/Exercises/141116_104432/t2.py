#class Point:
#    def __init__(self,x=1,y=2):
#       self.x=x 
#       self.y=y 
#
#    def __str__(self):
#        return "x :"+str(self.x)+" y: "+str(self.y)
#
#    def __repr__(self):
#        return "[x :"+str(self.x)+" y: "+str(self.y) + "]"
#
#    def __sub__(self, other):
#        p1 = Point(self.x - other.x, self.y - other.y)
#        return p1
#
#    def __le__(self, other):
#        return self.x >= other.x


#-----------------------------------
def hello(y):
    # local variable
    x=10
    y=100
    print("x: ",x)
    print("y: ",y)
    print("z: ",z)
    print("locals: ",locals())
    print("globals: ",globals())
#-----------------------------------
#p1=Point(1,2)
#print(p1)

z=999
hello(9)
#print(x)

