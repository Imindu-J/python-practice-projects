from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20, pady=20)
        self.window['bg']= THEME_COLOR

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.score_lbl = Label(text='Score: 0', background=THEME_COLOR, fg='white', font=('Arial', 16))
        self.score_lbl.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,bg = 'white')
        self.q_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='Some question',
            fill=THEME_COLOR, font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan = 2, pady=50)

        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.clicked_true)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.clicked_false)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        try:
            new_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=new_text)
        except IndexError:
            self.canvas.itemconfig(self.q_text, text='You have completed the quiz')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
        self.canvas.config(bg='white')


    def clicked_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)


    def clicked_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_lbl.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

