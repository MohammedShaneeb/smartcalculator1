from tkinter import *


def length():
    window1 = Toplevel()
    window1.title("Length Converter")
    window1.geometry('370x200+0+0')
    window1.resizable(width=False, height=False)
    window1.configure(bg='#1b1c1b')

    def from_km():
        # convert km to cm
        cm = float(length_screen.get()) * 100000

        # convert km to metre
        metre = float(length_screen.get()) * 1000

        # convert km to millimetre
        millimetre = float(length_screen.get()) * 1000000

        # Enters the converted km to
        text1.delete("1.0", END)
        text1.insert(END, cm)

        text2.delete("1.0", END)
        text2.insert(END, metre)

        text3.delete("1.0", END)
        text3.insert(END, millimetre)

    # Create the  widgets
    label_1 = Label(window1, text="Enter the length in Km", bg='red', fg='white', font=('20'))
    length_screen = StringVar()
    label_2 = Entry(window1, textvariable=length_screen, bg='#4f6658', fg='white', font=('10'))
    label_3 = Label(window1, text='Cm', bg='#1b1c1b', fg='white')
    label_4 = Label(window1, text='Metre', bg='#1b1c1b', fg='white')
    label_5 = Label(window1, text='Millimetre', bg='#1b1c1b', fg='white', font=('20'))

    # Create the Text Widgets
    text1 = Text(window1, height=1, width=20)
    text2 = Text(window1, height=1, width=20)
    text3 = Text(window1, height=1, width=20)

    # Create the Button Widget
    b1 = Button(window1, text="Convert", fg="white", bg="#1f211f", activebackground="#71c971", command=from_km)
    label_stuff_3 = Label(window1, text='   ')
    label_stuff_4 = Label(window1, text='   ')
    label_stuff_5 = Label(window1, text='   ')

    #calling above widgets and buttons
    label_1.grid(row=1, column=1)
    label_2.grid(row=2, column=1)
    label_3.grid(row=6, column=0)
    label_4.grid(row=7, column=0)
    label_5.grid(row=8, column=0)
    text1.grid(row=6, column=1)
    text2.grid(row=7, column=1)
    text3.grid(row=8, column=1)
    b1.grid(row=4, column=1)
    label_stuff_3.grid(row=5, column=1)
    label_stuff_3.configure(bg='#1b1c1b')



    label_stuff_5.grid(row=3, column=1)
    label_stuff_5.configure(bg='#1b1c1b')

    window1.mainloop()
