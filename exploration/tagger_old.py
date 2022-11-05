##################################################################
# adam.behun@slu.edu
##################################################################

def loadLexicon():
    answer = []
    for line in open('lexicon.txt'):
      if line.strip():
        answer.append(line.split())   # list of [word, label] pairs
    return answer

lexicon = loadLexicon()
#print(lexicon)
#print(type(lexicon))

def labelToTag(label):
    tag = ' '   
    for line in lexicon:
        if line[1]=='age' or line[1]=='color' or line[1]=='size':
            tag = 'JJ'
        if line[1]=='person' or line[1]=='animal' or line[1]=='inanimate':
            tag = 'NN'
        if line[1]=='copula' or line[1]=='intransitive' or line[1]=='transitive':
            tag = 'VB'
        if line[1]=='determiner':
            tag = 'DT'
        else:
            raise ValueError('not one of the recognized labels')
    return tag

#taskOne = labelToTag()


def tagWord(word):
    tags = []
    for line in lexicon:
        functionCall = labelToTag()
        tags.append(functionCall)

    result = sorted(set(tags))
    return result

#taskTwo = tagWord()


def tagSentence(wordList):
    listoflists = []  
    for word in lexicon:
        functionCall = tagWord()
        listoflists.append(functionCall)
        
    return listoflists

    
def tagWordRefined(word):
    
    
    




##def tagSentenceRefined(wordList):
##    pass     # your code here...
##
##      
##if __name__ == '__main__':
##    if tagSentence(['the','big','wave']) != [['DT'], ['JJ'], ['NN', 'VB']]:
##        print('Error tagging "the big wave"')
##    if tagSentenceRefined(['an','antique','swing']) != [['determiner'], ['age', 'inanimate'], ['inanimate', 'intransitive']]:
##        print('Error tagging "an antique swing" with refined tags')



































