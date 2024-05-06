from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(          # this will open up the file browser and then it will return a string of the file location
                                          initialdir="C:\\Users\\adamv\\PycharmProjects\\helloWorld",  # this will set the initial directory of the browser
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"), # only shows .txt files, intially it looks for text files, but with the dropdown menu you can choose to look for all files because of the code below
                                          ('all files',"*.*")))  # this will look for all files

    file = open(filepath,'r')   # by default r -> 'rt' -read text, we can change it to 'rb' -read binary
    print(file.read())
    file.close()

window = Tk()

button = Button(window,text="Open",command=openFile)
button.pack()

window.mainloop()

























