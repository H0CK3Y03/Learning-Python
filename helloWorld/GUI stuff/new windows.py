from tkinter import *

def create_window():
    # new_window = Toplevel()   # Toplevel() = new window on top of the other windows, linked to a bottom window, if we close a bottom level window, the top level windows also close, but not vice versa
    new_window = Tk()         # TK() = new independent window
    old_window.destroy()      # close out of old window

old_window = Tk()

button = Button(old_window,text='create new window',command=create_window)
button.pack()

old_window.mainloop()



















