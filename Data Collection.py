# 05/04/22

# modules
from tkinter import *


# objects
class DataCollectGUI:
    def __init__(self, parent):
        # initialising constants for graphics
        FONT = "Arial 12 bold"
        BG1 = 'magenta'
        BG2 = 'light blue'

        # initialising frames
        main = Frame(parent)
        f1 = Frame(main, bg=BG1)
        f2 = Frame(main, bg=BG2)

        # initialising label widgets
        collect_data_label = Label(main, text="Collecting Person Data", bg=BG1, font=FONT)
        name_label = Label(main, text='First Name:', bg=BG2)
        age_label = Label(main, text='Age:', bg=BG2)
        phone_q_label = Label(main, text='Do you have a mobile phone?', bg=BG2)

        # initialising entry widgets
        name_entry = Entry(main, width=30)
        age_entry = Entry(main, width=30)

        # initialising button variables
        self.yes_or_no_var = StringVar()
        self.yes_or_no_var.set('*')

        # initialising button widgets
        show_all_button = Button(main, text="Show All", pady=2, padx=5, font=FONT)
        yes_option = Radiobutton(main, text='Yes', value='Yes', variable=self.yes_or_no_var, bg=BG2)
        no_option = Radiobutton(main, text='No', value='No', variable=self.yes_or_no_var, bg=BG2)
        enter_button = Button(main, text='Enter', pady=2, padx=5, font=FONT)

        # widget grid
        main.grid(row=0, column=0)
        f1.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        f2.grid(row=1, column=0, rowspan=5, columnspan=2, sticky=NSEW)
        collect_data_label.grid(row=0, column=0, pady=20, padx=40)
        show_all_button.grid(row=0, column=1, pady=20, padx=20, sticky=W)
        name_label.grid(row=1, column=0, pady=6, padx=40, sticky=W)
        age_label.grid(row=2, column=0, pady=6, padx=40, sticky=W)
        name_entry.grid(row=1, column=1, pady=6, padx=10)
        age_entry.grid(row=2, column=1, pady=6, padx=10)
        phone_q_label.grid(row=3, pady=6, padx=40, sticky=W)
        yes_option.grid(row=3, pady=6, column=1, sticky=W)
        no_option.grid(row=4, pady=6, column=1, sticky=W)
        enter_button.grid(row=5, columnspan=2, pady=20)

# main routine
root = Tk()
DataCollectGUI(root)

root.mainloop()
