from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timerLbl.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    checkLbl.config(text = '')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    print(reps)
    reps += 1
    if reps > 8:
        timerLbl.config(text='Timer', fg=GREEN)
        return
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timerLbl.config(text='Long break', fg=PINK)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timerLbl.config(text='Work', fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timerLbl.config(text='Break', fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = f'{count // 60:02}'
    count_sec = f'{count % 60:02}'
    # count_sec = str(count % 60)
    # if len(count_sec) < 2:
    #     count_sec = f'0{count_sec}'
    time  = count_min + ':' + count_sec
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        timer = window.after(5, count_down, count-1)
    else:
        start_timer()
        work_sessions = reps // 2
        checkLbl.config(text='✔' * work_sessions)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

resetBtn = Button(text='Reset', command=reset_timer, bg=YELLOW)
resetBtn.grid(column=2, row=2)

startBtn = Button(text='Start', command=start_timer, bg=YELLOW)
startBtn.grid(column=0, row=2)

timerLbl = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME,38))
timerLbl.grid(column=1, row=0)

checkLbl = Label(bg=YELLOW, fg=GREEN)
checkLbl.grid(column=1, row=3)


window.mainloop()