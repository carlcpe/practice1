from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

expression = ""

def press(num):
    global expression

    expression = expression + str(num) 

    equation.set(expression)

def equalpress():
    try:
        global expression

        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

root = customtkinter.CTk() 

root.title("Calculator Application")
root.iconbitmap("icon.ico")
root.geometry("320x480")
root.resizable(width=False, height=False)


equation = StringVar()
expression_field = customtkinter.CTkEntry(master=root,
                                          width=320, height=100,
                                          corner_radius=0,
                                          state="readonly", justify="right",
                                          font=("Helvetica", 50),
                                          textvariable=equation)
expression_field.grid(columnspan=4)

button1 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="1",
                                  command=lambda: press(1))
button1.grid(row=2, column=0)

button2 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="2",
                                  command=lambda: press(2))
button2.grid(row=2, column=1)

button3 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="3",
                                  command=lambda: press(3))
button3.grid(row=2, column=2)

button4 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="4",
                                  command=lambda: press(4))
button4.grid(row=3, column=0)

button5 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="5",
                                  command=lambda: press(5))
button5.grid(row=3, column=1)

button6 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="6",
                                  command=lambda: press(6))
button6.grid(row=3, column=2)

button7 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="7",
                                  command=lambda: press(7))
button7.grid(row=4, column=0)

button8 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="8",
                                  command=lambda: press(8))
button8.grid(row=4, column=1)

button9 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="9",
                                  command=lambda: press(9))
button9.grid(row=4, column=2)

buttonC = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 25),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="Clear",
                                  command=clear)
buttonC.grid(row=5, column=0)

button0 = customtkinter.CTkButton(master=root, 
                                  fg_color=("lightgray"),
                                  text_color=("black"),
                                  font=("Helvetica", 40),
                                  corner_radius=0, border_width=1,
                                  height=96, width=80, text="0",
                                  command=lambda: press(0))
button0.grid(row=5, column=1)

buttonequals = customtkinter.CTkButton(master=root, 
                                       fg_color=("lightgray"),
                                       text_color=("black"),
                                       font=("Helvetica", 40),
                                       corner_radius=0, border_width=1,
                                       height=96, width=80, text="=",
                                       command=equalpress)
buttonequals.grid(row=5, column=2)

buttonplus = customtkinter.CTkButton(master=root, 
                                     fg_color=("orange"),
                                     text_color=("black"),
                                     font=("Helvetica", 40),
                                     corner_radius=0, border_width=1,
                                     height=96, width=80, text="+",
                                     command=lambda: press("+"))
buttonplus.grid(row=2, column=3)

buttonminus = customtkinter.CTkButton(master=root, 
                                      fg_color=("orange"),
                                      text_color=("black"),
                                      font=("Helvetica", 40),
                                      corner_radius=0, border_width=1,
                                      height=96, width=80, text="-",
                                      command=lambda: press("-"))
buttonminus.grid(row=3, column=3)

buttonmultiply = customtkinter.CTkButton(master=root, 
                                         fg_color=("orange"),
                                         text_color=("black"),
                                         font=("Helvetica", 40),
                                         corner_radius=0, border_width=1,
                                         height=96, width=80, text="*",
                                         command=lambda: press("*"))
buttonmultiply.grid(row=4, column=3)

buttondivide = customtkinter.CTkButton(master=root, 
                                       fg_color=("orange"),
                                       text_color=("black"),
                                       font=("Helvetica", 40),
                                       corner_radius=0, border_width=1,
                                       height=96, width=80, text="/",
                                       command=lambda: press("/"))
buttondivide.grid(row=5, column=3)

root.mainloop()