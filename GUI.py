from tkinter import *

root = Tk()


def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str= f'Данные: {str(login)}, {str(password)}'
    messagebox.showinfo(title='Название', message = '')


    #окно с ошибкой
    #messagebox.showerror(title='', message='Ошибка')


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
btn= Button(frame, text = 'Пробная кнопка', bg = 'green', command=btn_click)
btn.pack()



loginInput = Entry(frame, bg ="black")
loginInput.pack()

passField = Entry(frame, bg = "black", show='*')
passField.pack()



root.mainloop()