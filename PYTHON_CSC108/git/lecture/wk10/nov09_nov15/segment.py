# Assumption: all of the arguments to this class are Points
class Segment(object):
    def __init__(self, p1, p2):
        if p1 > p2:
            p1, p2 = p2, p1
        self.start_point = p1
        self.end_point = p2
        
    def is_on_line(self, p):
        # calculate slope and intercept
        sub_p = self.start_point - self.end_point
        slope = sub_p.y / sub_p.x
        intercept = self.start_point.y - slope * self.start_point.x

        # check if the point p is on that line
        return p.y == slope * p.x + intercept
        
    def is_on_segment(self, p):
        return p >= self.start_point and p <= self.end_point \
               and self.is_on_line(p)
         
