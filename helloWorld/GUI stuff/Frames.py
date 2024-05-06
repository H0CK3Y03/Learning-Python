# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

# button = Button(
#     window,
#     text='W',
#     font=('Consolas',25),
#     width=3
# )
# button.pack()

frame = Frame(window,bg='pink',bd=5,relief=SUNKEN)
# frame.pack(side=BOTTOM)
frame.place(x=100,y=100)

Button(frame,text='W',font=('Consolas',25),width=3).pack(side=TOP)  # does the same thing but doesn't have a name
Button(frame,text='A',font=('Consolas',25),width=3).pack(side=LEFT)
Button(frame,text='S',font=('Consolas',25),width=3).pack(side=LEFT)
Button(frame,text='D',font=('Consolas',25),width=3).pack(side=LEFT)


window.mainloop()
















