from tkinter import *
import time

def watch():
  curr_time=time.strftime('%H:%M:%S')
  lbl.config(text = curr_time)
  lbl.after(1000,watch)

root = Tk()
lbl = Label(root, font=('Georgia pro',35,'bold italic underline'),background='black', foreground='crimson')
lbl.pack(anchor='center')

watch()
root.mainloop()