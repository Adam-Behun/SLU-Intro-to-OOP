def threshold(values, goal):
    sum = 0
    counter =0
    for i in values:
        if i != 0:
            sum += i
            counter +=1
            if sum >= goal:            
                return counter
            
    return 0
          
print(threshold([5,3,0,0,0,0,0,0,2,9,1], 17))
