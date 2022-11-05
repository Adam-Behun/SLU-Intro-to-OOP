def doSomething(word,k):
    result = input.split()
    word, k = result[0], int(result[1])
    if not word:
        raise ValueError('empty string')
    if not isinstance(k,(int)):
        raise TypeError('k must be an integer')
    if k > len(word):
        raise IndexError('k is greater than len(word)')
    # doSomething function body
