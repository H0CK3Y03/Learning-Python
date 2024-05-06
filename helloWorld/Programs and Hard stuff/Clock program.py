from tkinter import *
from time import *

def update():
    time_string = strftime('%I:%M:%S %p')   # converts a tuple representing time as a string, look at python library on internet
    time_label.config(text=time_string)   # displays the time

    day_string = strftime('%A')
    day_label.config(text=day_string)  # displays the day

    date_string = strftime('%d %B,%Y')
    date_label.config(text=date_string)

    window.after(1000,update)    # 1000 miliseconds  # a recursive function -> a function that calls itself within itself
                                     # after 1000ms or 1s the function calls itself again


window = Tk()

time_label = Label(window,font=('Arial',50),fg='#00FF00',bg='#000000')
time_label.pack()

day_label = Label(window,font=('Ink Free',20))
day_label.pack()

date_label = Label(window,font=('Ink Free',30))
date_label.pack()

update()

window.mainloop()














