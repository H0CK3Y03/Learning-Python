from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(      # opens the file browser and saves your current file to wherever you choose
        initialdir='C:\\Users\\adamv\\PycharmProjects\\helloWorld',
        defaultextension='.txt',
        filetypes=[
            ("Text file",".txt"),
            ("HTML file",".html"),
            ("All files",".*"),
        ]
    )
    if file is None:
        return        # if we close before saving we don't get any errors now because it returns None
    filetext = str(text.get(1.0,END))  # 1.0 is the beginning of the text area, this gets everything from the text area
    # filetext = input("Enter some text I guess: ") # uses the console window instead of the text area
    file.write(filetext)
    file.close()

window = Tk()

button = Button(window,text='save',command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()


























