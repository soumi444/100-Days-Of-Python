from tkinter import *
import math

root = Tk()
root.title("Simple GUI Calculator")

e = Entry(root, width=25,borderwidth=5,justify = RIGHT)
e.grid(row=0, column=0, columnspan=5)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def all_clear():
    e.delete(0,END)

def clear():
    length = len(e.get())
    e.delete(length-1,END)

def add():
    first_number = e.get()
    global f_num
    global math
    math="addition"
    f_num=float(first_number)
    e.delete(0,END)

def subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num=float(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def squareroot():
    first_number = e.get()
    global f_num
    global math
    math = "squareroot"
    f_num = float(first_number)
    e.delete(0, END)

def remainder():
    first_number = e.get()
    global f_num
    global math
    math = "remainder"
    f_num = float(first_number)
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0,f_num+float(second_number))

    if math=="subtraction":
        e.insert(0,f_num-float(second_number))

    if math=="multiplication":
        e.insert(0,f_num*float(second_number))

    if math=="division":
        e.insert(0,f_num/float(second_number))

    if math=="squareroot":
        e.insert(math.sqrt(float(second_number)))

    if math=="remainder":
        e.insert(0,f_num%float(second_number))

button_1 = Button(root, text="1",padx=10, pady=10,command=lambda: button_click(1)).grid(row= 4, column= 0)
button_2 = Button(root, text="2",padx=10, pady=10,command=lambda: button_click(2)).grid(row= 4, column= 1)
button_3 = Button(root, text="3",padx=10, pady=10, command=lambda: button_click(3)).grid(row=4, column= 2)
button_minus = Button(root, text="-",padx=10, pady=10, command=subtract).grid(row= 4, column=3)

button_4 = Button(root, text="4",padx=10, pady=10, command=lambda: button_click(4)).grid(row=3 , column= 0)
button_5 = Button(root, text="5",padx=10, pady=10, command=lambda: button_click(5)).grid(row= 3, column=1)
button_6 = Button(root, text="6",padx=10, pady=10, command=lambda: button_click(6)).grid(row= 3, column=2)
button_multiplication = Button(root, text="*",padx=10, pady=10, command=multiply).grid(row=3 , column=3 )

button_7 = Button(root, text="7",padx=10, pady=10, command=lambda: button_click(7)).grid(row= 2, column=0)
button_8 = Button(root, text="8",padx=10, pady=10, command=lambda: button_click(8)).grid(row= 2, column= 1)
button_9 = Button(root, text="9",padx=10, pady=10, command=lambda: button_click(9)).grid(row= 2, column= 2)
button_divide = Button(root, text="/",padx=10, pady=10, command=divide).grid(row= 2, column=3)

button_ac = Button(root, text="AC",padx=10, pady=10, command=all_clear).grid(row= 1, column=0 )
button_c = Button(root, text="C",padx=10, pady=10, command=clear).grid(row= 1, column= 1)
button_root = Button(root, text="√",padx=10, pady=10, command=squareroot).grid(row= 1, column= 2)
button_remainder = Button(root, text="%",padx=10, pady=10, command=remainder).grid(row= 1, column=3 )

button_0 = Button(root, text="0",padx=30, pady=10, command=lambda: button_click(0) ).grid(row= 5, column=0, columnspan=2)
button_decimal = Button(root, text=".",padx=10, pady=10, command=lambda: button_click(".")).grid(row= 5, column= 2)
button_add = Button(root, text="+",padx=10, pady=10,command= add ).grid(row= 5, column= 3)


button_equal = Button(root,text="=",padx=10, pady=100, command=equal).grid(column=4, row=1, rowspan=5)


root.mainloop()