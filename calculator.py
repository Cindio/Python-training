import tkinter as tk
from tkinter import messagebox
import re


def evaluate():
    try:

        string1 = field1.get()
        string2 = field2.get()
        global get_var
        get_var = var.get()
        if string1.isdigit() or "." in string1 and string2.isdigit() or "." in string2:
            if get_var == 1:
                answer = float(string1) * float(string2)
                text.set(answer)
            elif get_var == 3:
                answer = float(string1) + float(string2)
                text.set(answer)
            elif get_var == 2:
                answer = float(string1) - float(string2)
                text.set(answer)
            elif get_var == 4:
                answer = float(string1) / float(string2)
                text.set(answer)
        else:
            messagebox.showerror("", "invalid entry")
            if re.search('[a-zA-Z]', string1):
                field1.focus_set()
            if re.search('[a-zA-Z]', string2):
                field2.focus_set()
    except ZeroDivisionError:
        messagebox.showwarning("!", "Cannot divide by zero")


root = tk.Tk()
root.geometry("225x180")
root.title("Calculator")
root['bg'] = 'white'


field1 = tk.Entry(root, width=8)

field1.grid(column=1, row=0)
field2 = tk.Entry(root, width=9)
field2.grid(column=3, row=0)
var = tk.IntVar()
mult = tk.Radiobutton(root, bg='white', text=" * ", variable=var, value=1, command=evaluate)
mult.grid(column=2, row=0)
sub = tk.Radiobutton(root, bg='white', text=" - ", variable=var, value=2, command=evaluate)
sub.grid(column=2, row=2)
add = tk.Radiobutton(root, text="+", bg='white', variable=var, value=3, command=evaluate)
add.grid(column=2, row=3)
div = tk.Radiobutton(root, text=" / ", variable=var, bg='white', value=4, command=evaluate)
div.grid(column=2, row=4)
text = tk.StringVar()
entry = tk.Entry(root, width=9, textvariable=text)
entry.grid(column=2, row=5)
root.mainloop()
