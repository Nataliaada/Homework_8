from tkinter import*


def calculation():
    result['text'] = f'{name.get()} {sourname.get()} {secname.get()} {data.get()} '
    result.pack()
    return result


root = Tk()
root.title('База данных учеников')
root.geometry('500x510')
root.resizable(width=False, height=False)
root['bg']='black'

Label(root, text ='Введите фамилию ученика:', font='Arial 15 bold', fg='lime', bg='black').pack(pady=5)

name = Entry(root,font='Arial 15 bold')
name.pack(pady=5)

Label(root, text ='Введите имя ученика:', font='Arial 15 bold', fg='lime', bg='black').pack(pady=5)

sourname = Entry(root,font='Arial 15 bold')
sourname.pack(pady=5)

Label(root, text ='Введите отчество ученика:', font='Arial 15 bold', fg='lime', bg='black').pack(pady=5)

secname = Entry(root,font='Arial 15 bold')
secname.pack(pady=5)

Label(root, text ='Введите дату рождения д/м/г:', font='Arial 15 bold', fg='lime', bg='black').pack(pady=5)

data = Entry(root,font='Arial 15 bold')
data.pack(pady=5)


btn = Button(root, text ='НАЙТИ', font='Arial 15 bold', command=calculation)
btn.pack(pady=5)

result = Label(root, font='Arial 15 bold', fg='lime', bg='black')


root.mainloop()