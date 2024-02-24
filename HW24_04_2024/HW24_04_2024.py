import random
from tkinter import *
import tkinter.messagebox

def generation():
    try:
        poch = int(ent_start.get())
        kin = int(ent_end.get())
        if poch > kin:
            tkinter.messagebox.showwarning("Зауваження", "Перше число має бути меншим за друге!")
        else:
            gen_num = random.randint(poch, kin)
            root.title(gen_num)
            but_gen['state']='disable'
            ent_start['state'] = 'disable'
            ent_end['state'] = 'disable'
    except:
        tkinter.messagebox.showerror("Помилка", "Потрібно ввести цілі числа!")


root = Tk()
w1 = root.winfo_screenwidth()
h1 = root.winfo_screenheight()
root.geometry(f"400x400+{int(w1/2-200)}+{int(h1/2-150)}")

Label(root, text='Введіть ліву межу', font=(None, 14)).place(x=20, y=40)
Label(root, text='Введіть праву межу', font=(None, 14)).place(x=20, y=80)
ent_start = Entry(root, font=(None, 14))
ent_start.place(x=200, y=40)
ent_end = Entry(root, font=(None, 14))
ent_end.place(x=200, y=80)
but_gen = Button(root, font=(None, 14), text='Генерувати', command=generation)
but_gen.place(x=150, y=120)



root.mainloop()