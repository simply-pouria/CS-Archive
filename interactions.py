import os
from tkinter import messagebox


# functions in this file are commands of the buttons and used to interact with the dataframe.
def add_lib_cmd(lib_name):
    for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        if lib_name == library:
            messagebox.showerror("showerror", "Error")
























