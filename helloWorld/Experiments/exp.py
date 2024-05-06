n = int(input("Your number: "))
x = int(input("Divider"))
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
#
# print(is_prime(n))

while n > 1:
    n = n / x
    print(n)
