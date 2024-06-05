import os
from tkinter import messagebox
import tkinter as tk
from utilities import Library
import pandas as pd

# functions in this file are commands of the buttons and used to interact with the dataframe.
def add_lib_cmd(lib_name: str) -> None:

    for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        if lib_name == library:
            messagebox.showerror("Repetitive Name", "The library name must be unique")

    lib = Library(lib_name)
    lib.save_csv()
    messagebox.showinfo("Successful", "The empty library has been added")


def show_lib_cmd(lib_name: str, df: pd.DataFrame) -> None:

    for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        if lib_name == library:
            rt = tk.Tk()
            rt.geometry('300x300')
            rt.title('Library Data')


































