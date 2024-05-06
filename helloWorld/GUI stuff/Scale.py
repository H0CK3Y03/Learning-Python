from tkinter import *

def submit():
    print(f'The temperature is: {scale.get()} degrees Celsius')

window = Tk()

photo_LEG = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Legion.png')
LEGLable = Label(image=photo_LEG)
LEGLable.pack()

scale = Scale(window,
              from_=100,          # value of scale
              to=0,
              length=600,         # length of scale length (not scale value)
              orient=VERTICAL,    # default VERTICAL, can be HORIZONTAL orientation of scale
              font=('Consolas',20),
              tickinterval=10,    # shows a number every x value/ numeric indicators on the scale for value
              # showvalue=0,      # will hide current value if 0, default is 1
              resolution=5,       # increment of slider
              troughcolor='#69EAFF',  # will change the sliding path of slider color but not the slider
              fg='#FF1C00',         # font color of the numbers
              bg='#111111',         #black background
              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])                    # sets starting point of slider on scale

scale.pack()

# photo_NCR = PhotoImage(file='C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\NCR.png')
# NCRLable = Label(image=photo_NCR)
# NCRLable.pack()

button = Button(window,
                text="submit",
                command=submit,
                )
button.pack()


window.mainloop()



















































