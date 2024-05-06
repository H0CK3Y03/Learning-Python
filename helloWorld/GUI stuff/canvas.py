# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()


canvas = Canvas(window,height=500,width=500)
canvas.pack()

# canvas.create_line(0,0,500,500,fill='blue',width=5)    # (startx,starty,endx,endy) 0,0 -> top left corner, 500,500 bottom right corner
# canvas.create_line(0,500,500,0,fill='red',width=5)     # overlaps the blue line, but stays on top because of order of code, pc executes from top to bottom
# canvas.create_rectangle(50,50,250,250,fill='purple')
# canvas.create_polygon(250,0,500,500,0,500,fill='yellow',outline='black',width=5)
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill='yellow',outline='black',width=5)
# canvas.create_arc(0,0,500,500,fill='green',style=PIESLICE, start=270,extent=180)  # default style is pie slice
canvas.create_arc(0,0,500,500,fill='red',extent=180,width=10)
canvas.create_arc(0,0,500,500,fill='white',extent=180,width=10,start=180)
canvas.create_oval(190,190,310,310,fill='white',width=10)

canvas.mainloop()






















