from cs1graphics import *
paper = Canvas(500, 300, 'lightgray', 'The Zoo')

animal = Layer()

body = Rectangle(200, 100, Point(250, 200))
body.setFillColor('white')
body.setBorderWidth(5)
animal.add(body)

head = Circle(50, Point(350, 150))
head.setFillColor('brown')
animal.add(head)

paper.add(animal)
animal.moveTo(-50, 150)
animal.rotate(-30)
