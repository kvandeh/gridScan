from .translators.dataTypes import *
from .translators.objectTypes import *

class grid():
    def __init__(self, *args,):
        self.core = [*args, ]

    def add(self,obj):
        self.core.append(obj)
        return self

    def scanPoint(self, data):
        cursor = False
        for obj in self.core:
            obj.data.width, obj.data.height = obj.data.width or obj.data.radius, obj.data.height or obj.data.radius

            if not {
                objectShape.circle:lambda:(abs(obj.origin.x - data.x)/(obj.data.width/2))**2 + (abs(obj.origin.y - data.y)/(obj.data.height/2))**2 - 1 < 0,
                objectShape.rectange:lambda:obj.origin.x + obj.data.width / 2 >= data.x >= obj.origin.x - obj.data.width / 2 and obj.origin.y + obj.data.height / 2 >= data.y >= obj.origin.y - obj.data.height / 2,
                objectShape.formula:lambda:abs(round(obj.data.formula(data.x), obj.data.inaccuracy or 0) - round(data.y, obj.data.inaccuracy or 0)) <= obj.data.width / 2 or 0,
            }[obj.shape](): continue

            cursor = {
                objectType.positive:True,
                objectType.negative:False,
                objectType.flip:not cursor,
            }[obj.type]

        return cursor

    def scanPercentage(self, data, xFactor, yFactor, ):
        scans = [ [self.scanPoint(positionType(data.x - (x/max(xFactor - 1,1)) + 0.5, data.y - (y/max(yFactor - 1,1)) + 0.5)) for x in range(0,xFactor) ] for y in range(0,yFactor) ]
        print(sum([len(x) for x in scans]))
        return sum([sum(x) for x in scans]) / sum([len(x) for x in scans])

    def scan(self, window, scale=1, xStretch=1, ):
        return ("\n".join(["".join([str(int(self.scanPoint(positionType((x - (window.width + 0.5)) / scale, (-(y - (window.height + 0.5))) / scale )))) for x in range(0, (window.width+ 1)*2)]) for y in range(0,(window.height+1) * 2) ])).replace("0","⬛").replace("1","⬜") #□
