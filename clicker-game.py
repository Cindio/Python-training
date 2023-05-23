#!/usr/bin/env python3
import sys
import os
import random
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

global text


def refresh():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def about():
    messagebox.showinfo('About',
                        "Click on the smallest number until you've grayed out all 25 numbers.\n Visual clue: Buttons with fewer digits are smaller!")


def disable(name):
    if name['text'] == button_list[0]:
        name.flash()
        name.config(state=tk.DISABLED, bg='white', cursor='heart')
        button_list.pop(0)


def bclicks():
    global b_clicks
    b_clicks += 1
    clicked.set(b_clicks)


def timer_count():
    global timer_counter
    text.set(timer_counter)
    timer_counter += 1
    tk.after_id = timer.after(1000, timer_count)
    if len(button_list) == 0:
        timer.after_cancel(tk.after_id)


root = tk.Tk()
# Specify Grid
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

root['bg'] = 'cornsilk'
root.title("Clicker Game")
root.tk.call('wm', 'iconphoto', root, PhotoImage(file='./numbers.png'))
menubar = tk.Menu(root, bg='black', fg='white')

about_menu = tk.Menu(menubar, tearoff=0, bg='cornsilk', activebackground='white')
about_menu.add_command(
    label='About',
    command=about
)
about_menu.add_separator()
about_menu.add_command(
    label='Exit',
    command=root.destroy
)
menubar.add_cascade(
    label="About",
    menu=about_menu,
    underline=0
)

root.config(menu=menubar)
frame = tk.Frame(root, bg='cornsilk')
frame.grid(row=0, column=0, padx=2, pady=1, ipadx=2, ipady=2, columnspan=3, rowspan=5, sticky='nsew')
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)
frame.rowconfigure(5, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
timer_counter = 0
counter = 0
grid_row = 0
button_list = []

while counter < 5:
    grid_col = 0
    for x in range(5):
        name = random.randint(1, 25)
        name = tk.Button(frame, text=random.randint(1, 999), bg='cornsilk', activebackground='red',
                         cursor='question_arrow')
        name["command"] = lambda name=name: [disable(name), bclicks()]  # this binding worked!
        name.grid(column=grid_col, row=grid_row, sticky='nsew')
        grid_col += 1
        button_list.append(name['text'])

    grid_row += 1
    counter += 1
    button_list.sort()

bottom_frame = tk.Frame(root, bg='cornsilk')
bottom_frame.grid(row=6, ipadx=2)
timer_label = tk.Label(bottom_frame, text="Timer", bg='cornsilk')
timer_label.grid(column=1, columnspan=2, row=6, sticky='w')
text = tk.IntVar()
timer = tk.Label(bottom_frame, textvariable=text, width=3, bg='black', foreground='white')
timer.grid(row=6, column=2, sticky='e')
clicks_label = tk.Label(bottom_frame, text="# Clicks", bg='cornsilk')
clicks_label.grid(column=1, columnspan=2, row=7, sticky='w')
clicked = tk.IntVar()
clicks = tk.Label(bottom_frame, textvariable=clicked, bg='black', foreground='white', width=3)
clicks.grid(column=2, row=7, sticky='e')
clicks.grid_columnconfigure(1, weight=1)
start_button = tk.Button(bottom_frame, text="Start over", bg='cornsilk', command=refresh)
start_button.grid(columnspan=2, column=1, row=8, sticky='e')
text.set(timer_counter)
b_clicks = 0

timer.after(1000, timer_count)
root.mainloop()
