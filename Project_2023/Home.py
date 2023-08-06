import mysql.connector as con
from acc_creation import *
from Login import *
import tkinter as tk

def Start():

    # Tkinter Window

    HOME = tk.Tk()
    HOME.title("Home Screen")
    HOME.state('zoomed')
    HOME.config(bg='#12aaaa')

    # Colours

    bbgc='black'
    bfgc='white'

    # Functions

    def exit_home():
        create_account()
        HOME.destroy()

    # Menu Buttons

    home = tk.Label(HOME, text = 'Welcome' ,font = ('Arial' , 75) , bg='#12aaaa' , fg='black')
    home.place(x=450,y=100)

    Login = tk.Button(HOME, text = 'Login' ,command=create_login ,  font = ('Arial',35) , bg = 'orange' , fg = 'black')
    Login.place(x=600,y=500)

    acc = tk.Label(HOME , text = "Don't have an account ??" , font=('Arial', 18) , bg = '#12aaaa' , fg='green' )
    acc.place(x=430,y=640)

    create_acc = tk.Button(HOME, text='Create Account',command=exit_home , font=('Arial', 19) , bg='yellow' , fg='black')
    create_acc.place(x=550, y=680)


    HOME.mainloop()

    
Start()