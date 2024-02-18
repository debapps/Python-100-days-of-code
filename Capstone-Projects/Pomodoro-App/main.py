# The Pomodoro Technique is explained in following article: 
# https://todoist.com/productivity-methods/pomodoro-technique

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text='00:00')
    heading.config(text='Timer', fg=GREEN)
    global checks, reps
    checks = ''
    reps = 0
    check_mark.config(text=checks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # Set the repetation.
    global reps
    reps += 1

    # Count the seconds.
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is 1st/3rd/5th/7th reps. Work.
    if reps % 2 != 0:
        heading.config(text='Work', fg=GREEN)
        count_down(work_sec)
    
    # If it is 2nd/4th reps. Short Break.
    if reps % 2 == 0 and reps % 8 != 0:
        heading.config(text='Break', fg=PINK)
        count_down(short_break_sec)
   
    # If it ts 8th reps. Long Break.
    if reps % 8 == 0:
        heading.config(text='Break', fg=RED)
        count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count_sec):
    global checks
    # Format the display in minites and seconds.
    min = count_sec // 60
    sec = count_sec % 60

    if sec < 10: 
        sec = f'0{sec}'

    if min < 10:
        min = f'0{min}'

    # Display the time count down on canvas
    canvas.itemconfig(text_timer, text=f'{min}:{sec}')

    # Windows sleep for 1 sec.
    if count_sec > 0:
        global timer
        timer = window.after(1000, count_down, count_sec - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += '✔'
            check_mark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
# Setting the window.
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# Setting the canvas for image and text.
tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(window, width=200, height=224, highlightthickness=0, bg=YELLOW)
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')

# Setting up the heading label.
heading = Label(window, text='Timer', font=(FONT_NAME, 45), bg=YELLOW, fg=GREEN)

# Setting up buttons.
start_btn = Button(window, text='Start', font=(FONT_NAME, 14), command=start_timer)
reset_btn = Button(window, text='Reset', font=(FONT_NAME, 14), command=reset_timer)

# Setting up check mark.
check_mark = Label(window, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))

# Geometry Manager: Setting up Layout
heading.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
check_mark.grid(column=1, row=3)

window.mainloop()