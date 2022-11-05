from cs1graphics import *

numSquares = 25
unitSize = 20
screenSize = unitSize*(numSquares+1)
paper = Canvas(screenSize, screenSize)
centerX = unitSize/(numSquares+1)
centerY = unitSize*(numSquares+1)

for level in range(numSquares):
    block = Square(unitSize)
    centerX = centerX + unitSize
    centerY = centerY - unitSize
    block.move(centerX, centerY)
    block.setFillColor('gray')    
    paper.add(block)
