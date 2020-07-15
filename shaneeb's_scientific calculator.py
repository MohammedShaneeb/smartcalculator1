from gtts import gTTS
import os
import math
from length_converter import *
from weigth_converter import *
from volume_converter import *
from temperature_converter import *
import webbrowser
import tkinter.messagebox


#for root Window
window = Tk()
window.title("SMART CALCULATOR ")
window.configure(bg='#1b1c1b')
window.resizable(width=False, height=False)
window.geometry('398x350+0+0')

calc = Frame(window, bg='#1b1c1b')
calc.grid()
# ======================Screen=======================
screen = Entry(calc, bd=5, width=48)
screen.grid(row=0, column=0, columnspan=4)


# ==========functios  for operations===========
#this function for taking number from the client
def button_clicked(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))

#for replace '÷' this with '/' this
#and 'x' this with '*' this
#this will help to evaluate the numbers
def replace():
    global newtext
    expression = screen.get()
    newtext = expression.replace('÷', '/')
    newtext= newtext.replace('x', '*')

#this function for valuate the numbers
def eval1():
    replace()
    global eval2
    eval2 = eval(newtext)
    screen.delete(0, END)
    screen.insert(0, eval2)
    speach(eval2)

#internet is required for working this functions
#this function will convert our answer to speach(gTTs=google text to speach)
def speach(result):
    num1 = str(result)
    tts = gTTS("Your answer is" +num1 )
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")


#this will clear our all numbers
def clear_all():
    screen.delete(0, END)

#this will clear our last numbers
def clear_1():
    txt = screen.get()[:-1]
    screen.delete(0,END)
    screen.insert(0, txt)

#this function for getting square
def square(self):

    replace()
    try:
     # evaluate the expression using the eval function
        value = eval(newtext)
    except SyntaxError or NameError:
        screen.delete(0, END)
        screen.insert(0, 'Invalid Input!')
    else:
        sqval = math.pow(value, 2)
        screen.delete(0, END)
        screen.insert(0, sqval)

#this function for getting squareroot
def square_root(num):
    replace()
    try:
         # evaluate the expression using the eval function
         value = eval(newtext)
    except SyntaxError or NameError:
         screen.delete(0, END)
         screen.insert(0, 'Invalid Input!')
    else:
         sqrtval = math.sqrt(value)
         screen.delete(0, END)
         screen.insert(0, sqrtval)

#=================functions for scientific calculator==========================================
#this all functions from math library in python
def pi():
    pi = math.pi
    screen.insert(0, pi)

def cos():
    screen1 =float(screen.get())
    cos = math.cos(screen1)
    screen.insert(0, cos)

def tan():
    screen1 = float(screen.get())
    tan = math.tan(screen1)
    screen.insert(0, tan)

def sin():
    screen1 = float(screen.get())
    sin = math.sin(screen1)
    screen.insert(0, sin)

def tau():
    tau = math.tau
    screen.insert(0, tau)

def cosh():
    screen1 = float(screen.get())
    cosh = math.cosh(screen1)
    screen.insert(0, cosh)

def tanh():
    screen1 = float(screen.get())
    tanh = math.tanh(screen1)
    screen.insert(0, tanh)

def sinh():
    screen1 = float(screen.get())
    sinh = math.sinh(screen1)
    screen.insert(0, sinh)

def log():
    screen1 = float(screen.get())
    log = math.log(screen1)
    screen.insert(0, log)

def exp():
    screen1 = float(screen.get())
    exp = math.exp(screen1)
    screen.insert(0, exp)

def lgamma():
    screen1 = float(screen.get())
    mod = math.lgamma(screen1)
    screen.insert(0, mod)


def e():
    e = math.e
    screen.insert(0, e)

 # ======================Buttons======================
# ========first_row===================
label_stuff = Label(calc, text="    ")
"""label_stuff1 = Label(calc, text="    ")"""
button_CE = Button(calc, width=8, height=1, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="X", padx=3,
                   pady=5, command= clear_1)
button_square = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="x²", padx=3,
                   pady=5, command=lambda :square("x²"))
button_c = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="AC", padx=3,
                  pady=5, command= clear_all)
button_root = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="√", padx=3,
                     pady=5, command=lambda: square_root('?'))
button_div = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text=chr(247),
                    padx=3,
                    pady=5, command=lambda: button_clicked('÷'))

# =========second_row===========
button_7 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="7", padx=3,
                  pady=5, command=lambda: button_clicked(7))
button_8 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="8", padx=3,
                  pady=5, command=lambda: button_clicked(8))
button_9 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="9", padx=3,
                  pady=5, command=lambda: button_clicked(9))
button_mult = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="x", padx=3,
                     pady=5, command=lambda: button_clicked('x'))

# =========third_row===========
button_4 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="4", padx=3,
                  pady=5, command=lambda: button_clicked(4))
button_5 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="5", padx=3,
                  pady=5, command=lambda: button_clicked(5))
button_6 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="6", padx=3,
                  pady=5, command=lambda: button_clicked(6))
button_sub = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="-", padx=3,
                    pady=5, command=lambda: button_clicked('-'))

# =========forth_row===========
button_1 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="1", padx=3,
                  pady=5, command=lambda: button_clicked(1))
