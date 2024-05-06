# try changing the distance variable by removing it from the append function
from tkinter import *
import math

WIDTH = 1000
HEIGHT = 1000
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/4

root = Tk()
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

vertices = [
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y + SIDE/2],
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y + SIDE/2],
]

def rotate(points, angle, center, i):
    change = i - i / 6
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    count = 0
    distance_x = points[1][0] - points[0][0]
    distance_y = points[1][1] - points[0][1]
    distance = distance_x * distance_x + distance_y * distance_y
    # distance -= change
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        if count % 4 == 0:
            new_points.append([x_new + cx, y_new + cy - distance])
        elif count % 4 == 1:
            new_points.append([x_new + cx + distance, y_new + cy])
        elif count % 4 == 2:
            new_points.append([x_new + cx, y_new + cy + distance])
        elif count % 4 == 3:
            new_points.append([x_new + cx - distance, y_new + cy])
        else:
            break
        count += 1
    return new_points

def draw_square(points):
    canvas.create_polygon(points, fill="", outline="black")

draw_square(vertices)
center = (CANVAS_MID_X, CANVAS_MID_Y)
new_square = rotate(vertices, 6, center, 0)
draw_square(new_square)
for i in range(60):

    new_square = rotate(new_square, 6, center, i)
    draw_square(new_square)


canvas.mainloop()
