z = 1
n = 0
x = n
correct = 1

while n != "":
    n = input("The height of the {}. student: ".format(z))
    z = z + 1
    if n != '':
        if int(n) < int(x):
            correct = 0
            # break
        else:
            x = n
            continue
    else:
        break


if correct == 1:
    print('The students are in the right order.')
else:
    print('The students are in the wrong order.')
