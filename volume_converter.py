from tkinter import *


def volume():
    window5 = Toplevel()
    window5.title("Volume Converter")
    window5.geometry('370x200+0+0')
    window5.resizable(width=False, height=False)
    window5.configure(bg='#1b1c1b')

    def from_lt():
        # litre kg to gram
        ml = float(length_screen.get()) * 1000


        # Enters the converted litre to
        # the text widget
        text1.delete("1.0", END)
        text1.insert(END, ml)



    # Create the Label widgets
    label_1 = Label(window5, text="Enter the volume in litre", bg='red', fg='white', font=('20'))
    length_screen = StringVar()
    label_2 = Entry(window5, textvariable=length_screen, bg='#4f6658', fg='white', font=('10'))
    label_3 = Label(window5, text='Millilitre', bg='#1b1c1b', fg='white')


    # Create the Text Widgets
    text1 = Text(window5, height=1, width=20)


    # Create the Button Widget
    b1 = Button(window5, text="Convert", fg="white", bg="#1f211f", activebackground="#71c971", command=from_lt)
    label_stuff_3 = Label(window5, text='   ')
    label_stuff_5 = Label(window5, text='   ')


    label_1.grid(row=1, column=1)
    label_2.grid(row=2, column=1)
    label_3.grid(row=6, column=0)

    text1.grid(row=6, column=1)

    b1.grid(row=4, column=1)
    label_stuff_3.grid(row=5, column=1)
    label_stuff_3.configure(bg='#1b1c1b')

    label_stuff_5.grid(row=3, column=1)
    label_stuff_5.configure(bg='#1b1c1b')

    window5.mainloop()
