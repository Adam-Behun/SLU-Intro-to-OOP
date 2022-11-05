#I will compute the hypotenuse of a right triangle.
#But first, you must tell me the lengths of the legs.
a = float(input('What is the length of the first leg? '))
b = float(input('What is the length of the second leg? '))
c = str(((a ** 2) + (b ** 2)) ** 0.5)
print('The length of the hypotenuse is',c+'.')
input('press enter to end')
