import tkinter, random

canvas = tkinter.Canvas(width=1000, height=1000, )
canvas.pack()

def pozadie(x,y,f,a):
    canvas.create_rectangle(x,y,x+1000,y+550,fill=f)
    canvas.create_rectangle(x, y+550, x+1000, y+1000, fill=a)

def mrakodrap (x,y,f,a):
    canvas.create_rectangle(x,y,x+100,y+500,fill=f)
    canvas.create_rectangle(x+10,y,x+20,y+380,fill=a)
    canvas.create_rectangle(x+35,y,x+45,y+380,fill=a)
    canvas.create_rectangle(x+55,y,x+65,y+380,fill=a)
    canvas.create_rectangle(x+80,y,x+90,y+380,fill=a)
    canvas.create_rectangle(x,y,x+100,y+10,fill=f)
    canvas.create_rectangle(x,y+30,x+100,y+40,fill=f)
    canvas.create_rectangle(x,y+60,x+100,y+70,fill=f)
    canvas.create_rectangle(x,y+90,x+100,y+100,fill=f)
    canvas.create_rectangle(x,y+120,x+100,y+130,fill=f)
    canvas.create_rectangle(x,y+150,x+100,y+160,fill=f)
    canvas.create_rectangle(x,y+180,x+100,y+190,fill=f)
    canvas.create_rectangle(x,y+210,x+100,y+220,fill=f)
    canvas.create_rectangle(x,y+240,x+100,y+250,fill=f)
    canvas.create_rectangle(x,y+270,x+100,y+280,fill=f)
    canvas.create_rectangle(x,y+300,x+100,y+310,fill=f)
    canvas.create_rectangle(x,y+330,x+100,y+340,fill=f)
    canvas.create_rectangle(x+25,y+400,x+75,y+500,fill=a)
    canvas.create_rectangle(x+30,y+500,x+70,y+550, fill='gray')


def oblak (x,y,f):
    canvas.create_oval (x,y,x+40,y+50,fill=f,outline = '')
    canvas.create_oval (x+30,y-20,x+70,y+50,fill=f,outline = '')
    canvas.create_oval (x+60,y,x+100,y+50, fill=f,outline = '')
    canvas.create_rectangle (x+10,y+30,x+90,y+50,fill=f,outline = '')

def pan (x,y,f,a):
    canvas.create_oval(x + 25, y, x + 55, y + 30,fill=a)
    canvas.create_line(x + 35, y + 30, x + 20, y + 45)
    canvas.create_line(x + 45, y + 30, x + 60, y + 45)
    canvas.create_rectangle(x + 35, y + 30, x + 45, y + 50, fill=f)
    canvas.create_line(x + 38, y + 50, x + 35, y + 70)
    canvas.create_line(x + 42, y + 50, x + 50, y + 70)
    canvas.create_oval(x + 32, y + 10, x + 37, y + 15, fill=f)
    canvas.create_oval(x + 42, y + 10, x + 47, y + 15, fill=f)
    canvas.create_line(x + 32, y + 22, x + 47, y + 22)

def vagon (x,y):
    canvas.create_line(x-5,y+22,x+55,y+22,width=2)
    canvas.create_oval(x+5,y+20,x+15,y+30,fill='black')
    canvas.create_oval(x+35,y+20,x+45,y+30,fill='black')
    canvas.create_rectangle(x,y,x+50,y+25,fill='green')
    canvas.create_rectangle(x+5,y+5,x+15,y+15,fill='skyblue')
    canvas.create_rectangle(x+20,y+5,x+30,y+15,fill='skyblue')
    canvas.create_rectangle(x+35,y+5,x+45,y+15,fill='skyblue')

def dama(x,y,f,a):
    canvas.create_oval(x+30,y,x+70,y+35,fill=a)
    canvas.create_line(x+20,y+45,x+40,y+35)
    canvas.create_line(x+50,y+35,x+80,y+45)
    canvas.create_polygon(x+40,y+35,x+60,y+35,x+20,y+70,x+70,y+70,fill=f)
    canvas.create_oval(x+45,y+13,x+42,y+15)
    canvas.create_oval(x+60,y+13,x+57,y+15)
    canvas.create_line(x+43,y+25,x+59,y+25)

def auto(x,y,f,a,b):
    canvas.create_rectangle(x,y,x+40,y+25,fill=f)
    canvas.create_rectangle(x+40,y+10,x+50,y+25,fill=f)
    canvas.create_polygon(x+40,y+10,x+50,y+10,x+40,y,fill=a)
    canvas.create_oval(x+5,y+20,x+15,y+30,fill=b)
    canvas.create_oval(x+30,y+20,x+40,y+30,fill=b)

def rusen(x,y,f,a,b):
    canvas.create_rectangle(x,y,x+50,y+25,fill=f)
    canvas.create_oval(x,y+25,x+12,y+35,fill=a)
    canvas.create_oval(x+12,y+25,x+24,y+35,fill=a)
    canvas.create_oval(x+24,y+25,x+36,y+35,fill=a)
    canvas.create_oval(x+36,y+25,x+48,y+35,fill=a)
    canvas.create_rectangle(x+10,y-10,x+20,y,fill=b)
    canvas.create_rectangle(x+30,y-20,x+50,y,fill=a)
    canvas.create_line(x+10,y-20,x+9,y-12)
    canvas.create_line(x+15,y-20,x+14,y-12)
    canvas.create_line(x+20,y-20,x+19,y-12)
    canvas.create_line(x+25,y-20,x+24,y-12)
def chodnik(x,y):
    canvas.create_line(x,y,x+1000,y)
    canvas.create_line(x, y+70, x + 1000, y+70)
    canvas.create_rectangle(x,y+1,x+1000,y+69,outline='gray',fill='lightgray')
def kolajnice(x,y,z,f):
    for i in range(20):
        canvas.create_line(x+i*50,y-10,x+i*50,y+40,fill=f,width=z)
    canvas.create_line(x,y,x+1000,y,width=z-5)
    canvas.create_line(x,y+30,x+1000,y+30,width=z-5)
def cesta(x,y):
    canvas.create_rectangle(x, y + 1, x + 1000, y + 69, fill='dark gray')
    canvas.create_line(x,y,x+1000,y)
    canvas.create_line(x, y+70, x + 1000, y + 70)
    for i in range(10):
        canvas.create_line(x+i*100,y+35,x+i*100+20,y+35,fill='white',width=5)


pozadie(0,0,"lightblue","light green")

chodnik(0,600)
cesta(0,670)

rusen(50,120,'red','black','blue')

auto(700,670,"red","blue","black")
auto(680,700,"yellow","green","black")
auto(450,700,"blue","orange","black")
auto(160,670,"green","blue","black")

mrakodrap(10,50,'black','blue')
mrakodrap(300,50,'green','red')
mrakodrap(850,50,'red','yellow')

pan(100,600,'green','beige')
dama(150,600,'crimson','beige')
pan(500,600,'blue','brown')
dama(550,600,'purple','salmon')


kolajnice(0,800,10,'brown')

x=350
for i in range(5):
    vagon(x,800)
    x+=60

for i in range(random.randint(0,5)):
    oblak(random.randint(0,700),random.randint(20,200),random.choice(('blue','gray')))

canvas.mainloop()