n = int(input("Your number: "))

print(n, end=', ')

while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(n, end="")
    if n>1:
        print(end=", ")
    else:
        print(".")