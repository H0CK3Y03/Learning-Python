from tkinter import *
import random, string


window = Tk()
canvas = Canvas(window, width=500, height=500)
canvas.pack()

letters = string.ascii_letters
vowels = "aeiouAEIOU"
consonants = ''.join(set(letters).difference(set(vowels)))

start = random.choice(letters)
word = start
count = None

if start in vowels:

    count = 0

if start in consonants:

    count = 1

for i in range(random.randint(2, 20)):

    if count == 0:

        count += 1

        word += random.choice(consonants)

    elif count == 1:

        count -= 1

        word += random.choice(vowels)

print(word)

text = canvas.create_text(250, 250, text=word, font=("Courier", 20))

window.mainloop()
