#!usr/bin/env
from tkinter import *
import tkinter as tk
import login
import register

def window():
    #initialize window
    window = tk.Tk()
    window.title('CCBank')
    width  = int(window.winfo_screenwidth()/2)
    height = int(window.winfo_screenheight()/2)
    window.geometry(f'{width}x{height}')

    #create buttons
    loginButton = tk.Button(window, text ='Login', command = login.loginButton())
    registerButton = tk.Button(window, text ='Register', command = register.registerButton())

    loginButton.place(relx=0.5, rely=0.6, anchor=CENTER)
    registerButton.place(relx=0.5, rely=0.7, anchor=CENTER)

    

    #keep the window opened
    window.mainloop()

def main():
    window()

if __name__ == "__main__":
    main()
