class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)  # starting x,y, then xdiameter and y diameter, basically a square
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        print(f'{self} coordinates: {coordinates}')

        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0: # [2] -> bottom right of the 'square' (inscribed circle -> vpisana kruznica)
            self.xVelocity *= -1

        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.yVelocity *= -1

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)


