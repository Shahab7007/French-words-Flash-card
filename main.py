from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
timer = NONE

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def know_the_card():
    if current_card:
        to_learn.remove(current_card)
        print(len(to_learn))
        words = pandas.DataFrame(to_learn)
        words.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global timer, current_card
    window.after_cancel(timer)
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text, text="French", fill="Black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="Black")
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="White")
    canvas.itemconfig(word_text, text=current_card["English"], fill="White")

# -------------------------------------------UI SETUP-------------------------------------------------- #


window = Tk()
window.title("Flashcard")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="Title", fill="Black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="Black", font=("Arial", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

r_button_image = PhotoImage(file="images/right.png")

r_button = Button(image=r_button_image, highlightthickness=0, command=know_the_card)
r_button.grid(column=0, row=1)

w_button_image = PhotoImage(file="images/wrong.png")

w_button = Button(image=w_button_image, highlightthickness=0, command=next_card)
w_button.grid(column=1, row=1)

window.mainloop()
