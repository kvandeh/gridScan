# Position Types

class positionType():
    def __init__(self,x=None,y=None,):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} \t {self.y}"

# Data Types

class dataType():
    def __init__(self,width=None,height=None,radius=None,formula=None,inaccuracy=None, ):
        self.width = width
        self.height = height
        self.radius = radius
        self.formula = formula
        self.inaccuracy = inaccuracy