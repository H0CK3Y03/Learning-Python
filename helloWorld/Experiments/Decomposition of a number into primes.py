def prime_num(n):
    print("{} =\t".format(n), end="")
    i = 2
    while n > 1:
        if n % i == 0:
            print(i, end=" ")
            n = n // i
            if n > 1:
                print("*", end=" ")
        else:
            i = i + 1
    print()

k = int(input("Choose a number you want to decompose into prime numbers: "))
prime_num(k)







