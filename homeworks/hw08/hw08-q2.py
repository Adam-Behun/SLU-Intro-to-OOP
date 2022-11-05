######################################
# hw08 Question 2 template
######################################


######################################
# some sample data; of course your program should work on any such data
words = ['apple', 'kayak', 'aha', 'midnight', 'noon']
######################################


######################################
# Your part of the code here
palindromes = []
for word in words:
    if word[0:] == word[::-1]:
        palindromes.append(word)



######################################


######################################
# Let's see your results
print(palindromes)
######################################
