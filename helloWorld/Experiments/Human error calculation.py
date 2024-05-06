from tkinter import *
import time

WIDTH = 1000
HEIGHT = 1000

def doSomething(event):

    print('Mouse coordinates: ' + str(event.x) + ', ' + str(event.y))
    time.sleep(0.01)
    list_of_y.append(abs(event.y - 500))

    result = sum(list_of_y) / len(list_of_y)

    label = Label(canvas,
                  text=f' Your average error is {result:.3f} pixels',
                  font=("Arial", 40),
                  background="#111111",
                  foreground="#00FF00")
    label.place(anchor=N, x=WIDTH / 2, y=100)

# def combined_function(event):  # commented out section doesn't allow real time results
#
#     average()
#     handle_event()


# def average():
#
#     global list_of_y
#     result = sum(list_of_y) / len(list_of_y)
#     return result
#
# def handle_event():

    # global result
    # result = average()
    #
    # label = Label(canvas,
    #               text=f' Your average error is {result:.2f} pixels',
    #               font=("Arial", 40),
    #               background="#222222",
    #               foreground="#00FF00")
    # label.place(anchor=N,x=WIDTH/2, y=100)

window = Tk()
window.title("Human Error Calculation")


canvas = Canvas(window, width=WIDTH, height=HEIGHT, background="#111111")
canvas.pack()

window.update()  # for the window to be centered by code below we need to have this line here

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")



canvas.create_line(0 + 50,HEIGHT/2 - 50,WIDTH - 50,HEIGHT/2 - 50, width=5,fill='#00AA00')
canvas.create_line(0 + 50,HEIGHT/2,WIDTH - 50,HEIGHT/2,fill="white")
canvas.create_line(0 + 50,HEIGHT/2 + 50,WIDTH - 50,HEIGHT/2 + 50, width=5,fill='#00AA00')



list_of_y = []

window.bind("<B1-Motion>", doSomething)

result = None

# window.bind("<ButtonRelease>", combined_function)

controls = Label(canvas,
                 background="#111111",
                 foreground="lightblue",
                 font=("Courier", 20),
                 text="Press and hold the left mouse button to start")
controls.place(x=WIDTH/2, y=HEIGHT/2 + 100, anchor=CENTER)

instructions = Label(canvas,
                 background="#111111",
                 foreground="lightblue",
                 font=("Courier", 20),
                 text="Move your mouse from one end to the other")
instructions.place(x=WIDTH/2, y=HEIGHT/2 + 150, anchor=CENTER)

window.mainloop()