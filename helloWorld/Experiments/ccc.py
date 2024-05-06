import random

myList = [random.randint(1,20)]
dupItems = []
uniqItems = {}

print("List = ",myList)

for x in myList:
	if x not in uniqItems:
		uniqItems[x] = 1
	else:
		if uniqItems[x] == 1:
			dupItems.append(x)
		uniqItems[x] += 1
print("Duplicate Elements = ",dupItems)