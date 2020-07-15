from tkinter import *


def mass():
    window2 = Toplevel()
    window2.title("Mass Converter")
    window2.geometry('370x200+0+0')
    window2.resizable(width=False, height=False)
    window2.configure(bg='#1b1c1b')

    def from_kg():
        # convert kg to gram
        gram = float(length_screen.get()) * 1000

        # convert kg to pound
        pound = float(length_screen.get()) * 2.205

        # convert kg to ounce
        ton = float(length_screen.get()) * 0.001

        # Enters the converted weight to

        text1.delete("1.0", END)
        text1.insert(END, gram)

        text2.delete("1.0", END)
        text2.insert(END, pound)

        text3.delete("1.0", END)
        text3.insert(END, ton)

    # Create the Label widgets
    label_1 = Label(window2, text="Enter the weight in Kg", bg='red', fg='white', font=('20'))
    length_screen = StringVar()
    label_2 = Entry(window2, textvariable=length_screen, bg='#4f6658', fg='white', font=('10'))
    label_3 = Label(window2, text='Gram', bg='#1b1c1b', fg='white')
    label_4 = Label(window2, text='Pound', bg='#1b1c1b', fg='white')
    label_5 = Label(window2, text='Ton', bg='#1b1c1b', fg='white', font=('20'))

    # Create the Text Widgets
    text1 = Text(window2, height=1, width=20)
    text2 = Text(window2, height=1, width=20)
    text3 = Text(window2, height=1, width=20)

    # Create the Button Widget
    b1 = Button(window2, text="Convert", fg="white", bg="#1f211f", activebackground="#71c971", command=from_kg)
    label_stuff_3 = Label(window2, text='   ')
    label_stuff_5 = Label(window2, text='   ')

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

    window2.mainloop()
