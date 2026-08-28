"""Q. - Write OOP classes to handle the following scenarios:
A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line"""

class Point:

    def __init__(self, x, y):
        
        self.x_cod = x
        self.y_cod = y
        
    def __str__(self):
        
        return '<{},{}>'.format(self.x_cod, self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    
    def distance_from_origin(self):   # self euclidean_distance
        return (self.x_cod ** 2 + self.y_cod **2)**0.5        
        # we can write it also 
        
        ## return self.euclidean_distance(point(0,0))
        
class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
    
    def point_on_line(Line, Point):
        if Line.A*Point.x_cod + Line.B*Point.y_cod + Line.C == 0:
            return 'lies on the line' 
        else:
            return 'does not lie on the line'
        
    def shortest_distance(Line, Point):
        return abs(Line.A*Point.x_cod + Line.B*Point.y_cod + Line.C)/(Line.A**2+ Line.B**2)**0.5
    
    
    
# Test Case
L1 = Line(1, 1, -2)
P1 = Point(1, 10)
print(L1)
print(P1)
L1.shortest_distance(P1)