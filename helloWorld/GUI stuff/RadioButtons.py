# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered a hamburger")
    elif(x.get()==2):
        print("You ordered a hotdog")
    else:
        print("Huh?")

window = Tk()

photo_Legion = PhotoImage(file="C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Legion.png")
photo_NCR = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\NCR.png')
photo_Brotherhood = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Brotherhood.png')
foodImages = [photo_Brotherhood, photo_NCR, photo_Legion]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,          # groups radiobuttons together if they share the same variable
                              value=index,         # assigns each radio button a unique value
                              padx=25,
                              font=("Impact",50),
                              image=foodImages[index],
                              compound='left',
                              indicatoron=0,     # will eliminate circle indicators (they will look like pressable buttons)
                              width=1200,  # sets width of radio buttons
                              command=order)
    radiobutton.pack(anchor=W)                     # lines up the radiobuttons

window.mainloop()





















































