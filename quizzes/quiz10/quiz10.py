# Student:  adam.behun@slu.edu
# Student:  aksheytha.chelikavada@slu.edu

n = int(input('Enter a number: '))
while n != 1:
    print(int(n))
    if n%2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
print(int(n))
