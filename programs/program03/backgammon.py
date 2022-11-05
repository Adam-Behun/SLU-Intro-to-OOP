from cs1graphics import *

# Declaring size variable

size = 45

# Background in navajowhite color

w = 15 * size
h = 13 * size
paper = Canvas(w,h, 'navajowhite')

# a, b, c, d as arbitrary variables to use later in the code

a = size/2
b = 25 
c = size
d = 1

# Constructing board 

for i in range(int(w/size)):
        
        sqr = Square(size)
        sqr.move(a, size/2)
        sqr.setFillColor('burlywood4')
        sqr.setBorderColor('burlywood4')
        sqr1 = sqr.clone()
        sqr1.moveTo(size/2, a)
        sqr2 = sqr.clone()
        sqr2.moveTo(w - (size/2), a)
        sqr3 = sqr.clone()
        sqr3.moveTo(a, h - (size/2))
        sqr4 = sqr.clone()
        sqr4.moveTo(w/2, a)
        line = Path(Point(w/2,0),Point(w/2,h))
        line.setBorderWidth(3)
        
        paper.add(line) 
        paper.add(sqr) 
        paper.add(sqr1) 
        paper.add(sqr2) 
        paper.add(sqr3) 
        paper.add(sqr4)
        
        a += size

a = size/2 

# Adding numbers around the board

for i in range(6):
        
        text = Text(str(d))
        text.moveTo(a + size, h - (size/2))
        text.setDepth(49) # Making numbers visible by setting the depth to Depth < 50
        top_text = Text(str(b - d))
        top_text.move(a + size, size/2)
        text.scale(size * .03)
        top_text.scale(size * .03)
        a += size
        d += 1
        
        paper.add(top_text)
        paper.add(text)
        
        while d >= 7 and d <= 12:
                text = Text(str(d))
                text.moveTo(a + size * 2, h - (size / 2))
                text.setDepth(49)
                a += size
                top_text = Text(str(b - d))
                top_text.move(a + size, size / 2)
                d += 1
                text.scale(size * .03)
                top_text.scale(size * .03)
                
                paper.add(text)
                paper.add(top_text)

# Adding triangles to the board

for i in range(3):
        
        left = Layer() # left-hand layer of 4 triangles which is then cloned to the right-hand side of one square
        
        poly = Polygon(Point(c, size), Point(c + size, size), Point(c + size * .5, (h / 2) - (size / 2))) 
        poly.setFillColor('tan') 
        poly1 = poly.clone() 
        poly1.adjustReference(size / 2, size * 5)
        poly1.rotate(180)
        poly1.setFillColor('darkorange3')
        poly1.move(0, size)
        poly2 = poly1.clone()
        poly2.rotate(180)
        poly2.move(size, - size)
        poly3 = poly2.clone()
        poly3.rotate(180)
        poly3.move(0, size)
        poly3.setFillColor('tan')  
        left.add(poly3)
        left.add(poly2)
        left.add(poly1)
        left.add(poly)
        
        paper.add(left)
        
        right = left.clone()  # right-hand side triangles
        right.move(size * 7, 0)
        
        paper.add(right)
        
        c += size * 2 # adding the rest of triangles (Comment out this line to see how it works)
        
c = size
a = size * .05

# Adding circles to the board

for i in range(2):
        cir = Circle(size / 2, Point(size + (size /2), c + (size /2) - a))
        cir.setFillColor('white')
        cir.scale(.9)
        cir2 = cir.clone()
        cir2.setFillColor('black')
        cir2.moveTo(size * 1.5 ,h - c - (size/2) + a)
        c += size * .9
        paper.add(cir)
        paper.add(cir2)

c = size
for i in range(5): # 5-piece repeating circles added using the same technic as the triangles - layer and cloning
        
        circles = Layer()
        
        cir = Circle(size / 2, Point(w/2 - size, c + (size /2) - a))
        cir.setFillColor('black')
        cir.scale(.9)
        cir2 = cir.clone()
        cir2.setFillColor('white')
        cir2.moveTo(w/2 - size, h - c - (size/2) + a)
        c += size * .9
        circles.add(cir)
        circles.add(cir2)

        paper.add(circles)

        nextCircles = circles.clone()
        nextCircles.move(size * 7, 0)

        paper.add(nextCircles)
        
c = size
for i in range(3):
        cir = Circle(size / 2, Point(w/2 + size*2, c + (size /2) - a))
        cir.setFillColor('black')
        cir.scale(.9)
        cir2 = cir.clone()
        cir2.setFillColor('white')
        cir2.moveTo(w/2 + size*2, h - c - (size/2) + a)
        c += size * .9
        paper.add(cir)
        paper.add(cir2)
