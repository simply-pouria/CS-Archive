import os
from tkinter import messagebox
import tkinter as tk
from utilities import Library
import utilities
from utilities import Book
import pandas as pd


# functions in this file are commands of the buttons and used to interact with the dataframe.
def add_lib_cmd(lib_name: str) -> None:
    for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        if lib_name == library:
            messagebox.showerror("Repetitive Name", "The library name must be unique")
            return

    lib = Library(lib_name)
    lib.save_csv()
    messagebox.showinfo("Successful", "The empty library has been added")


def delete_lib_cmd(lib_name: str) -> None:
    for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        if lib_name == library:
            os.remove(f"{os.getcwd()}\\csv_files\\{lib_name}")
            del utilities.libraries[lib_name]


def show_lib_cmd(lib_name: str, df: pd.DataFrame) -> None:
    for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        if lib_name == library:
            rt = tk.Tk()
            rt.title('Library Data')
            tk.Label(rt, text=df.loc[:, :], font=("Arial", 20, "bold")).pack()


def add_book_cmd(library: Library, name: str, author: str, keyword: str, release_date: str) -> None:
    book = Book(name, author, keyword, release_date)
    library.add(book)


def edit_book_cmd(library: Library, name: str, author: str, keyword: str, release_date: str) -> None:
    book = Book(name, author, keyword, release_date)
    library.edit(book)


def delete_book_cmd(library: Library, name: str) -> None:
     data_with_index = library.df.set_index("name")
     data_with_index = data_with_index.drop(name)