# adam.behun@slu.edu
# aksheytha.chelikavada@slu.edu

from random import *

trails = 10000
k = 20

totalsteps = 0
minsteps = 0
maxsteps = 0

for t in range(trails):
    stepsinloop = 0
    count = 0
    while abs(stepsinloop) < k:
        count += 1
        stepsinloop += -1 + 2 * randrange(2)
    totalsteps += count
    if t == 0:
        minsteps = maxsteps = count
    else:
        minsteps = min(count,minsteps)
        maxsteps = max(count,maxsteps)

print('Average steps:',totalsteps/trails)
print('Maximum steps:',maxsteps)
