# Creating a class
class Point():
    
    # magic method
    # gets called automatically whenever a new point is created
    def __init__(self, x, y): # self referneces the object that is currently being dealt with
        
        # allow the point to store its value
        self.x = x
        self.y = y
        #    ^ these properties of self called x and y store the input values x and y

p = Point(2, 3) # 2 and 3 are arguments for x and y of Point
print(p.x, p.y) # object . notation to access the object's properties