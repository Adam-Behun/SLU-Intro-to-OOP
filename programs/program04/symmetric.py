original = []
item = 1

count = 0

while True:
    item = int(input())
    if item == 0:
        break
    count += 1
    for i in range(item):
        name = input()
        original.append(name)
    beg = []
    end = []

    for i in range(len(original)):
        if i%2 == 0:
            beg.append(original[i])
        elif i%2 == 1:
            end.append(original[i])

    end = end[::-1]
    final = beg + end
    for i in final:
        print(i)
        print('Set',str(count))
    beg.clear()
    end.clear()
    original.clear()
# I want to create the final list and then print it all at once ut do not know how to do that.
