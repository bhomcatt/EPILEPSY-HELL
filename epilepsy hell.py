from tkinter import *
import random

root = Tk()
root.geometry("600x400")
dictionary = {'color' : ['#EBA937','#dc143c','#30D5C8','#7B3F00','#50c878','#50327c']}

def bg_change():
    random_no = random.randint(0,5)
    print(dictionary["color"][random_no])
    root.configure(background=dictionary["color"][random_no])


btn = Button(root,text="HAZ CLICK AQUI PARA GANAR 10000 DOLARES! NO ES UN VIRUS!",command=bg_change)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()