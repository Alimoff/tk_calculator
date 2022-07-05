from tkinter import *
from tkmacosx import Button
import tkinter.font as font

tk = Tk()

tk.title("Calculator")
tk.geometry("410x450")
tk.configure(bg="black")
tk.resizable(width=False, height=False)


e = Entry(tk, width=29, borderwidth=3, relief="ridge", font=("default", 20))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Operation functions


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_point(point):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(point))


def button_clear():
    e.delete(0, END)


def button_add():
    first_num = e.get()
    global f_numb
    global operation
    operation = "addition"
    f_numb = int(first_num)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if operation == "addition":
        e.insert(0, f_numb + int(second_number))

    if operation == "division":
        e.insert(0, f_numb / int(second_number))

    if operation == "subtraction":
        e.insert(0, f_numb - int(second_number))

    if operation == "multiplation":
        e.insert(0, f_numb * int(second_number))


def button_divide():
    first_num = e.get()
    global f_numb
    global operation
    operation = "division"
    f_numb = int(first_num)
    e.delete(0, END)


def button_subtract():
    first_num = e.get()
    global f_numb
    global operation
    operation = "subtraction"
    f_numb = int(first_num)
    e.delete(0, END)


def button_multiple():
    first_num = e.get()
    global f_numb
    global operation
    operation = "multiplation"
    f_numb = int(first_num)
    e.delete(0, END)


# Number buttons

button_1 = Button(
    tk,
    text="1",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(1),
)


button_2 = Button(
    tk,
    text="2",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(2),
)


button_3 = Button(
    tk,
    text="3",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(3),
)


button_4 = Button(
    tk,
    text="4",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(4),
)


button_5 = Button(
    tk,
    text="5",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(5),
)


button_6 = Button(
    tk,
    text="6",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(6),
)


button_7 = Button(
    tk,
    text="7",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(7),
)


button_8 = Button(
    tk,
    text="8",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(8),
)


button_9 = Button(
    tk,
    text="9",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 17 bold",
    activeforeground="black",
    command=lambda: button_click(9),
)


button_0 = Button(
    tk,
    text="0",
    padx=12,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 18 bold",
    activeforeground="black",
    command=lambda: button_click(0),
)

button_00 = Button(
    tk,
    text="00",
    padx=80,
    pady=8,
    bg="#7C7972",
    activebackground="#E29B00",
    font="sans 18 bold",
    activeforeground="black",
    command=lambda: button_click(0),
)

# Operations
btn_equal = Button(
    tk,
    text="=",
    padx=80,
    pady=8,
    bg="#E29B00",
    activebackground="#E6E5E3",
    font="sans 17 bold",
    activeforeground="black",
    command=button_equal,
)

btn_multiple = Button(
    tk,
    text="*",
    padx=12,
    pady=10,
    bg="#FFAE00",
    activebackground="#CFD1D0",
    font="sans 17 bold",
    activeforeground="black",
    command=button_multiple,
)

btn_subtract = Button(
    tk,
    text="-",
    padx=12,
    pady=10,
    bg="#FFAE00",
    activebackground="#CFD1D0",
    font="sans 17 bold",
    activeforeground="black",
    command=button_subtract,
)

btn_divide = Button(
    tk,
    text="/",
    padx=12,
    pady=10,
    bg="#FFAE00",
    activebackground="#CFD1D0",
    font="sans 17 bold",
    activeforeground="black",
    command=button_divide,
)

btn_addition = Button(
    tk,
    text="+",
    padx=12,
    pady=10,
    bg="#FFAE00",
    activebackground="#CFD1D0",
    font="sans 17 bold",
    activeforeground="black",
    command=button_add,
)

button_point = Button(
    tk,
    text=".",
    padx=12,
    pady=10,
    bg="#FFAE00",
    activebackground="#CFD1D0",
    font="sans 17 bold",
    activeforeground="black",
    # command=lambda: button_point(str(".")),
)

btn_delete = Button(
    tk,
    text="C",
    padx=80,
    pady=10,
    bg="#FFAE00",
    activebackground="#CFD1D0",
    font="sans 17 bold",
    activeforeground="black",
    command=button_clear,
)

# Showing on screen

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)


button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_0.grid(row=5, column=0)
button_00.grid(row=5, column=1, columnspan=2)


btn_multiple.grid(row=6, column=0)
btn_addition.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)


btn_subtract.grid(row=7, column=0)
btn_equal.grid(row=7, column=1, columnspan=2)

button_point.grid(row=8, column=0)
btn_delete.grid(row=8, column=1, columnspan=2)

# Last label

label = Label(
    text="Calculater by Alimoff", fg="#FFAE00", padx=140, pady=26, font="sans 12 bold"
)
label.grid(row=10, column=0, columnspan=3)

tk.mainloop()
