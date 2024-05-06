# slicing = create a substring by extracting elements from another string
#               indexing[] or slice()
#               [start:stop:step]  (start,stop,step)
#               [inclusive:exclusive:how much we increase our index by between starting and stopping, by default 1]
#  characters have both a positive and negative index n...3,2,1,0 = -1,-2,-3...-n  (n=-1, 0=-n, 1=-n+1, -2=n-1....)

#name = "Bro Cade"

#first_name = name[0:3]  #or [:3] because it's the beginning    #computers always start with zero, the stopping index is not include in the slice
#last_name = name[4:8]  #or [4:]
#funky_name = name[0:8:2]   #or [::2]  #displays every second character starting from the first one
#reversed_name = name[::-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice_website = slice(7,-4)

print(website[slice_website])
print(website2[slice_website])
print(type(slice_website))


