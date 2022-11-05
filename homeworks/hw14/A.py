weight = 0.0
while not weight > 0.0:
    try:
        weight = float(input('Enter a weight in pounds: '))
        if not weight > 0.0:
            print('Weights must be nonnegative.')
    except ValueError:
        print(('That is not a valid number.'))
kilograms = weight * 0.45359
print('That is equal to', round(kilograms,5),'kilograms')

# how can I round it to 1.13398?
# this is not working print(round(kilograms, 5))
