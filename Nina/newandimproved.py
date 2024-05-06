import tkinter


platno = tkinter.Canvas(tkinter.Tk(), width=1000,height=600)
platno.pack()

def peta():
    platno.create_oval(x - 20, y - 20, x + 20, y + 20)
    platno.create_rectangle(x-20, y + 20, x + 20, y + 80)
    platno.create_text(x, y + 50, text=vstup.get())
    platno.create_line(x - 40, y + 85, x + 90, y + 85, x + 100, y + 80)


def ides():
    global x,y
    platno.delete("all")
    peta()
    x+=5
    y+=10
    platno.after(100, ides)

x=40
y=10

vstup = tkinter.Entry()
vstup.pack()

tlacidlo = tkinter.Button(text='Start',command =ides)
tlacidlo.pack()

platno.mainloop()