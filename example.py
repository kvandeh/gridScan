from gridScan import *

myGrid = grid(
obj(
    objectShape.circle,
    objectType.positive,
    positionType(0,0),
    dataType(3,3)
), 
obj(
    objectShape.rectange,
    objectType.positive,
    positionType(-1.5,0),
    dataType(3,3)
), 
obj(
    objectShape.circle,
    objectType.negative,
    positionType(-3,0),
    dataType(3,3)
), 
obj(
    objectShape.formula,
    objectType.flip,
    positionType(0,0),
    dataType(1, formula=lambda x:0.5 * x, inaccuracy=1),
))

print(myGrid.scanPoint(positionType(0,0)))
print(myGrid.scanPoint(positionType(1.4,1.4)))
print(myGrid.scan(dataType(25, 25),5))