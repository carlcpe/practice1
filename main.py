from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def button_function():
    print("Button Pressed.")

root = customtkinter.CTk() 

root.title("Calculator Application")
root.iconbitmap("icon.ico")
root.geometry("320x480")
root.resizable(width=False, height=False)


equation = StringVar()
expression_field = customtkinter.CTkEntry(master=root,
                                          width=320,
                                          height=100,
                                          corner_radius=0,
                                          font=("Helvetica", 25))
expression_field.grid(columnspan=4)

button1 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="1",
                                  command=button_function)
button1.grid(row=2, column=0)

button2 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="2",
                                  command=button_function)
button2.grid(row=2, column=1)

button3 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="3",
                                  command=button_function)
button3.grid(row=2, column=2)

button4 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="4",
                                  command=button_function)
button4.grid(row=3, column=0)

button5 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="5",
                                  command=button_function)
button5.grid(row=3, column=1)

button6 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="6",
                                  command=button_function)
button6.grid(row=3, column=2)

button7 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="7",
                                  command=button_function)
button7.grid(row=4, column=0)

button8 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="8",
                                  command=button_function)
button8.grid(row=4, column=1)

button9 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="9",
                                  command=button_function)
button9.grid(row=4, column=2)

buttonclear = customtkinter.CTkButton(master=root, 
                                      fg_color=("black", "lightgray"),
                                      text_color=("white","black"),
                                      font=("Helvetica", 25),
                                      corner_radius=0, border_width=1,
                                      height=96, width=80, text="Clear",
                                      command=button_function)
buttonclear.grid(row=5, column=0)

button0 = customtkinter.CTkButton(master=root, 
                                  fg_color=("black", "lightgray"),
                                  text_color=("white","black"),
                                  font=("Helvetica", 50),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="0",
                                  command=button_function)
button0.grid(row=5, column=1)

buttonequals = customtkinter.CTkButton(master=root, 
                                       fg_color=("black", "lightgray"),
                                       text_color=("white","black"),
                                       font=("Helvetica", 50),
                                       corner_radius=0, border_width=1,
                                       height=96, width=80, text="=",
                                       command=button_function)
buttonequals.grid(row=5, column=2)

buttonplus = customtkinter.CTkButton(master=root, 
                                     fg_color=("black", "orange"),
                                     text_color=("white","black"),
                                     font=("Helvetica", 50),
                                     corner_radius=0, border_width=1,
                                     height=96, width=80, text="+",
                                     command=button_function)
buttonplus.grid(row=2, column=3)

buttonminus = customtkinter.CTkButton(master=root, 
                                      fg_color=("black", "orange"),
                                      text_color=("white","black"),
                                      font=("Helvetica", 50),
                                      corner_radius=0, border_width=1,
                                      height=96, width=80, text="-",
                                      command=button_function)
buttonminus.grid(row=3, column=3)

buttonmultiply = customtkinter.CTkButton(master=root, 
                                         fg_color=("black", "orange"),
                                         text_color=("white","black"),
                                         font=("Helvetica", 50),
                                         corner_radius=0, border_width=1,
                                         height=96, width=80, text="*",
                                         command=button_function)
buttonmultiply.grid(row=4, column=3)

buttondivide = customtkinter.CTkButton(master=root, 
                                       fg_color=("black", "orange"),
                                       text_color=("white","black"),
                                       font=("Helvetica", 50),
                                       corner_radius=0, border_width=1,
                                       height=96, width=80, text="/",
                                       command=button_function)
buttondivide.grid(row=5, column=3)

root.mainloop()