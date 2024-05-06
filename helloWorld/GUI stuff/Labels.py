# label = an area widget that holds text and/or an image within a window
# widgets will change their size to accommodate all of the components within the widget

from tkinter import *

window = Tk()

photo = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Legion.png')

label = Label(window,                              # syntax -> Label(container[this case window], argument/s)
              text="bro, do you even code?",
              font=('Arial',40,'bold'),
              foreground='#00FF00',                # foreground -> fg = font color (color of text)
              background='black',                  # background -> bg = background of only text
              relief=RAISED,                       # relief -> border, can be RAISED or SUNKEN
              bd=10,                               # bd = border width
              padx=20,                             # padx -> adds some padding (space) between text and border on x axis (right and left)
              pady=20,                             # pady -> adds some padding (space) between text and border on y axis (up and down)
              image=photo,                         # adds an image (but in front of the text)
              compound='bottom')                   # compound -> sets a direction of where the image is placed relative to the text

label.pack()          # does the same thing as place, but you can't change the coordinates (as far as I know)
# label.place(x=100,y=100)

window.mainloop()



















