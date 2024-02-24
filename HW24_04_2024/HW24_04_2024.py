import random
from tkinter import *
import tkinter.messagebox

def generation():
    try:
        poch = int(ent_start.get())
        kin = int(ent_end.get())
        if poch >= kin:
            tkinter.messagebox.showwarning("Зауваження", "Перше число має бути меншим за друге!")
        else:
            global gen_num
            gen_num = random.randint(poch, kin)
            root.title(str(gen_num))
            but_gen['state'] = 'disable'
            ent_start['state'] = 'disable'
            ent_end['state'] = 'disable'
    except:
        tkinter.messagebox.showerror("Помилка", "Потрібно ввести цілі числа!")

def chislo():
    pass
    # try:
    #     chisl = int(ent_game.get())
    #     if chisl == gen_num:


gen_num = 0

root = Tk()
w1 = root.winfo_screenwidth()
h1 = root.winfo_screenheight()
root.geometry(f"400x400+{int(w1/2-200)}+{int(h1/2-150)}")

Label(root, text='Введіть ліву межу', bg="purple", fg="black",  font=(None, 14)).place(x=20, y=40)
Label(root, text='Введіть праву межу', bg="black", fg="purple", font=(None, 14)).place(x=20, y=80)
ent_start = Entry(root, font=(None, 14))
ent_start.place(x=200, y=40)
ent_end = Entry(root, font=(None, 14))
ent_end.place(x=200, y=80)
but_gen = Button(root, font=(None, 14), text='Генерувати', bg="purple", fg="black",  command=generation)
but_gen.place(x=150, y=120)
Label(root, text='Вгадайте число', bg="black", fg="purple", font=(None, 14)).place(x=20, y=200)
ent_game = Entry(root, font=(None, 14))
ent_game.place(x=200, y=200)
but_game = Button(root, font=(None, 14), text='Вгадати', bg="purple", fg="black",  command=chislo)
but_game.place(x=140, y=235)


root.mainloop()