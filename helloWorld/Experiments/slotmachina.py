import random


z = (int(input('How many euros: ')))
s = 0

while z > 0 and s < 1000:
    x = [random.randint(1,20), random.randint(1, 20), random.randint(1, 20)]
    if len(x) == len(set(x)):
        z -= 1
        print('- 1', end=' ')
    elif len(set(x)) == 2:
        z += 5
        print('+ 5', end=' ')
    elif len(set(x)) == 1:
        z += 100
        print('+ 100', end=' ')
    else:
        print('No')
    s += 1
    print(len(set(x)), end='   ')
    print(x)
    print(s)
    print(z)




if z == 0:
    print('Ostalo mi 0 eur.')
else:
    print(f'Ostalo mi {z} eur po 1000 hrach.')


print(s)
print(z)
