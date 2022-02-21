import random 
from tkinter import *

 
# Creating gui with name and dimensions 
root = Tk()
root.title('Simple Password Creator ! ')
root.iconbitmap()
root.geometry('500x500')

# Letters and numbers/symbols to be pulled when creating a password
alpha = 'abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_-+='

characters = alpha + numbers + symbols

label_characters = Label(root, text="Number of characters", font =('Arial',12)).pack(padx=10)

character_length = Entry(root, font=("Arial 14"))
character_length.pack(padx=10)

def generate_password():
    length = character_length.get()
    password = "".join(random.sample(characters,int(length)))
    label_password.config(text="Created Password:" + password)

# Creating button for GUI
Button(root, text="Create Password",command=generate_password, font=("Arial",12)).pack(padx=10)
label_password = Label(root, font=("Arial",12))
label_password.pack()

root.mainloop()