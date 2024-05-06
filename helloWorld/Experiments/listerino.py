a = [1,2,3,55,66,77,66,77, 66,5456,465151]

x = a[0]
b = 0
for i in a:
    if i < x:
        print(i)
        print(x)
        b += 1
    x = i
print(f'final: {x}')
print(b)