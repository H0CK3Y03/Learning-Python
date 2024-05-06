#grid() = geometry manager that organizes widgets in a table-like structure in a parent
# from left to right (column 0 --> colum x) from top to bottom(row 0 --> row y), by default -> 1 row and 1 column to work with at the start

from tkinter import *

def submit():
    print(f'First name: {firstNameEntry.get()}')
    print(f'Last name: {lastNameEntry.get()}')
    print(f'email: {emailEntry.get()}')

window = Tk()

titleLabel = Label(window,text='Enter your info',font=('Arial',25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=20,bg='red').grid(row=1, column=0)
# firstNameEntry = Entry(window).grid(row=1,column=1)
firstNameEntry = Entry(window)
firstNameEntry.grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg='green').grid(row=2, column=0)
# lastNameEntry = Entry(window).grid(row=2,column=1)     # doesn't allow us to use .get() function
lastNameEntry = Entry(window)
lastNameEntry.grid(row=2,column=1)

emailLabel = Label(window,text="email: ",bg='blue',width=30).grid(row=3, column=0)
# emailEntry = Entry(window).grid(row=3,column=1)
emailEntry = Entry(window)
emailEntry.grid(row=3,column=1)

submitButton = Button(window,text="submit",command=submit).grid(row=4, column=0,columnspan=2) # columnspan places the widget between x columns

window.mainloop()



