button_2 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="2", padx=3,
                  pady=5, command=lambda: button_clicked(2))
button_3 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="3", padx=3,
                  pady=5, command=lambda: button_clicked(3))
button_sum = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="+", padx=3,
                    pady=5, command=lambda: button_clicked('+'))

# =========fifth_row===========
button_mode = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="%",
                         padx=3, pady=5, command=lambda: button_clicked('%'))
button_dot = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text=".", padx=3,
                    pady=5, command=lambda: button_clicked("."))
button_0 = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="0", padx=3,
                  pady=5, command=lambda: button_clicked("0"))
button_equal = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="=", padx=3,
                      pady=5, command=eval1)

label_stuff.configure(bg="#1b1c1b")
"""label_stuff1.configure(bg="#1b1c1b")"""

# ================Scientific_calculator=====================
# ====== ==============HEADING========================
heading = Label(calc, text="Scientific Calculator", font=('arial', 21, 'bold'), bg='red', fg='white')
heading.grid(row=0, column=6, columnspan=4)
# =======Sc_row1========
button_pi = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="π", padx=3,
                   pady=5, command=pi)
button_cos = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="cos", padx=3,
                    pady=5, command=cos)
button_tan = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="tan", padx=3,
                    pady=5, command=tan)
button_sin = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="sin", padx=3,
                    pady=5, command=sin)

# =======Sc_row2========
button_2pi = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="2π", padx=3,
                    pady=5, command=tau)
button_cosh = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="cosh", padx=3,
                     pady=5, command=cosh)
button_tanh = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="tanh", padx=3,
                     pady=5, command=tanh)
button_sinh = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="sinh",
                     padx=3,
                     pady=5, command=sinh)

# =======Sc_row3========
button_log = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="log", padx=3,
                    pady=5, command=log)
button_Exp = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="Exp", padx=3,
                    pady=5, command=exp)
button_lgamma = Button(calc, width=8, height=2, fg="white", bg="#1f211f", activebackground="#71c971", text="lgamma", padx=3,
                    pady=5, command=lgamma)
button_e = Button(calc, width=8, height=2, fg="#2659ff", bg="#1f211f", activebackground="#71c971", text="e", padx=3,
                  pady=5, command=e)


# ===========row_1_Display========
label_stuff.grid(row=1, column=0, )
"""label_stuff1.grid(row=2, column=0, )"""
button_CE.grid(row=2, column=3)
button_c.grid(row=3, column=0)
button_square.grid(row=3, column=1)
button_root.grid(row=3, column=2)
button_div.grid(row=3, column=3)

# ===========row_2_Display=====
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_mult.grid(row=4, column=3)

# =========row_3_Display=======
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_sub.grid(row=5, column=3)

# =========row_4_Display=======
button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_sum.grid(row=6, column=3)

# ==========row_5_Display=======
button_mode.grid(row=7, column=0)
button_dot.grid(row=7, column=1)
button_0.grid(row=7, column=2)
button_equal.grid(row=7, column=3)

# ==========Scentific_row_1======
button_pi.grid(row=4, column=6)
button_cos.grid(row=4, column=7)
button_tan.grid(row=4, column=8)
button_sin.grid(row=4, column=9)

# ==========Scentific_row_2======
button_2pi.grid(row=5, column=6)
button_cosh.grid(row=5, column=7)
button_tanh.grid(row=5, column=8)
button_sinh.grid(row=5, column=9)

# ==========Scentific_row_3======
button_log.grid(row=6, column=6)
button_Exp.grid(row=6, column=7)
button_lgamma.grid(row=6, column=8)
button_e.grid(row=6, column=9)


# ========================MENU========================================
#for standard calculator
def Standard():
    window.resizable(width=False, height=False)
    window.geometry('398x350+0+0')

#for Scientific calculator
def Scientific():
    window.resizable(width=False, height=False)
    window.geometry('713x350+0+0')
#for getting info about me
#this will go to direct my personal website page
def about():
    webbrowser.open('https://shaneeb-123.github.io/shanu-personal/')

#this will exit calculator application
def Exit():
    Exit = tkinter.messagebox.askyesno("Do you agree to exit your SMART CAlCULATOR")
    if Exit > 0:
        window.destroy()
        return

#==============for menubar============================
menu_bar = Menu(calc)
menu_bar.configure(bg='#242123',fg='white')
#==============for file in menubar============================
file_menu = Menu(menu_bar, tearoff=0)
file_menu.configure(fg='white',bg='#1b1c1b')
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Standard", command=Standard)
file_menu.add_command(label="Scientific", command=Scientific)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=Exit)

#==============for unit in menubar============================
unit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Converter", menu=unit_menu)
unit_menu.add_command(label="Length", command=length)
unit_menu.add_command(label="Mass", command=mass)
unit_menu.add_command(label="Temperature", command=temperature)
unit_menu.add_command(label="Volume", command=volume)
unit_menu.configure(fg='white',bg='#1b1c1b')

#==============for help in menubar============================
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Info",command=about)
help_menu.configure(fg='white',bg='#1b1c1b')

window.config(menu=menu_bar)
window.mainloop()







