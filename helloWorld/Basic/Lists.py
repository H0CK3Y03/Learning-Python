# list = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]        #food is now a list instead of a string, to verify: print(type(food))

food[0] = "sushi"   #list is now updated to sushi,hamburger....

# food.append("ice cream")
# food.remove("hotdog")
# food.pop()    #will remove last element
# food.insert(0,"cake")
# food.sort()        #sorts alphabetically
# food.clear()        #clears list


for x in food:
    print(x + " ",end="")
