from tkinter import *

def openFile():
    print('File has been opened!')

def saveFile():
    print("File has been saved")

def cut():
    print('You cut some text')

def copy():
    print('You copied some text')

def paste():
    print('You pasted some text')

window = Tk()

BOS = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Brotherhood.png')
LEG = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Legion.png')
NCR = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\NCR.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=('MV Boli',15))   # tearoff = 0 -> this removes a command with a label of only straight lines (- - - - - -)
menubar.add_cascade(label="File",menu=fileMenu)    # this will add a dropdown menu effect
fileMenu.add_command(label='Open',command=openFile,image=BOS,compound="right")   # this will create a clickable option under the fileMenu
fileMenu.add_command(label='Save',command=saveFile, image=LEG,compound='left')
fileMenu.add_separator()           # this will separate your commands via a thin line
fileMenu.add_command(label='Exit',command=exit,image=NCR,compound=BOTTOM)   # quit and exit both work perfectly fine

editMenu = Menu(menubar,tearoff=0,font=('MV Boli',15))
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Cut',command=cut)
editMenu.add_command(label='Copy',command=copy)
editMenu.add_command(label='Paste',command=paste)

window.mainloop()






























