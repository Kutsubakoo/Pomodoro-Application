from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_RED = "#FF858D"
MINT = "#68B684"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TEA_GREEN = "#C2F8CB"
CELADON = "#B3E9C7"
AMETHYST = "#8367C7"
CHRYSLER_BLUE = "#5603AD"
CHECK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Pomodoro Timer")
    check_mark.config(text="")

    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(fg=MINT, text="work work work!")
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(fg=LIGHT_RED, text="You've earned yourself a long break ^_^")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(fg=CHRYSLER_BLUE, text="Take a short break :--)")
    elif reps > 8:
        reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=70, bg=AMETHYST)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

timer_label = Label(text="Pomodoro Timer", font=(FONT_NAME, 25, "bold"), fg=CELADON, bg=AMETHYST)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=AMETHYST, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

check_mark = Label(fg=CELADON, bg=AMETHYST)
check_mark.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()

