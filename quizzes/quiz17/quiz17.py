####################################
# Students:
#  aksheytha.chelikavada@slu.edu
#  adam.behun@slu.edu
####################################

from data import zip2state, zip2pop

state2pop = {}
for zipcode in zip2pop.keys():

    x = zip2state[zipcode]

    if x in state2pop:
        state2pop[x] = state2pop[x] + zip2pop[zipcode]
    else:
        state2pop[x] = zip2pop[zipcode]

print(state2pop)
