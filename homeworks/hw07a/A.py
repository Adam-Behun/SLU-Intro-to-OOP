from math import *

square = 0
response = int(input('Enter k: '))
for n in range(response):
    square = square + pow(response, 2)
    response = response - 1
square = int(square)    
print(square)  
