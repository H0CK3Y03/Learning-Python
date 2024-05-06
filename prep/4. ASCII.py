with open("ascii.txt", "w") as file:
    for i in range(32, 127):
        file.write(f'{i} = {chr(i)}\n')
with open("ascii.txt", "r") as file:
    print(file.read())