
def ascend(a):
    x = a[0]
    for i in a:
        if i < x:
            return False
        x = i
    return True

n = []

try:
    while n != '':
        n += [int(input("Your number sir: "))]
except:
    print(ascend(n))