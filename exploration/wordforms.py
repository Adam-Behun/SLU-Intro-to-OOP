##################################################################
# Anonymous Authors
##################################################################

def pluralNoun(word):
    for i in range(len(word)):
        if word == 'man':
            return 'men'
        elif word == 'woman':
            return 'women'
        elif word == 'sheep':
            return 'sheep'
        elif word == 'goose':
            return 'geese'
        elif word == 'mouse':
            return 'mice'
        elif word == 'ox':
            return 'oxen'
        elif word == 'calf':
            return 'calves'
        elif word == 'thief':
            return 'thieves'
        elif word == 'wife':
            return 'wives'
        elif word == 'wolf':
            return 'wolves'
        else:
            return generic(word)
    
def singularVerb(word):
    for i in range(len(word)):
        if word == 'are':
            return 'is'
        elif word == 'have':
            return 'has'
        else:
            return generic(word)

# duplicate code for generic cases
def generic(word):
    if word[-1] == 'x' or word[-1] == 's' or word[-1] == 'z' or word[-1] == 'o':
        return word + 'es'
    elif word[-2:] == 'ch' or word[-2:] == 'sh':
        return word + 'es'  
    elif word[-1] == 'y':
        if word[-2] in 'aeiou':
            return word + 's'
        else:
            return word[:-1] + 'ies'  
    else:
        return word + 's'

# testing
if __name__ == '__main__':
    nounTests = (
        ('dog','dogs'),
        ('church', 'churches'),
        ('city', 'cities'),
        ('tax','taxes'),
        ('ox','oxen'),
        ('toy', 'toys'),
        ('boy', 'boys'),
        ('calf', 'calves'),
        ('thief','thieves'),
        ('wife', 'wives'),
        ('wolf', 'wolves'),
        )
    verbTests = (
        ('eat','eats'),
        ('tax','taxes'),
        ('have','has'),
        ('are', 'is'),
        )
    battery = (('Plural of noun', pluralNoun, nounTests),
               ('Singular of verb', singularVerb, verbTests))
    for msg,func,tests in battery:
        for (s,t) in tests:
            guess = func(s)
            if guess != t:
                print(msg,s,'is incorrect; expected',t,'but got',guess)
