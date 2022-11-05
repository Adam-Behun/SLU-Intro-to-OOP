from random import randrange

trials = 10000
totalflips = 0  
maxflips = 0          

for t in range(trials):
    count = 1
    while randrange(2) != 0:
        count += 1

    totalflips += count
    maxflips = max(count, maxflips)

print('Average number of flips:', totalflips/trials)
print('Maximum number of flips:', maxflips)
