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


def show_book_cmd(lib_name, book_name: str) -> None:

    for library in os.listdir(f'{os.getcwd()}\\csv_files'):

        if lib_name == library:
            lib_dict = utilities.libraries[lib_name].df.to_dict()
            print("passed")

            for row in lib_dict['name']:

                book = lib_dict["name"][row]

                if book_name == book:

                    book_info = utilities.libraries[lib_name].df.loc[row, :]
                    print("passed2")
                    rt = tk.Tk()
                    rt.title('Library Data')
                    tk.Label(rt, text=book_info, font=("Arial", 20, "bold")).pack()
                    return

    messagebox.showerror("book not found", "The book you were looking for was not found in the library or the library "
                                           "did not exist")


def delete_book_cmd(lib_name: str, book_name: str) -> None:

    for library in os.listdir(f'{os.getcwd()}\\csv_files'):

        if lib_name == library:
            lib_dict = utilities.libraries[lib_name].df.to_dict()
            print("passed")

            for row in lib_dict['name']:

                book = lib_dict["name"][row]
                print(book)

                if book_name == book:
                    utilities.libraries[lib_name].df = utilities.libraries[lib_name].df.drop(index=row, axis=0)
                    utilities.libraries[lib_name].save_csv()

                    return

    messagebox.showerror("book not found", "The book you were looking for was not found in the library or the library "
                                           "did not exist")





