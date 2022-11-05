# Defining a function to reverse a string
def seq_reverser(x):
    return x[::-1]

# Asking user for the input of a dna and a pattern
original = input('Enter a DNA Sequence: ')
pattern = input('Enter the pattern: ')

# Reversing the user given pattern
reversedPattern = seq_reverser(pattern)

# Splitting the user given DNA into two strings
original = original.split(pattern, 1)

# Splitting the leftover string from last split 
middle = original[1].split(reversedPattern, 1)

# Reversing the middle part
reversedMiddle = seq_reverser(middle[0])

# Printing out appropiate outputs
print('Prefix:', original[0])
print('Marker:', pattern)
print('Middle:', middle[0])
print('Reversed Middle:', reversedMiddle)
print('Reversed Marker:', reversedPattern)
print('Suffix:', middle[1])
print('Result:', original[0]+pattern+reversedMiddle+reversedPattern+middle[1])
