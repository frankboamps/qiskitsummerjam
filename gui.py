import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

TITLE = "Quantum CV"
HEIGHT = 700
WIDTH = 700
BROWSE_BUTTON_TEXT_1 = "Browse for image 1"
BROWSE_BUTTON_TEXT_2 = "Browse for image 2"

root = tk.Tk()
root.resizable(False, False)
root.title(TITLE)

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = 'blue')
canvas.pack()

title = tk.Label(canvas, text = TITLE, font = ('Helvetica', 20), anchor = 'center')
title.place(relx = .15, rely = .02, relwidth = .7, relheight = .05)

frame_1 = tk.Frame(root)
frame_1.place(relwidth=0.8, relheight=0.35, relx=0.5, rely=0.1, anchor='n')

label_1 = tk.Label(frame_1, text = "Choose Image")
label_1.place(relheight=0.1, relx=0.02)

image_entry_1 = tk.Entry(frame_1)
image_entry_1.place(relwidth = .9, relheight = .2, relx = .05, rely = .4, anchor = 'nw')
image_entry_2 = tk.Entry(frame_1)
image_entry_2.place(relwidth = .9, relheight = .2, relx = .05, rely = .4, anchor = 'sw')

browse_button_1 = tk.Button(frame_1, text = BROWSE_BUTTON_TEXT_1, command = lambda: image_file_selector(image_entry_1))
browse_button_1.place(relx = .69, rely = .1, relwidth = .25, relheight = .13, anchor = 'e')
browse_button_2 = tk.Button(frame_1, text = BROWSE_BUTTON_TEXT_2, command = lambda: image_file_selector(image_entry_2))
browse_button_2.place(relx = .69, rely = .1, relwidth = .25, relheight = .13, anchor = 'w')

def image_file_selector(entry):
    filename = filedialog.askopenfilename(initialdir="/D", title="Select Image  file",
                                          filetypes=(("JPG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")))
    set_entrybox_text(filename, entry)
    return

def set_entrybox_text(filename, entry):
    entry.delete(0, tk.END)
    entry.insert(0, filename)
    return

root.mainloop()