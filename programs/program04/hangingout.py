response = input().split()

limit = int(response[0])
countturned = 0
onroof = 0
for i in range(int(response[1])):
    val = input().split()
    if val[0] == 'enter':
        
        if onroof + int(val[1]) <= limit: 
            onroof = int(val[1]) + onroof
        else:
            countturned += 1
    elif val[0] == 'leave':
        onroof -= int(val[1])
print(countturned)
