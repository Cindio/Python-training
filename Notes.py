import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
import shelve
from datetime import datetime


def save_tooltip():
    save_it = "SAVE: " + str(text_box.get('1.0', 'end'))
    return save_it


def save_note():
    save_text = text_box.get('1.0', 'end-1c')
    my_shelve = shelve.open('/home/cindy/Python-training/notes_shelve.shlv', flag='c')
    note_date = datetime.today()
    note_date = str(note_date.strftime('%Y/%m/%d'))
    my_shelve[note_date] = {save_text}
    my_shelve.close()


def get_notes():
    new_shelve = shelve.open('/home/cindy/Python-training/notes_shelve.shlv')
    set_text = list(new_shelve.items())

    def mysort(e):
        return e[0]

    set_text = sorted(set_text, key=mysort, reverse=True)
    for item in set_text:
        item = str(item) + '\n'
        text_box.insert('end', item)
    new_shelve.close()


def delete_key():
    selected = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
    new_shelve = shelve.open('/home/cindy/Python-training/notes_shelve.shlv')
    new_shelve.pop(selected)
    text_box.delete(selected)
    new_shelve.close()


def clear_box():
    text_box.delete('1.0', 'end')


def insert_emoji(selected):
    positions = (0.0, 0.5666666666666667)
    print(emoji_menu.yview())
    if emoji_menu.yview() == positions:
        text_box.image_create(text_box.index('insert'), image=aok)
    else:
        text_box.image_create(text_box.index('insert'), image=thumbs_down)



root = tk.Tk()
root.configure(background="pink")
root.title("NOTES")
#root.bind('<Button-1>', insert_emoji)
style = ttk.Style(root)
style.configure("TFrame", background="pink", highlightcolor="black", highlightbackground="black")
button_frame = ttk.Frame(root, width=100, height=40)
button_frame.grid(row=0, columnspan=4)
clear_button = ttk.Button(button_frame, text="Clear", command=clear_box)
clear_button.grid(row=1, column=1, columnspan=1, sticky='w')
save_icon = tk.PhotoImage(file="/home/cindy/Pictures/icon-save.png")
save = tk.Button(button_frame, image=save_icon, bd=2, command=save_note)
save.grid(row=1, column=2, columnspan=1, sticky='w')
ToolTip(save, msg=save_tooltip, bg="white")
get = tk.PhotoImage(file='/home/cindy/Pictures/icon-fetch.png')
get_saved = tk.Button(button_frame, image=get, bd=2, command=get_notes)
get_saved.grid(row=1, column=3, columnspan=1, sticky='w')
ToolTip(get_saved, msg='Get', bg="white")
x = tk.PhotoImage(file="/home/cindy/Pictures/icon-x.png")
delete = tk.Button(button_frame, image=x, bd=2, command=delete_key)
delete.grid(row=1, column=4, columnspan=1, sticky='w')
ToolTip(delete, msg="Delete", bg="white")

emoji_listbox = tk.Listbox(
    button_frame,
    height=1,
    selectmode=tk.BROWSE
)

scrollbar = tk.Scrollbar(orient='horizontal')
text_box = tk.Text(root, width=100, height=50, takefocus=1, wrap='word')
text_box.grid(row=2, columnspan=4)
scrollbar.grid(row=3)
text_box.focus_set()
thumbs_down = tk.PhotoImage(name= "thumbs_down", file="/home/cindy/Python-training/thumbsDownSmall.png")
aok = tk.PhotoImage(name="aok", file="/home/cindy/Python-training/aokSmall.png")
emoji_frame = tk.Frame(button_frame, width=10, height=4)
emoji_frame.grid(row=1, column=5, columnspan=3)
emoji_menu = tk.Text(emoji_frame, yscrollcommand=scrollbar.set, height=2, width=5, cursor="hand2")
emoji_menu.bind('<Button-1>', insert_emoji)
scrollbar = ttk.Scrollbar(emoji_frame, orient='vertical', command=emoji_menu.yview)
emoji_menu.grid(row=1, column=5)
scrollbar.grid(row=1, column=6)
aokTexted = emoji_menu.image_create(emoji_menu.index('1.0'), image=aok)
thumbs_downTexted = emoji_menu.image_create(emoji_menu.index('2.0'), image=thumbs_down)
root.mainloop()
