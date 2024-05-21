from tkinter import *
import customtkinter

def createWindow():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk() 

    root.title("Calculator Application")
    root.iconbitmap("gui\icon.ico")
    root.geometry("320x480")
    root.resizable(width=False, height=False)

    hello = Label(root,
                  text="Hello",
                  font=('Arial',0,'bold'))
    hello.pack(pady=40)

    root.mainloop()