import math


hodnoty = []
amount = 0

try:
    while hodnoty != '':
        hodnoty += [int(input('Your number: '))]

except:
    average = sum(hodnoty) / len(hodnoty)
    for i in hodnoty:
        if i > average:
            print(f'{i} is bigger than the average.')
            amount += 1
        else:
            continue

if amount == 1:
    print("There is {} number that is above average.".format(amount))
else:
    print("There are {} numbers that are above average.".format(amount))