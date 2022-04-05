# 05/04/22

# modules
from tkinter import *


# objects
class DataCollectGUI:
    def __init__(self, parent):
        # initialising personal data list
        self.data = []

        # initialising constants for graphics
        self.FONT = "Arial 12 bold"
        self.BG1 = 'magenta'
        self.BG2 = 'light blue'

        # initialising frames
        self.main = Frame(parent)
        f1 = Frame(self.main, bg=self.BG1)
        f2 = Frame(self.main, bg=self.BG2)

        # initialising widget variables
        self.yes_or_no_var = StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.yes_or_no_var.set('*')

        # initialising label widgets
        collect_data_label = Label(self.main, text="Collecting Person Data", bg=self.BG1, font=self.FONT)
        name_label = Label(self.main, text='First Name:', bg=self.BG2)
        age_label = Label(self.main, text='Age:', bg=self.BG2)
        phone_q_label = Label(self.main, text='Do you have a mobile phone?', bg=self.BG2)

        # initialising entry widgets
        self.name_entry = Entry(self.main, width=30, textvariable=self.name_var)
        self.age_entry = Entry(self.main, width=30, textvariable=self.age_var)

        # initialising button widgets
        show_all_button = Button(self.main, text="Show All", pady=2, padx=5, font=self.FONT)
        yes_option = Radiobutton(self.main, text='Yes', value='Yes', variable=self.yes_or_no_var, bg=self.BG2)
        no_option = Radiobutton(self.main, text='No', value='No', variable=self.yes_or_no_var, bg=self.BG2)
        enter_button = Button(self.main, text='Enter Data', pady=2, padx=5, font=self.FONT, command=self.enter_data)

        # widget grid
        self.main.grid(row=0, column=0)
        f1.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        f2.grid(row=1, column=0, rowspan=6, columnspan=2, sticky=NSEW)
        collect_data_label.grid(row=0, column=0, pady=20, padx=40)
        show_all_button.grid(row=0, column=1, pady=20, padx=20, sticky=W)
        name_label.grid(row=1, column=0, pady=6, padx=40, sticky=W)
        age_label.grid(row=2, column=0, pady=6, padx=40, sticky=W)
        self.name_entry.grid(row=1, column=1, pady=6, padx=10)
        self.age_entry.grid(row=2, column=1, pady=6, padx=10)
        phone_q_label.grid(row=3, pady=6, padx=40, sticky=W)
        yes_option.grid(row=3, column=1, pady=6, sticky=W)
        no_option.grid(row=4, column=1, pady=6, sticky=W)
        enter_button.grid(row=5, columnspan=2, pady=10)

    def enter_data(self):
        name = self.name_var.get()
        age = self.age_var.get()
        phone = self.yes_or_no_var.get()
        error_label = Label(self.main, text='', bg=self.BG2)
        error_label.grid(row=6, columnspan=2, pady=10)
        if name.isalpha() and age.isnumeric() and phone != '*':
            error_label.configure(text="Data entered successfully!")
            self.data.append(Person(name, age, phone))
            self.yes_or_no_var.set('*')
            self.name_entry.delete(0, END)
            self.age_entry.delete(0, END)
        else:
            if not name.isalpha():
                error_label.configure(text="Please enter a valid name")
            elif not age.isnumeric():
                error_label.configure(text="Please enter a positive integer for age")
            elif phone == '*':
                error_label.configure(text="Please select an option for phone availability")


class DataDisplay:
    pass


class Person:
    def __init__(self, name, age, phone_availability):
        self.name = name
        self.age = age
        self.phone = phone_availability


# main routine
root = Tk()
DataCollectGUI(root)

root.mainloop()
