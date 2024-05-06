import random


z = (int(input('How many euros: ')))
s = 0
games = int(input("How many games am I playing? "))

while z > 0 and s < games:
    x = [random.randint(1,20), random.randint(1,20), random.randint(1,20)]
    if len(x) == len(set(x)):
        z -= 1
        print('- 1', end=' ')
    elif len(set(x)) == 2:
        z += 5
        print('+ 5', end=' ')
    elif len(set(x)) == 1:
        z += 50
        print('+ 100', end=' ')
    else:
        print('No')
    s += 1

if z == 0:
    print('\nI have 0 euros now.')
else:
    print(f'\nI actually have {z} euros after playing {s} games.')

