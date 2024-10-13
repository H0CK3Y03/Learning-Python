import tkinter as tk

# Function to create the house
def draw_house(canvas):
    # House body
    canvas.create_rectangle(150, 200, 300, 350, fill='lightblue', outline='black')

    # Roof
    canvas.create_polygon(140, 200, 230, 130, 320, 200, fill='brown', outline='black')

    # Door
    canvas.create_rectangle(210, 280, 240, 350, fill='darkbrown', outline='black')

    # Windows
    canvas.create_rectangle(170, 220, 190, 240, fill='white', outline='black')
    canvas.create_rectangle(260, 220, 280, 240, fill='white', outline='black')

# Function to create the fence
def draw_fence(canvas):
    # Fence posts
    for i in range(50, 400, 30):  # Draw posts along the bottom
        canvas.create_rectangle(i, 350, i + 10, 400, fill='saddlebrown', outline='black')

    # Fence rails
    canvas.create_line(50, 360, 380, 360, fill='saddlebrown', width=5)
    canvas.create_line(50, 380, 380, 380, fill='saddlebrown', width=5)

# Main function to set up the window and canvas
def draw_scene():
    root = tk.Tk()
    root.title("House with Fence")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    draw_house(canvas)
    draw_fence(canvas)

    root.mainloop()

# Call the main function
if __name__ == "__main__":
    draw_scene()
