from tkinter import *
from tkmacosx import Button
import tkinter.font as font

tk = Tk()

tk.geometry("600x500")

# font_btn = font.Font(size=30,)

btn1 = Button(
    tk,
    bg="orange",
    fg="black",
    activebackground="black",
    activeforeground="white",
    text="Button1",
    font="sans 30 bold",
)
btn1.configure(height=50, width=120)
# btn.pack()

btn1.grid(row=0, column=1)


btn2 = Button(
    tk,
    bg="orange",
    fg="black",
    activebackground="black",
    activeforeground="white",
    text="Button2",
    font="sans 30 bold",
)
btn2.configure(height=50, width=120)
# btn.pack()

btn2.grid(row=1, column=1)

tk.mainloop()
