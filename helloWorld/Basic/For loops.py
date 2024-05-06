import time
# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#                     while loop = unlimited
#                     for loop = limited

#for i in range(10):        # index(i) is most commonly used
    #print(i + 1)

#for i in range(50,100+1,2):
    #print(i)

#for i in "Adam Vesely":
    #print(i)

for seconds in range(10, -3,-1):       #(start-inclusive, stop-exclusive, step[if negative then in reverse]
    print(seconds)
    time.sleep(1)
print("Happy New Year!!!")