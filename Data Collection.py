# 05/04/22

# modules
from tkinter import *


# objects
class DataCollectGUI:

    def __init__(self, parent):
        # initialising personal data list
        self.person_data = PersonDataStorage()

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

        # initialising widgets for list
        self.collect_data_widgets = []
        self.display_data_widgets = []

        """
        Widgets for collecting data
        """

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

        # appending collect data widgets
        self.collect_data_widgets.append(self.name_entry)
        self.collect_data_widgets.append(self.age_entry)
        self.collect_data_widgets.append(self.phone_q_label)
        self.collect_data_widgets.append(self.yes_option)
        self.collect_data_widgets.append(self.no_option)
        self.collect_data_widgets.append(self.enter_button)
        self.collect_data_widgets.append(self.error_label)

        """
        Widgets for displaying data
        """

        # initialising label widgets
        self.display_name_label = Label(self.main, bg=self.BG2)
        self.display_age_label = Label(self.main, bg=self.BG2)
        self.display_statement_label = Label(self.main, bg=self.BG2)

        # initialising button widgets
        self.previous_button = Button(self.main, text='Previous', command=lambda: self.next_display(-1))
        self.next_button = Button(self.main, text='Next', command=lambda: self.next_display(1))

        # appending display data widgets
        self.display_data_widgets.append(self.display_name_label)
        self.display_data_widgets.append(self.display_age_label)
        self.display_data_widgets.append(self.display_statement_label)
        self.display_data_widgets.append(self.next_button)
        self.display_data_widgets.append(self.previous_button)

    def enter_data(self):
        name = self.name_var.get()
        age = self.age_var.get()
        phone = self.yes_or_no_var.get()
        if name.isalpha() and age.isnumeric() and phone != '*':
            if int(age) <= 200:
                self.error_label.configure(text="Data entered successfully!")
                self.person_data.add_data(name, age, phone)
                self.yes_or_no_var.set('*')
                self.name_entry.delete(0, END)
                self.age_entry.delete(0, END)
            else:
                self.error_label.configure(text="You cannot be more than 200 years old")
        else:
            if not name.isalpha():
                self.error_label.configure(text="Please enter a valid name")
            elif not age.isnumeric():
                self.error_label.configure(text="Please enter a positive integer for age")
            elif phone == '*':
                self.error_label.configure(text="Please select an option for phone availability")

    def display(self):
        if len(self.person_data.data) == 0:
            self.error_label.configure(text="No data available to show")
        else:
            # destroying unnecessary widgets
            for widget in self.collect_data_widgets:
                widget.grid_forget()

            # reconfiguring widgets
            self.collect_data_label.configure(text="Displaying Person Data")
            self.show_all_button.configure(text="Add New Person", command=self.collect_data)
            self.display_name_label.configure(text=self.person_data.call_name(self.x))
            self.display_age_label.configure(text=self.person_data.call_age(self.x))
            self.display_statement_label.configure(text=self.person_data.phone_statement(self.x))

            # widget grid
            self.display_name_label.grid(row=1, column=1, pady=6, padx=10)
            self.display_age_label.grid(row=2, column=1, pady=6, padx=10)
            self.display_statement_label.grid(row=3, columnspan=2, pady=6)
            self.previous_button.grid(row=4, column=0, pady=6, padx=10, sticky=W)
            self.next_button.grid(row=4, column=1, pady=6, padx=10, sticky=E)

    # function for binding to next and previous buttons for displaying other data
    def next_display(self, n):
        if self.x == 0 and n == -1:
            self.x = len(self.person_data.data) - 1
        elif self.x == len(self.person_data.data) - 1 and n == 1:
            self.x = 0
        else:
            self.x += n
        self.display_name_label.configure(text=self.person_data.call_name(self.x))
        self.display_age_label.configure(text=self.person_data.call_age(self.x))
        self.display_statement_label.configure(text=self.person_data.phone_statement(self.x))

    def collect_data(self):
        for widget in self.display_data_widgets:
            widget.grid_forget()

        # reconfiguring widgets
        self.collect_data_label.configure(text="Collecting Person Data")
        self.show_all_button.configure(text="Show All", command=self.display)
        self.error_label.configure(text='Please answer all the fields before entering data')

        # widget grid
        self.name_entry.grid(row=1, column=1, pady=6, padx=10)
        self.age_entry.grid(row=2, column=1, pady=6, padx=10)
        self.phone_q_label.grid(row=3, pady=6, padx=40, sticky=W)
        self.yes_option.grid(row=3, column=1, pady=6, sticky=W)
        self.no_option.grid(row=4, column=1, pady=6, sticky=W)
        self.enter_button.grid(row=5, columnspan=2, pady=10)
        self.error_label.grid(row=6, columnspan=2, pady=10)


class PersonDataStorage:
    def __init__(self):
        self.data = []

    def add_data(self, name, age, phone_availability):
        self.data.append((name, age, phone_availability))

    def call_name(self, index):
        return self.data[index][0].title()

    def call_age(self, index):
        return self.data[index][1]

    def phone_statement(self, index):
        if self.data[index][2] == 'Yes':
            return f"{self.call_name(index)} does have a mobile phone"
        else:
            return f"{self.call_name(index)} does not have a mobile phone"


# main routine
root = Tk()
root.resizable(0, 0)
DataCollectGUI(root)
root.mainloop()
