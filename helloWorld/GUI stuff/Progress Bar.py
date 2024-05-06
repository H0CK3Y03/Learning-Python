from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 2
    while download < GB:
        bar['value'] += (speed / GB)*100   # max value is 100, this increases the value {start -> 0} by x everytime function is called
        download += speed
        time.sleep(0.05)      # the window waits for the bar to fill instead of updating us every second on the bar progress
        percent.set(f'{int((download / GB)*100)}%')  # sets the percent variable
        text.set(str(download)+"/"+str(GB)+' GB completed')     # sets the text variable
        window.update_idletasks()   # updates the window every iteration of the loop

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()

taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()



































