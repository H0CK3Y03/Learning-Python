from tkinter import *

from tkinter import messagebox    # import the messagebox library

def click():
    # messagebox.showinfo(title='This is an info message box', message='You are a person')    # shows a message (from your OS)

    # while(True):   # when you close the window, a new one pops up (virus)
    #     messagebox.showwarning(title='WARNING!',message='You have a VIRUS!!!!!')  # different icon, this is a warning message box(also from your OS)

    # messagebox.showerror(title='ERROR',message='Something went wrong')  # again different icon, error window from your OS

    # if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing'):  # windows confirmation window with a question and 2 options -> 'ok' and 'cancel'. Adding 'if' to the beginning will return True if you click ok or False if you click cancel
    #     print('You did a thing!')
    # else:
    #     print('You canceled a thing :(')

    # if messagebox.askretrycancel(title='ask retry cancel',message='Do you want to retry the thing'): # a OS confimation window but with an option to retry or cancel, retry returns a True value, cancel returns a False value
    #     print('You retried a thing')
    # else:
    #     print('You canceled a thing :(')

    # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):   # a OS question window with the options Yes and No, Yes returns a True value, No returns a False value
    #     print('I like cake too')
    # else:
    #     print('Why do you not like cake? :(')

    # answer = messagebox.askquestion(title='ask question',message='Do you like pie?')  # returns the strings 'yes' and 'no' instead of True and False
    # if answer == 'yes':
    #     print('I like pie too :)')
    # else:
    #     print('Why do you not like pie? :(')

    answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you like to code?', # returns True for yes, False for no and None for cancel
                                       icon='question')  # sets the icon [and the sound] to one of the other preset icons ('warning','info','error','question')
    if answer == True:
        print('You like to code :)')
    elif answer == False:
        print('Then why are you watching a video on coding?')
    else:
        print('You have dodged the question')

window = Tk()

button = Button(window, command=click,text="click me")
button.pack()


window.mainloop()

























