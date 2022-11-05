name = input('Your name in form of FN MN LN: ')
sepNames = []
sepNames = name.split(' ')
result = sepNames[1]
result1 = result.capitalize()
result2 = result1[0]
print(sepNames[0], result2+'.', sepNames[2])

