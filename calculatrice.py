from tkinter import *
from math import *

def calculer():
    chaine.configure(text="Résultat = "+ str(eval(entre.get())))
window = Tk()
entre = Entry(window)
entre.bind("<Return>",calculer)
chaine = Label(window)
chaine.pack()
entre.pack()
window.mainloop()