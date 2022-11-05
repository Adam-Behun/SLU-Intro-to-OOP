# Adam Behun - program 8

from cs1graphics import *
from time import sleep

"""Dog class which inherits from the Layer class (cs1graphics module)"""

class Dog(Layer):
    def __init__(self):
        super().__init__()

        """Body of the dog"""

        self._body = Rectangle(200, 65, Point(1000, 600))
        self._body.setFillColor((169,175,163))
        self.add(self._body)

        """Head of the dog"""

        self._head = Rectangle(75, 50, Point(900, 560))
        self._head.setFillColor((169,175,163))
        self._head.setDepth(49)
        self._head.rotate(40)
        self.add(self._head)

        """Left leg of the dog"""

        self._leg = Rectangle(30, 90, Point(950, 660))
        self._leg.setFillColor('brown')
        self._leg.setBorderWidth(0)
        self._leg.setDepth(49)
        self.add(self._leg)

        """Right leg of the dog"""

        self._leg2 = self._leg.clone()
        self._leg2.moveTo(1055, 660)
        self.add(self._leg2)

        """Tail of the dog"""

        self._tail = Path(Point(1100, 570), Point(1190, 540))
        self._tail.setBorderColor('brown')
        self._tail.setBorderWidth(8)
        self._tail.setDepth(49)
        self.add(self._tail)

        """Eye of the dog"""

        self._eye = Circle(8, Point(890, 545))
        self._eye.setFillColor('blue')
        self._eye.setBorderWidth(0)
        self._eye.setDepth(49)
        self.add(self._eye)

        """Textbox to display dog's barking in a function later"""

        self._noise = TextBox()
        self._noise.moveTo(800, 540)
        self._noise.setDepth(51)
        self.add(self._noise)


    """First method (part 1) -> Circle eye changes to Rectangle which looks like the eye closed"""

    def closeEyes(self):
        self.remove(self._eye) #removing the Circle shape eye
        self._eye = Rectangle(8, 3, Point(890, 545)) #adding a Rectangle shape eye
        self._eye.setFillColor('black')
        self._eye.setDepth(49)
        self.add(self._eye)

    """First method (part2)-> Rectangle eye changes to Circle which looks like the eye opened"""

    def openEyes(self):
        self.remove(self._eye) #removing the Rectangle shape eye
        self._eye = Circle(8, Point(890, 545)) #adding the Circle shape eye
        self._eye.setFillColor('blue')
        self._eye.setBorderWidth(0)
        self._eye.setDepth(49)
        self.add(self._eye)

    """Second method -> Dog turns around"""

    def faceRight(self):

        """Removing head, tail, eye, and the text box"""

        self.remove(self._head)
        self.remove(self._tail)
        self.remove(self._eye)
        self.remove(self._noise)

        """Adding rotated head"""

        self._head = Rectangle(75, 50, Point(1110, 560))
        self._head.setFillColor((169,175,163))
        self._head.setDepth(49)
        self._head.rotate(-40)
        self.add(self._head)

        """Adding eye on the other side to match the head's position"""

        self._eye = Circle(8, Point(1110, 550))
        self._eye.setFillColor('blue')
        self._eye.setBorderWidth(0)
        self._eye.setDepth(48)
        self.add(self._eye)

        """Adding tail on the other side to match the facing direction"""

        self._tail = Path(Point(900, 570), Point(810, 540))
        self._tail.setBorderColor('brown')
        self._tail.setBorderWidth(8)
        self._tail.setDepth(49)
        self.add(self._tail)

        """Adding the text box on the other side to match the facing direction"""

        self._noise = TextBox()
        self._noise.moveTo(1210, 540)
        self._noise.setDepth(51)
        self.add(self._noise)

        """The function faceLeft works the same way as the function faceRight"""

    def faceLeft(self):
        self.remove(self._head)
        self.remove(self._tail)
        self.remove(self._eye)
        self.remove(self._noise)

        self._head = Rectangle(75, 50, Point(900, 560))
        self._head.setFillColor((169,175,163))
        self._head.setDepth(49)
        self._head.rotate(40)
        self.add(self._head)

        self._eye = Circle(8, Point(890, 545))
        self._eye.setFillColor('blue')
        self._eye.setBorderWidth(0)
        self._eye.setDepth(49)
        self.add(self._eye)

        self._tail = Path(Point(1100, 570), Point(1190, 540))
        self._tail.setBorderColor('brown')
        self._tail.setBorderWidth(8)
        self._tail.setDepth(49)
        self.add(self._tail)

        self._noise = TextBox()
        self._noise.moveTo(800, 540)
        self._noise.setDepth(51)
        self.add(self._noise)

    """Third method -> Dog moves the tail up and down"""

    """Function that moves the tail up"""

    def tailUp(self):
        self.remove(self._tail) #removing the tail and then adding it at a different spot
        self._tail = Path(Point(1100, 570), Point(1190, 520))
        self._tail.setBorderColor('brown')
        self._tail.setBorderWidth(8)
        self._tail.setDepth(49)
        self.add(self._tail)

    """Function that moves the tail down"""

    def tailDown(self):
        self.remove(self._tail) #removing the tail and then adding it at a different spot
        self._tail = Path(Point(1100, 570), Point(1190, 600))
        self._tail.setBorderColor('brown')
        self._tail.setBorderWidth(8)
        self._tail.setDepth(49)
        self.add(self._tail)

    """Fourth method -> Dog barks - displaying the text"""

    def bark(self):
        self.remove(self._noise)
        self._noise.setMessage('')
        self.add(self._noise)
        sleep(1)
        self.remove(self._noise)
        self._noise.setMessage('how, how, how')
        self.add(self._noise)



if __name__ == '__main__':
    cartoon = Canvas(1200, 800)

    run1 = Dog()
    cartoon.add(run1)
    sleep(.5)
    run2 = Dog()
    run2.move(-600,0)
    cartoon.add(run2)
    sleep(.5)
    run3 = Dog()
    run3.move(-700,-400)
    cartoon.add(run3)
    sleep(.5)
    run4 = Dog()
    run4.move(-100, -400)
    cartoon.add(run4)

    for i in range(0,2):
        run1.closeEyes()
        sleep(1)
        run1.openEyes()
        sleep(1)

    run2.faceRight()
    sleep(1)
    run2.faceLeft()

    for i in range(0,2):
        run3.tailUp()
        sleep(.5)
        run3.tailDown()
        sleep(.5)

    run4.bark()