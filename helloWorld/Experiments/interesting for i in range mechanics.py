from math import sqrt

n = int(input(': '))

print(sqrt(n))
print(sqrt(n) + 1)

for i in range(2, int(sqrt(n)) + 1):
    print(i)

for i in range(2, int(sqrt(n)) + 1):
    print("i")

for i in range(int(sqrt(n)) + 1, -8, -1):
    print(i)