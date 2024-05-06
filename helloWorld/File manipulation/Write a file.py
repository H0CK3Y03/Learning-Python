# text = "Yoooooooooooo\nThis is some text\nHave a good one!\n"
# text = "Uh oh! This text has been overwritten"
text = "Have a nice day! See ya"
text1 = "\nI hope this works"



with open('test2.txt','w') as file:     # w -> write, by default it is 'r' -> read
    file.write(text)

with open('test1.txt','a') as file:       # a -> append
    file.write(text + text1)








