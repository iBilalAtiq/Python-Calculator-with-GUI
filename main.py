from tkinter import *

root = Tk()
root.title("Calculator")

txt_input = Entry(root, width=45, borderwidth=10)
txt_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def click(num):
    current_num = txt_input.get()
    txt_input.delete(0, END)
    txt_input.insert(0, str(current_num) + str(num))


def clear():
    txt_input.delete(0, END)


def add():
    f_num = txt_input.get()
    global rem_num
    global calc
    calc = "addition"
    rem_num = f_num
    txt_input.delete(0, END)


def equal():

        sec_num = txt_input.get()
        txt_input.delete(0, END)
        if calc == "addition":
            txt_input.insert(0, int(rem_num) + int(sec_num))
        elif calc == "Subtraction":
            txt_input.insert(0, int(sub_rem) - int(sec_num))
        elif calc == "multiply":
            txt_input.insert(0, int(mul_rem) * int(sec_num))
        elif calc == "divide":
            txt_input.insert(0, int(div_rem) / int(sec_num))

def sub():
    f_num = txt_input.get()
    global sub_rem
    global calc
    calc = "Subtraction"
    sub_rem = f_num
    txt_input.delete(0, END)


def mul():
    f_num = txt_input.get()
    global mul_rem
    global calc
    calc = "multiply"
    mul_rem = f_num
    txt_input.delete(0, END)


def divide():
    f_num = txt_input.get()
    global div_rem
    global calc
    calc = "divide"
    div_rem = f_num
    txt_input.delete(0, END)


btn_1 = Button(root, text="1", padx=30, pady=20, command=lambda: click(1))
btn_2 = Button(root, text="2", padx=30, pady=20, command=lambda: click(2))
btn_3 = Button(root, text="3", padx=30, pady=20, command=lambda: click(3))
btn_4 = Button(root, text="4", padx=30, pady=20, command=lambda: click(4))
btn_5 = Button(root, text="5", padx=30, pady=20, command=lambda: click(5))
btn_6 = Button(root, text="6", padx=30, pady=20, command=lambda: click(6))
btn_7 = Button(root, text="7", padx=30, pady=20, command=lambda: click(7))
btn_8 = Button(root, text="8", padx=30, pady=20, command=lambda: click(8))
btn_9 = Button(root, text="9", padx=30, pady=20, command=lambda: click(9))
btn_0 = Button(root, text="0", padx=30, pady=20, command=lambda: click(0))
btn_add = Button(root, text="+", padx=30, pady=20, command=add)
btn_sub = Button(root, text="-", padx=30, pady=20, command=sub)
btn_mul = Button(root, text="x", padx=30, pady=20, command=mul)
btn_div = Button(root, text="/", padx=30, pady=20, command=divide)
btn_equal = Button(root, text="=", padx=80, pady=20, command=equal)
btn_clear = Button(root, text="Clear", padx=70, pady=20, command=clear)

# Buttons on screen

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=1)
btn_clear.grid(row=5, column=1, columnspan=2)

btn_add.grid(row=4, column=0)
btn_equal.grid(row=6, column=1, columnspan=2)

btn_sub.grid(row=4, column=2)
btn_mul.grid(row=5, column=0)
btn_div.grid(row=6, column=0)

root.mainloop()
