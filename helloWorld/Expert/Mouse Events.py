from tkinter import *

def doSomething(event):
    print('Mouse coordinates: ' + str(event.x) + ', ' + str(event.y))  # event.x/y -> gives the current x/y coordinates of your mouse on the window when you press call the function by an event


window = Tk()

# window.bind('<Button-1>',doSomething)  # left click
# window.bind('<Button-2>',doSomething)  # middle mouse button (press, not scroll)
# window.bind('<Button-3>',doSomething)  # right click
# window.bind('<Button-4>',doSomething)  # side mouse button (closer to user)
# window.bind('<Button-5>',doSomething)  # side mouse button (further away from user)
# window.bind('<ButtonRelease>',doSomething)  # only after releasing a button on the mouse will the event call the function
# window.bind('<Enter>',doSomething)   # when your cursor enters the window
# window.bind('<Leave>',doSomething)    # when your cursor leaves the window
# window.bind('<Motion>',doSomething)   # whenever you move your mouse inside the window
# window.bind('<ButtonRelease-1>',doSomething)  # when you release the left mouse button
# window.bind('<MouseWheel>',doSomething)  # when you scroll up and/or down with the MouseWheel


window.mainloop()

















