import customtkinter as ctk
from customtkinter import *
from tkinter import *
import random

root = ctk.CTk()
root.geometry("400x400")
root.title("Password Case Study")

box = ctk.CTkTextbox(root, height=50)
lbl0 = ctk.CTkLabel(root, text="")
lbl = ctk.CTkLabel(root, text="")

charlist = [[[0,1,2,3,4,5,6,7,8,9],["Hello", "Goodbye", "HappyCoding", "Hola", "FilthyRich", "Antagonist", "Protagonist"],["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]]

def password():
    r1 = random.randint(0,9)
    r2 = random.randint(0,6)
    r3 = random.randint(0,25)
    
    p1 = str(charlist[0][0][r1])
    p2 = str(charlist[0][1][r2])
    p3 = str(charlist[0][2][r3])
    
    conch = "You can try this unique password: "+p1+p2+p3+"."
    
    lbl.configure(text=conch)
    
    txt = "Your guess: " + str(box.get("0.0", "end"))
    
    lbl0.configure(text=txt)
    
btn = CTkButton(root, text="New Password", command=password)

box.place(relx=0.5, rely=0.33, anchor=CENTER)
lbl0.place(relx=0.5, rely=0.475, anchor=CENTER)
btn.place(relx=0.5, rely=0.55, anchor=CENTER)
lbl.place(relx=0.5, rely=0.66, anchor=CENTER)

root.mainloop()