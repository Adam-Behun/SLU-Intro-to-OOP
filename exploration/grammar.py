##################################################################
# Student one: adam.behun@slu.edu
# Student two:
##################################################################

from tagger import *

def isGrammatical(wordList):
    x = labelToTag()
    if tag[1] == 'DT' and tag[2] == 'NN' and tag[3] == 'VB':
        return True
    else:
        return False




    
# The rest of this file is a test suite. You are welcome to add tests to
# the groups within, or even add a new group (though you'll need to be
# careful to mimic the given syntax for tests

if __name__ == '__main__':

    tests = (
        
        ('Simple Sentence Model',
         (
          ('the sheep run', True),
          ('the sheep swing', True),
          ('the wave run', True),      # okay for now
          ('a sheep run', True),       # okay for now
          ('an sheep run', True),      # okay for now
          ('run the sheep', False),
          ('the sheep', False),
          ('sheep run', False),
         ),
        ),


        ('With Augmented Lexicon',
         (
          ('the wolf run', True),     # okay for now
          ('the thief run', True),    # okay for now
         ),
        ),

    
        ('With Plural Nouns',
         (
          ('the cats run', True),
          ('the foxes run', True),
          ('the waves run', True),
          ('the waves wave', True),
          ('the thieves run', True),
          ('the thieves wave', True),
         ),
        ),

    
        ('With Singular Verb Forms',
         (
          ('the cat runs', True),
          ('the sheep runs', True),
         ),
        ),


        ('Enforcing Matching Singular/Plural Forms',
         (
          ('the cat runs', True),
          ('the cats run', True),
          ('the cat run', False),
          ('the cats runs', False),
         ),
        ),


        ('With Adjectives',
         (
          ('the big sheep run', True),
          ('the big white sheep run', True),
          ('the cat sheep run', False),
         ),
        ),


        ("Enforce 'a' followed by consonant and 'an' followed by vowel",
         (
          ('a fox runs', True),
          ('an fox runs', False),
          ('an old fox runs', True),
          ('a old fox runs', False),
          ('an engineer eats', True),
          ('a engineer eats', False),
         ),
        ),


        ("Do not allow 'a' or 'an' with plural noun",
         (
          ('a foxes swim', False),
          ('a fox swims', True),
          ('the foxes swim', True),
          ('the fox swims', True),
         ),
        ),


        ("Enforce appropriate ordering of adjectives",
         (
          ('the big old red fox swims', True),
          ('the red old big fox swims', False),
         ),
        ),

    )

for label,subtests in tests:
    print(label)
    for sentence,expected in subtests:
        try:
            result = isGrammatical(sentence.split())
            label = 'SUCCESS:' if result==expected else 'FAILED: '
            print(' ',label,sentence, '(returned '+str(result)+')')
        except Exception as e:
            print('  FAILED: ',sentence,'unexpected exception')
            print(e)
    print()


