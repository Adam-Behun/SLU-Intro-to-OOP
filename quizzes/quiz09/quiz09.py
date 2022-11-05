#####################################
# Quiz 09
#
# Students:
#   aksheytha.chelikavada@slu.edu  (replace this with actual address)
#   adam.behun@slu.edu  (replace this with actual address)
#
#####################################


######################################
# some sample data; of course your program should work on any such data
words = ['apple','Bayer', 'iPod', 'jaguar','Saturn']
######################################


######################################
# Your part of the code here
special = str([w for w in words if w.lower() != w]).lower()


######################################


######################################
# Let's see your results
print(special)
######################################
