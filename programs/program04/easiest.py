x = input()


def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

while int(x) != 0:
    y = getSum(x)
    p = 11
    while p <= 150:
        n = p * int(x)
        if getSum(n) == y:
            break
        else:
            p += 1
    print(p)
    x = input()
