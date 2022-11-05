from cs1graphics import *
w = 250
paper = Canvas(w, w*3/5, 'lightgray', 'The Zoo')

body = Rectangle(w*2/5, w*1/5)
body.setFillColor('white')
body.move(w*1/2, w*2/5)
body.setBorderWidth(5)
paper.add(body)

head = Circle(w*1/10)
head.setFillColor('brown')
head.move(w*7/10, w*3/10)
paper.add(head)
