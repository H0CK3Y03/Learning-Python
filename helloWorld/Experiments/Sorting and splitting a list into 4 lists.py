import random


num_list = []

while len(num_list) < 100:
    num_list += [random.randint(-1000, 1000)]

random.shuffle(num_list)
Blue = num_list[:(len(num_list) // 4)]
Green = num_list[(len(num_list) // 4):(len(num_list) // 4 * 2)]
Red = num_list[(len(num_list) // 4 * 2):(len(num_list) // 4 * 3)]
Yellow = num_list[(len(num_list) // 4 * 3):]

print(num_list)
print(len(num_list))
print(Blue)
print(len(Blue))
print(Green)
print(len(Green))
print(Red)
print(len(Red))
print(Yellow)
print(len(Yellow))