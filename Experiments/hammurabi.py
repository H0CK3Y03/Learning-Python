def TowerOfHanoi(n , source, destination, auxiliary):
    global counter
    counter += 1
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
n = 1

counter = 0
TowerOfHanoi(n,'A','B','C')
print(counter)
