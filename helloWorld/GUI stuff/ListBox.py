# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))   # listbox.get(index[this index is a position]) gets us the current item at the index number in the for loop

    print("You have ordered: ",end='')
    # print(listbox.get(listbox.curselection()))  # gets the current selection of items from the listbox, this does not work for MULTIPLE selection
    for index in food:
        print(index, end='')
        if index != food[-1]:
            print(end=", ")
        elif index == food[-1]:
            print('.')

def add():
    listbox.insert(listbox.size(),entryBox.get())  # inserts the contents of the entrybox into the current size of listbox(last character)
    listbox.config(height=listbox.size())          # readjusts the listbox size to fit all of the content

def delete():
    for index in reversed(listbox.curselection()):   # the indexes change so we need to reverse(we now start at the last index) the selection, that way the items behind the last item move upwards so the items in front of the last item don't move
        listbox.delete(index)
    # listbox.delete(listbox.curselection())   # deletes the current selection, this does not work for current selection
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE,          # setting this to MULTIPLE allows us to select more stuff, default is SINGLE
                  )
listbox.pack()

listbox.insert(1,"pizza")   # inserts selectable text into the position in the listbox
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())    # dynamically changes the height of the listbox depending on the items within it

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()

window.mainloop()





















