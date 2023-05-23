import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import random
import re
global whole_string

class Div(ZeroDivisionError):
    pass

class Alpha(ValueError):
    pass


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def clear():
    whole_string.set('0')
    entry.focus_set()
    calc_var.set("")


class Button:
    def __init__(self):
        self.color = 'pink'
        self.state = 'normal'
        self.text = random.choice(mylist)
        s = ttk.Style()
        s.configure('C.TButton', background=self.color, activebackground='lavender blush')
        self.button = ttk.Button(root, text=self.text, style='C.TButton', command=self.button_get)

    def button_get(self):
        whole_string.set(self.button['text'])
        calc_var.set(calc_var.get() + whole_string.get())


def calc(_event=None):
    get_it = calc_var.get()
    try:
        if re.search('[a-zA-Z]', get_it):
            raise Alpha
    except Alpha:
        calc_var.set("Can't use letters")
    try:
        t = ""
        if '+' in get_it:
            t = get_it.split('+')
            a = t[0]
            a = float(a)

            b = t[1]
            b = b.rstrip("=")
            b = float(b)
            isequals = calc_var.get()
            if "=" not in isequals:
                t.append("=")
            result = a + b
            result = round(result, 4)
            t.insert(1, "+")
            t.append(result)

        if "-" in get_it:
            t = get_it.split('-')
            a = t[0]
            b = t[1]
            b = b.rstrip("=")
            a = float(a)
            b = float(b)
            isequals = calc_var.get()
            if "=" not in isequals:
                t.append("=")
            result = a - b
            result = round(result, 4)
            t. insert(1, "-")
            t.append(result)

        if "*" in get_it:
            t = get_it.split('*')
            a = t[0]
            a = float(a)

            b = t[1]
            b = b.rstrip("=")
            b = float(b)
            isequals = calc_var.get()
            if "=" not in isequals:
                t.append("=")
            result = a * b
            result = round(result, 4)
            t.insert(1, "*")
            t.append(result)

        if "/" in get_it:
            t = get_it.split('/')
            a = t[0]
            a = float(a)

            b = t[1]
            b = b.rstrip("=")
            b = float(b)
            if b == 0:
                raise Div
            isequals = calc_var.get()
            if "=" not in isequals:
                t.append("=")
            result = a / b
            result = round(result, 4)
            t.insert(1, "/")
            t.append(result)

        return calc_var.set(t)
    except Div:
        calc_var.set("Can't divide by zero")
        entry.icursor(0)
    except ValueError:
        get_error = calc_var.get()
        calc_var.set("Malformed expression: " + get_error)
        entry.icursor(0)


root = tk.Tk()
root.tk.call('wm', 'iconphoto', root, PhotoImage(file='/home/cindy/Python-training/accessories-calculator.png'))
root.title("Pocket Calc ")
root.bind("=", calc)
global whole_string; whole_string = tk.StringVar()
calc_var = tk.StringVar()
entry = tk.Entry(width=39, textvariable=calc_var, bd=2, bg='white', disabledbackground='white', disabledforeground='black')
root.bind('<Return>', calc)
entry.focus_set()
entry.grid(row=0, column=0, columnspan=4)
b1 = Button()
b1.button['text'] = '+'
b1.button['style'] = 'Enter.TButton'
b1.button.grid(row=1, column=4, sticky='e', padx=3)
b2 = Button()
b2.button['text'] = '-'
b2.button['style'] = 'Enter.TButton'
b2.button.grid(row=1, column=5, sticky='e')
mult_button = Button()
mult_button.button['text'] = '*'
mult_button.button['style'] = 'Enter.TButton'
mult_button.button.grid(row=2, column=4, sticky='e', padx=3)
div_button = Button()
div_button.button['text'] = '/'
div_button.button['style'] = 'Enter.TButton'
div_button.button.grid(row=2, column=5, sticky='e')
b3 = Button()
point_button = Button()
point_button.button['text'] = '.'
point_button.button.grid(row=1, column=0)
clear_button = ttk.Button(root, text="Clear", style='C.TButton', command=clear)
clear_button.grid(row=1, column=1)
b3.button['text'] = 9
b3.button.grid(row=1, column=2)
b4 = Button()
b4.button['text'] = 8
b4.button.grid(row=2, column=0)
b5 = Button()
b5.button['text'] = 7
b5.button.grid(row=2, column=1)
b6 = Button()
b6.button['text'] = 6
b6.button.grid(row=2, column=2)
b7 = Button()
b7.button['text'] = 5
b7.button.grid(row=3, column=0)
b8 = Button()
b8.button['text'] = 4
b8.button.grid(row=3, column=1)
b9 = Button()
b9.button['text'] = 3
b9.button.grid(row=3, column=2)
b10 = Button()
b10.button['text'] = 2
b10.button.grid(row=4, column=0)
b11 = Button()
b11.button['text'] = 1
b11.button.grid(row=4, column=1)
b12 = Button()
b12.button['text'] = 0
b12.button.grid(row=4, column=2)
style = ttk.Style()
style.configure('Enter.TButton', foreground='red', background='lavender blush', borderwidth=2, relief='ridge')
style_enter = ttk.Style()
style_enter.configure('E.TButton', foreground='red', background='light green', borderwidth=2, relief='ridge')
enter = ttk.Button(root, text="=", style='E.TButton', command=calc)
enter.grid(row=3, column=4, columnspan=2)
root.mainloop()
