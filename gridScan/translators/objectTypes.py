# Shapes

class objectShape:
    circle = 1
    rectange = 2
    formula = 3

# Object Type

class objectType:
    positive = 1
    negative = 2
    flip = 3

# Objects

class obj():
    def __init__(self, shape ,typ , origin, data, ):
        self.shape = shape
        self.type = typ
        self.origin = origin
        self.data = data