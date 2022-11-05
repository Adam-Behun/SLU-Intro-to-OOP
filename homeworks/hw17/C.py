def letterFrequency(word):
    counter = {}
    for w in word:
        if w in counter:
            counter[w] += 1
        else counter[w] = 1
    return counter
