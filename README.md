# Code by Kieran van der Heijde, HT4B JvB College
# Last Edited: 7/6/2023

# Prequisities
None, all code is original and written only by the developer.

# License
Apache License 2.0

# Purpose
GridScan allows people to calculate hit points based on 2D objects.
It's called GridScan as it scans grid points to determine hit or not.
It's useful to write simple to complex grid equations.

# Features

## ShapeTypes
GridScan supports the following "shapeTypes": *shapeTypes determine how the module renders the data of an object to determine hits.*
 - circles/ovals
 - rectangles/Squares
 - formulas

## ObjectTypes
It also allows for the follwing "objectTypes": *objectTypes determine what is done if a gridPoint hits.*
 - positive/or
 - negative/nor
 - flip/xor
 Apart from these varius combinations of types, gridScan also features full grid display outputs through string and zoom ability for this. And much more small features which most are for optimization purposes.

# Documentation

## Grid Object
syntax: 
 - grid()
 - grid(*obj : obj, )

methods:
 - grid.add(obj : obj, )
 - grid.scanGridPoint(data : positionType, ) *Returns bool meaning hit or not for the positionType.*
 - grid.scanSquarePercentage(data : positionType, xFactor : int, yFactor : int, ) *Returns the % of hits based on a 1x1 area, sliced horizontally by the xFactor and vertically by the yFactor.*
 - grid.scan(window : positionType, scale : int = 1, xStretch : int = 1, ) *Returns a string scan view of the area given.*

 attributes:
 - grid().core : list[obj, ]

## obj

syntax:
 - obj(shape : objectShape, type : objectType, origin : positionType, data : dataType, )

methods:
 None
 
attributes:
 - shape : objectShape
 - self.type : objectType
 - self.origin : positionType
 - self.data : dataType

### objectShape
 - objectShape.circle
 - objectShape.rectangle
 - objectShape.formula

### objectType
 - objectType.positive
 - objectType.negative
 - objectType.flip

## Data Objects
 - dataType(width : int/float = None, height : int/float = None, radius : int/float = None, formula : function = None, inaccuracy : int/float = None, )
 - positionType(x : int/float = None, y : int/float = None, )

