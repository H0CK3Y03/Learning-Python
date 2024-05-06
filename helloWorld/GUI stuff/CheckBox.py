from tkinter import *

def display():
    if(x.get()==1):                     # if onvalue and offvalue are integers we use this
        print("You agree!")
    else:
        print("You don't agree :(")

# def display():
#     if(x.get()):               # x.get() will return True of False so if True then, if False then.
#         print("You agree!")
#     else:
#         print("You don't agree :(")
#
# def display():
#     if(x.get()=="YES"):                     # if onvalue and offvalue are strings we use this
#         print("You agree!")
#     else:
#         print("You don't agree :(")

window = Tk()

photo = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Legion.png')

# x = StringVar()                  # if onvalue and offvalue are strings we use this
x = IntVar()                     # by default 1 and 0, if onvalue and offvalue are integers we use this
# x = BooleanVar()                     # True, False -> if onvalue and offvalue are booleans we use this

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,             # default value of variable x -> 1. We can change it to a boolean(True/False) and below
                           offvalue=0,            # default value of variable x -> 0. We can change it to a string("YES"/"NO") and above
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')

check_button.pack()


window.mainloop()



















































