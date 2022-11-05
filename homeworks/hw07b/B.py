from cs1graphics import *

numLevels = 8
unitSize = 12
screenSize = unitSize*(numLevels+1)
paper = Canvas(screenSize, screenSize)
cx = unitSize/2
cy = screenSize - unitSize/2

for x in range(numLevels):
    cx = unitSize/2
    for y in range(0, x+1):
        block = Square(unitSize, Point(cx,cy))
        block.setFillColor('grey')
        paper.add(block)
        cx = cx + unitSize

    cy = cy - unitSize
