from tkinter import *
from tkinter import messagebox

root = Tk()


root.title('CPI-NEWS')
root['bg'] = '#fafafa'
root.wm_attributes('-alpha', 0.7)
root.geometry('1280x960')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=1280, width =960)
canvas.pack()

frame = Frame(root, bg='black')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text = "CPI-NEWS", bg = 'gray', font= 80)
title.pack()



root.mainloop()