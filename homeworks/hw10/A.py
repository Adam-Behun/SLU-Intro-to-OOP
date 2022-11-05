words = []
items = input('Start entering words: \n')
while words.count(items) < 2:
    items = input()
    words.append(items)
print('You already entered', words[-1]+'.')
print('You listed', len(words), 'distinct words.')
