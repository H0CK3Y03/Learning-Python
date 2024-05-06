import tkinter

canvas = tkinter.Canvas()
canvas.pack()

# for i in range(1,11):
#     print(i*10)
#     canvas.create_line(10, i*10, 200, i*10)
#     canvas.update()
# koniec prveho obrazku v 1. ulohe

# for i in range(1,6):
#     print(i*10)
#     canvas.create_line(i*10, i*10, 200, i*10)
#     canvas.update()
# koniec druheho obrazku v 1. ulohe

# for i in range(1,6):
#     print(i*10)
#     canvas.create_line(10, i*10, 200, i*25)
#     canvas.update()
# koniec tretieho obrazku v 1. ulohe

# for i in range(1,11):
#     print(i*10)
#     canvas.create_line(i*10, 10, i*10, 200)
#     canvas.update()
# koniec 1. obrazku v 2. ulohe

# for i in range(1,6):
#     print(i*10)
#     canvas.create_line(i*10, i*30, i*10, 200)
#     canvas.update()
# koniec 2. obrazku v 2. ulohe

for i in range(1,6):
    print(i*10)
    canvas.create_line(i*10, i*20, i*10, i*20 + 100)
    canvas.update()
# koniec 3. obrazku v 2. ulohe





































canvas.mainloop()
