testcases = int(input())

for j in range(testcases):
    worktrips = int(input())
    count = []
    for i in range(worktrips):
        val = input()
        if val not in count:
            count.append(val)
    print(len(count))
    
