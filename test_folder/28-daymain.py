from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text="00:00")
    my_label_1.config(text="Timer")
    my_label_2.config(text="")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    # count_down(5*60)
    work_sec=WORK_MIN *60
    break_sec=SHORT_BREAK_MIN *60
    long_break=LONG_BREAK_MIN *60
    if reps%8==0:
        my_label_1.config(text="long break of 20mins",fg=RED)
        count_down(long_break)
    elif reps %2==0:
        my_label_1.config(text= "Short break of 5mins",fg=PINK)
        count_down(break_sec)
    else:
        my_label_1.config(text= "Am in working ⌚⌚ section",fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            marks+="✅"
        my_label_2.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("ANDREE self study timer⌚")
window.config(padx=100,pady=50,bg=YELLOW)


canva=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_imag=PhotoImage(file="tomato.png")
canva.create_image(100,112,image=tomato_imag)
timer_text=canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
canva.grid(column=1,row=1)



my_label_1=Label(text="Timer",font=(FONT_NAME,45,"bold"),fg=GREEN,bg=YELLOW)
my_label_1.grid(column=1,row=0)



my_label_2=Label(fg=GREEN,bg=YELLOW,font=("Arial", 40, "bold"))
my_label_2.grid(column=1,row=3)


start_button=Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)


reset_button=Button(text="reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)








window.mainloop()