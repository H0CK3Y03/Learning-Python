import tkinter

canvas = tkinter.Canvas(width=800, height=600, bg='green')
canvas.pack()


def daco(event):
    canvas.delete('all')
    canvas.create_text(400, 300, text='Kto grga a prdi zdravie si tvrdi', font=('Arial', 20), fill='blue', anchor='center')


def daco1(event):
    canvas.delete('all')
    canvas.create_text(400, 300, text='Hlavne ze sme zdravi', font=('Arial', 20), fill='blue', anchor='center')


def daco2(event):
    canvas.delete('all')
    canvas.create_text(400, 300, text='Skola vola', font=('Arial', 20), fill='blue', anchor='center')


def daco3(event):
    canvas.delete('all')
    canvas.create_text(400, 300, text='Pomaly ďalej zajdes', font=('Arial', 20), fill='blue', anchor='center')


def daco4(event):
    canvas.delete('all')
    canvas.create_text(400, 300, text='Bez práce nie sú koláče', font=('Arial', 20), fill='blue', anchor='center')


def daco5(event):
    canvas.delete('all')
    canvas.create_text(400, 300, text='Dobrá rada je nad zlato', font=('Arial', 20), fill='blue', anchor='center')





canvas.bind_all('i', daco)
canvas.bind_all('l', daco1)
canvas.bind_all('o', daco2)
canvas.bind_all('v', daco3)
canvas.bind_all('e', daco4)
canvas.bind_all('u', daco5)

canvas.mainloop()
