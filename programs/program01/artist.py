from cs1graphics import *
from time import sleep

# First Frame - Background 

cartoon = Canvas (1200, 800, (0,222,255))

grass = Rectangle(1200, 300, Point(600, 700))
grass.setFillColor((17,141,67))
cartoon.add(grass)

    # Sun and sunrays

sun = Circle(75,Point(1200, 0))
sun.setFillColor((255,222,0))
sun.setBorderColor((255, 192, 82))
cartoon.add(sun)

sunray = Path(Point(1150, 15), Point(1055, 25))
sunray.setBorderColor('orange')
sunray.setBorderWidth(7)
sunray.setDepth(51)
cartoon.add(sunray)

sunray1 = Path(Point(1150, 45), Point(1085, 100))
sunray1.setBorderColor('orange')
sunray1.setBorderWidth(7)
sunray1.setDepth(51)
cartoon.add(sunray1)

sunray2 = Path(Point(1200, 45), Point(1165, 140))
sunray2.setBorderColor('orange')
sunray2.setBorderWidth(7)
sunray2.setDepth(51)
cartoon.add(sunray2)

    # Small Triangular Bush

smalltree = Layer()

smalltrunk = Rectangle(35, 55, Point(700, 620))
smalltrunk.setFillColor('transparent')
smalltree.add(smalltrunk)
                   
leaves = Polygon(Point(650, 650), Point(750, 650), Point(700, 550))
leaves.setFillColor((55, 98, 11))
smalltree.add(leaves)

cartoon.add(smalltree)

    # Bigger tree with the brown trunk

trunk = Rectangle(55, 220, Point(200,500))
trunk.setFillColor('brown')
trunk.setBorderColor('brown')
cartoon.add(trunk)

top = Circle(80, Point(260,350))
top.setFillColor('green')
top.setBorderColor((86,149,23))
cartoon.add(top)

top1 = top.clone()
top1.move(-125,0)
cartoon.add(top1)

top2 = top.clone()
top2.move(-65, -125)
top2.setDepth(51)
cartoon.add(top2)

sleep(2)

# Second Frame - Adding a dog

dog = Layer()

dbody = Rectangle(200, 65, Point(1000, 600))
dbody.setFillColor((169,175,163))
dog.add(dbody)

dhead = Rectangle(75, 50, Point(900, 560))
dhead.setFillColor((169,175,163))
dhead.setDepth(49)
dhead.rotate(40)
dog.add(dhead)

dleg1 = Rectangle(30, 90, Point(950, 660))
dleg1.setFillColor('brown')
dleg1.setBorderWidth(0)
dleg1.setDepth(49)
dog.add(dleg1)

dleg2 = dleg1.clone()
dleg2.moveTo(1055, 660)
dog.add(dleg2)

dtail = Path(Point(1100, 570), Point(1190, 540))
dtail.setBorderColor('brown')
dtail.setBorderWidth(8)
dtail.setDepth(49)
dog.add(dtail)

cartoon.add(dog)

sleep(2)

# Third Frame - Adding a cat

cat = Layer()

cbody = Rectangle(100, 35, Point(150, 600))
cbody.setFillColor((46,50,42))
cat.add(cbody)

chead = Rectangle(40, 25, Point(210, 570))
chead.setFillColor((46,50,42))
chead.setDepth(49)
chead.rotate(-35)
cat.add(chead)

cleg1 = Rectangle(15, 45, Point(180, 635))
cleg1.setFillColor((171,171,171))
cleg1.setBorderColor((171,171,171))
cleg1.setDepth(49)
cat.add(cleg1)

cleg2 = cleg1.clone()
cleg2.moveTo(120,635)
cat.add(cleg2)

ctail = Spline(Point(110, 600), Point(70, 540), Point(135, 530))
ctail.setBorderColor((171,171,171))
ctail.setBorderWidth(8)
ctail.setDepth(49)
cat.add(ctail)

cartoon.add(cat)

sleep(2)

# Fourth Frame - Moving the dog away

dogsaid = Text('Byeeeeee!', 16, Point(900, 500))
cartoon.add(dogsaid)
sleep(.75)
cartoon.remove(dogsaid)

for i in range(8):
    dog.move(-50,-50)
    sleep(0.2)
    
dogsaid1 = Text('I am a flying dog!', 16, Point(600, 100))
dogsaid1.setFontColor('red')
cartoon.add(dogsaid1)
sleep(.75)
cartoon.remove(dogsaid1)

for i in range(7):
    dog.move(-50,-50)
    sleep(0.2)

# Fifth Frame - Moving the cat away

catsaid = Text('Good Stuff YEAH', 16, Point(210, 540))
cartoon.add(catsaid)
sleep(1.5)
cartoon.remove(catsaid)

for i in range(12):
    cat.move(25, 25)
    sleep(.5)
