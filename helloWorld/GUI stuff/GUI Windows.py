# GUI - Graphical User Interface

from tkinter import *   # import * -> imports everything related to tkinter module


# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serve as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window

window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file="C:\\Users\\adamv\\PycharmProjects\\helloWorld\\Advanced\\Legion.png")    # or "Legion.jpg"  # jpg doesn't work, only in PIL module, so we need to convert to png, also file size might be an issue
window.iconphoto(True, icon)
# window.config(background="black")
window.config(background='#0633ba')

window.mainloop()   # place window on computer screen, listen for events




































