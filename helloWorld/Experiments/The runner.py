km = int(input("What distance did he run the first day: "))
goal = int(input("What distance was he supposed to reach: "))

i = 1
while km < goal:
    km = km * 1.10
    i = i + 1

print("The runner reached his goal ({} km) on his {}. day".format(goal, i))
