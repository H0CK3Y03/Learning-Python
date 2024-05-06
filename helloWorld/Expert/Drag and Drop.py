from tkinter import *

def drag_start(event):
    widget = event.widget   # this will get the widget of the event that is happening
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    # label.winfo_x()  # will get the top left x coordinate of our label relative to the window it's in
    # label.winfo_y()  # will get the top left y coordinate of our label
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)


window = Tk()

label = Label(window,bg='red',width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg='blue',width=10,height=5)
label2.place(x=100,y=100)

label.bind('<Button-1>',drag_start)
label.bind('<B1-Motion>',drag_motion)  # when the left mouse button is held and you move the mouse inside the window

label2.bind('<Button-1>',drag_start)
label2.bind('<B1-Motion>',drag_motion)

window.mainloop()
























