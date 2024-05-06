
n = []

try:
    while n != '':
        n += [int(input("Your number/s: "))]

except:
    def even(n):
        m = []
        for i in n:
            if i % 2 == 0:
                m += [i]
        return m
    print(even(n))
    print(n)
    print(set(even(n)))

