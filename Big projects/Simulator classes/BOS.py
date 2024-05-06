import sys

sys.path.append("C:\Users\Adam Vesely\PycharmProjects\pythonProject\Big projects\Simulator classes\BOS.py")

class Bos:

    def __init__(self, count, position):

        self.count = count
        self.position = position


    def new_soldier(self, position):

        canvas.create_oval(position - 25, position - 25, position + 25, position + 25)