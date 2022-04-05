# 05/04/22

# modules
from tkinter import *


# objects
class DataCollectGUI:

    def __init__(self, parent):
        # initialising personal data list
        self.data = []

        # initialising data index number
        self.x = 0

        # initialising constants for graphics
        self.FONT = "Arial 12 bold"
        self.BG1 = 'magenta'
        self.BG2 = 'light blue'

        # initialising frames
        self.main = Frame(parent)
        self.f1 = Frame(self.main, bg=self.BG1)
        self.f2 = Frame(self.main, bg=self.BG2)

        # initialising widget variables
        self.yes_or_no_var = StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.yes_or_no_var.set('*')

        # initialising label widgets
        self.collect_data_label = Label(self.main, text="Collecting Person Data", bg=self.BG1, font=self.FONT)
        self.name_label = Label(self.main, text='First Name:', bg=self.BG2)
        self.age_label = Label(self.main, text='Age:', bg=self.BG2)
        self.phone_q_label = Label(self.main, text='Do you have a mobile phone?', bg=self.BG2)
        self.error_label = Label(self.main, text='Please answer all the fields before entering data', bg=self.BG2)

        # initialising entry widgets
        self.name_entry = Entry(self.main, width=30, textvariable=self.name_var)
        self.age_entry = Entry(self.main, width=30, textvariable=self.age_var)

        # initialising button widgets
        self.show_all_button = Button(self.main, text="Show All", pady=2, padx=5, font=self.FONT, command=self.display)
        self.yes_option = Radiobutton(self.main, text='Yes', value='Yes', variable=self.yes_or_no_var, bg=self.BG2)
        self.no_option = Radiobutton(self.main, text='No', value='No', variable=self.yes_or_no_var, bg=self.BG2)
        self.enter_button = Button(self.main, text='Enter Data', pady=2, padx=5, font=self.FONT, command=self.enter_data)

        # widget grid
        self.main.grid(row=0, column=0)
        self.f1.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.f2.grid(row=1, column=0, rowspan=6, columnspan=2, sticky=NSEW)
        self.collect_data_label.grid(row=0, column=0, pady=20, padx=40)
        self.show_all_button.grid(row=0, column=1, pady=20, padx=20, sticky=W)
        self.name_label.grid(row=1, column=0, pady=6, padx=40, sticky=W)
        self.age_label.grid(row=2, column=0, pady=6, padx=40, sticky=W)
        self.name_entry.grid(row=1, column=1, pady=6, padx=10)
        self.age_entry.grid(row=2, column=1, pady=6, padx=10)
        self.phone_q_label.grid(row=3, pady=6, padx=40, sticky=W)
        self.yes_option.grid(row=3, column=1, pady=6, sticky=W)
        self.no_option.grid(row=4, column=1, pady=6, sticky=W)
        self.enter_button.grid(row=5, columnspan=2, pady=10)
        self.error_label.grid(row=6, columnspan=2, pady=10)

    def enter_data(self):
        name = self.name_var.get()
        age = self.age_var.get()
        phone = self.yes_or_no_var.get()
        if name.isalpha() and age.isnumeric() and phone != '*':
            self.error_label.configure(text="Data entered successfully!")
            self.data.append(Person(name, age, phone))
            self.yes_or_no_var.set('*')
            self.name_entry.delete(0, END)
            self.age_entry.delete(0, END)
        else:
            if not name.isalpha():
                self.error_label.configure(text="Please enter a valid name")
            elif not age.isnumeric():
                self.error_label.configure(text="Please enter a positive integer for age")
            elif phone == '*':
                self.error_label.configure(text="Please select an option for phone availability")

    def display(self):
        if len(self.data) == 0:
            self.error_label.configure(text="No data available to show")
        else:

            # function for binding to next and previous buttons for displaying other data
            def next_display(n):
                print(self.x)
                if self.x == 0 and n == -1:
                    self.x = len(self.data)-1
                elif self.x == len(self.data)-1 and n == 1:
                    self.x = 0
                else:
                    self.x += n
                display_name_label.configure(text=self.data[self.x].name.title())
                display_age_label.configure(text=self.data[self.x].age)
                if self.data[self.x].phone == 'Yes':
                    display_statement_label.configure(text=f"{self.data[self.x].name.title()} does have a mobile phone")
                else:
                    display_statement_label.configure(text=f"{self.data[self.x].name.title()} does not have a mobile phone")


            # destroying unnecessary widgets
            self.name_entry.destroy()
            self.age_entry.destroy()
            self.yes_option.destroy()
            self.no_option.destroy()
            self.phone_q_label.destroy()
            self.enter_button.destroy()
            self.error_label.destroy()

            # reconfiguring widgets
            self.collect_data_label.configure(text="Displaying Person Data")
            self.show_all_button.configure(text="Add New Person")

            # initialising button widgets
            previous_button = Button(self.main, text='Previous', command=lambda: next_display(-1))
            next_button = Button(self.main, text='Next', command=lambda: next_display(1))

            # initialising label widgets
            display_name_label = Label(self.main, text=self.data[self.x].name.title(), bg=self.BG2)
            display_age_label = Label(self.main, text=self.data[self.x].age, bg=self.BG2)
            display_statement_label = Label(self.main, bg=self.BG2)
            if self.data[self.x].phone == 'Yes':
                display_statement_label.configure(text=f"{self.data[self.x].name.title()} does have a mobile phone")
            else:
                display_statement_label.configure(text=f"{self.data[self.x].name.title()} does not have a mobile phone")

            # widget grid
            display_name_label.grid(row=1, column=1, pady=6, padx=10)
            display_age_label.grid(row=2, column=1, pady=6, padx=10)
            display_statement_label.grid(row=3, columnspan=2, pady=6)
            previous_button.grid(row=4, column=0, pady=6, padx=10, sticky=W)
            next_button.grid(row=4, column=1, pady=6, padx=10, sticky=E)


class Person:
    def __init__(self, name, age, phone_availability):
        self.name = name
        self.age = age
        self.phone = phone_availability


# main routine
root = Tk()
DataCollectGUI(root)
root.mainloop()
