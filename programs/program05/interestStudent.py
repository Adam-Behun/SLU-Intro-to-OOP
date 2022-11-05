##################################################################
# Student contributions to the interest calculator
# adam.behun@slu.edu
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#function which prints the first couple lines (introduction)

def greeting():
    
    print('This interest calculator will ask you to select an interest rate,')
    print('followed by a principal value.  It will then calculate and display')
    print('the principal, interest rate, and balance after one year. You will')
    print('then be invited to execute the process again or terminate.')

###---------------------------------------------------------------------------------

#function which asks the user to choose an interest rate from the provided options
    
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def getRate(choices):
    for i in range(len(choices)):
        print(alpha[i], str(choices[i]) + '%')
    option = input('Please, select an interest rate from the choices: ')
    option = option.upper()
    if len(option) > 1:
        print('Sorry this is an invalid response')
        return getRate(choices)
    elif option not in alpha[0:len(choices)]:
        print('Sorry this is an invalid response')
        return getRate(choices)
    else:
        return float(choices[alpha.index(option)]) * .01
    
###---------------------------------------------------------------------------------
    
#function which asks the user for principal

def getPrincipal(limit):
    response = input('Enter the principal, limit is: ' + str(limit) + ':')
    if '$' in response:
        response = response.strip('$')
    try:
        response = float(response)
    except ValueError:
        print('Please, enter a number only.')
        return getPrincipal(limit)
    if not float(response) <= float(limit):
        print('Please, enter amount lower than the limit.')
        return getPrincipal(limit)
    if not response > 0:
        print('Please, enter a positive amount')
        return getPrincipal(limit)
    if response > float(("{:.2f}".format(val))):
        print('Please enter dollars and cents only.')
        return getPrincipal(limit)

    return response

###---------------------------------------------------------------------------------

#function that returns the year-end balance taking principal and rate from previous functions

def computeBalance(principal, rate):
    balance = principal + (principal * rate)
    
    return balance

###---------------------------------------------------------------------------------

#function displaying results alligned according to the pattern assigned

def displayTable(principal, rate, balance):

    print('Initial Principle       Interest Rate    End of Year Balance')
    print('$%-23.2f%-17.2f$%-19.2f' % (principal, rate, balance))   #formatting the program's computations

###---------------------------------------------------------------------------------
  
#function that asks whether the user wants to compute some more examples or not
    
def askYesNo(prompt):
    
    response = input(prompt)  #asking for user input
    if len(response) == 0:
        return askYesNo(prompt)
    else:
        response = response[0].lower().strip()          #checking only the first lower-cased character

    while response not in ['y','n']:
        response = input(prompt)
        response = response[0].lower().strip()
        
    if response == 'y':
        return True
    elif response == 'n':
        return False
