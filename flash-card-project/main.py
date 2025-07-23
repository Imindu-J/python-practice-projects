from operator import index
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
selected_word = {}
to_learn = {}

try:
    words_df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_df = pd.read_csv('data/french_words.csv')
    to_learn = original_df.to_dict(orient='records')
else:
    to_learn = words_df.to_dict(orient='records')
print(to_learn, len(to_learn))

#--------------change word--------------#

def is_known():
    try:
        to_learn.remove(selected_word)
        print(len(to_learn))
        data = pd.DataFrame(to_learn)
        data.to_csv('data/Words_to_learn.csv', index=False)
        next_word()
    except ValueError:
        next_word()

def next_word():
    selected_word.clear()
    selected_word.update(random.choice(to_learn))
    print(selected_word)
    french(selected_word['French'])
    window.after(1500, english, selected_word["English"])


def french(f_word):
    canvas.itemconfig(word_txt, text = f_word, fill='black')
    canvas.itemconfig(lang_txt, text='French', fill='black')
    canvas.itemconfig(canvas_img, image=front_img)

def english(e_word):
    canvas.itemconfig(word_txt, text=e_word, fill='white')
    canvas.itemconfig(lang_txt, text='English', fill='white')
    canvas.itemconfig(canvas_img, image=back_img)

#--------------GUI--------------#
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
wrong_img = PhotoImage(file='images/wrong.png')
right_img = PhotoImage(file='images/right.png')

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(400,263,image=front_img)
lang_txt = canvas.create_text(400, 150, text='French', font=('Ariel',40,'italic'))
word_txt = canvas.create_text(400, 263, text='Word', font=('Ariel',60,'bold'))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

window.mainloop()