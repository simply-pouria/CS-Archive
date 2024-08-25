import tkinter as tk
import interactions
from utilities import libraries
from GUI_utilities import WindowSwitchButton as Wsb


#### MENUS ####
# each menu is implemented as a function so that switching windows is easier
def main_menu():
    root = tk.Tk()
    root.title("Main Menu")

    label = tk.Label(root,
                     text="Welcome to Main Menu",
                     height=3,
                     width=30,
                     bd=3,
                     fg="black")

    mod_libs = Wsb(label="Show, Add, or Remove Libraries",
                   root=root,
                   target_window=mod_lib_menu,
                   grid_place=(1, 0))

    mod_books = Wsb(label="Show, Add, Remove, or edit Books",
                    root=root,
                    target_window=choose_lib_menu,
                    grid_place=(2, 0))

    label.grid(column=0, row=0, padx=10, pady=10)

    root.mainloop()


def mod_lib_menu():
    root = tk.Tk()
    root.title("Library Management")

    def add_lib_cmd():
        lib_name = entry.get()
        interactions.add_lib_cmd(lib_name)

    def show_lib_cmd():
        lib_name = entry.get()
        interactions.show_lib_cmd(lib_name=lib_name, df=libraries[lib_name].df)

    def delete_lib_cmd():
        lib_name = entry.get()
        interactions.delete_lib_cmd(lib_name=lib_name)

    label = tk.Label(root,
                     text="Enter the name of the Library to add, remove or show it:",
                     height=3,
                     bd=3,
                     fg="black")

    entry = tk.Entry(root)

    add_lib_btn = tk.Button(root,
                            text="Add this Library",
                            command=add_lib_cmd)

    del_lib_btn = tk.Button(root,
                            text="Remove this Library",
                            command=delete_lib_cmd)

    show_lib_btn = tk.Button(root,
                             text="Show this Library",
                             command=show_lib_cmd)

    mod_books = Wsb(label="Back to Main Menu",
                    root=root,
                    target_window=main_menu,
                    grid_place=(3, 0))

    label.grid(column=0, row=0, padx=10, pady=10, columnspan=3)
    entry.grid(column=0, row=1, padx=10, pady=10, columnspan=3)
    add_lib_btn.grid(column=0, row=2, padx=5, pady=5)
    del_lib_btn.grid(column=1, row=2, padx=5, pady=5)
    show_lib_btn.grid(column=2, row=2, padx=5, pady=5)

    root.mainloop()


def choose_lib_menu():
    def add_book():
        def add_book_cmd():
            interactions.add_book_cmd(library=libraries[lib_name.get()],
                                      name=name.get(),
                                      release_date=release_date.get(),
                                      author=authors.get(),
                                      keyword=keyword.get())

        # creating a window to get information
        root_add = tk.Tk()
        root_add.title("Add Book")

        header = tk.Label(root_add,
                          text="Enter the data of the new book",
                          height=3,
                          bd=3,
                          fg="black",
                          font=("Arial", 12))

        name_label = tk.Label(root_add,
                              text="Name",
                              height=3,
                              bd=3,
                              fg="black",
                              font=("Arial", 8))

        name = tk.Entry(root_add)

        release_date_label = tk.Label(root_add,
                                      text="Release Date",
                                      height=3,
                                      bd=3,
                                      fg="black",
                                      font=("Arial", 8))
        release_date = tk.Entry(root_add)

        authors_label = tk.Label(root_add,
                                 text="Authors",
                                 height=3,
                                 bd=3,
                                 fg="black",
                                 font=("Arial", 8))
        authors = tk.Entry(root_add)
        keyword_label = tk.Label(root_add,
                                 text="Keyword",
                                 height=3,
                                 bd=3,
                                 fg="black",
                                 font=("Arial", 8))
        keyword = tk.Entry(root_add)

        submit_btn = tk.Button(root_add,
                               text="Submit Changes",
                               command=add_book_cmd)

        # placing UI elements using Grid layout manager
        header.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        name_label.grid(column=0, row=1, padx=10, pady=10)
        name.grid(column=1, row=1, padx=10, pady=10)
        release_date_label.grid(column=0, row=2, padx=10, pady=10)
        release_date.grid(column=1, row=2, padx=10, pady=10)
        authors_label.grid(column=0, row=3, padx=10, pady=10)
        authors.grid(column=1, row=3, padx=10, pady=10)
        keyword_label.grid(column=0, row=4, padx=10, pady=10)
        keyword.grid(column=1, row=4, padx=10, pady=10)
        submit_btn.grid(column=0, row=5, padx=5, pady=5, columnspan=2)

    def del_book():
        def del_book_cmd():
            interactions.delete_book_cmd(lib_name=lib_name.get(), book_name=book_name.get())

        root_del = tk.Tk()
        root_del.title("Choose Book")

        label = tk.Label(root_del,
                         text="Enter the name of the book you want to delete from the Library",
                         height=3,
                         bd=3,
                         fg="black")

        book_name = tk.Entry(root_del)

        delete_book_btn = tk.Button(root_del,
                                    text="Remove this book from the library",
                                    command=del_book_cmd)

        label.grid(column=0, row=0, padx=10, pady=10)
        book_name.grid(column=0, row=1, padx=10, pady=10)
        delete_book_btn.grid(column=0, row=2, padx=5, pady=5)

    def show_book():
        def show_book_cmd():
            interactions.show_book_cmd(lib_name=lib_name.get(), book_name=book_name.get())

        root_show = tk.Tk()
        root_show.title("Choose Book")

        label = tk.Label(root_show,
                         text="Enter the name of the book you want to show from the Library",
                         height=3,
                         bd=3,
                         fg="black")

        book_name = tk.Entry(root_show)

        add_book_btn = tk.Button(root_show,
                                 text="show this book from the library",
                                 command=show_book_cmd)

        label.grid(column=0, row=0, padx=10, pady=10)
        book_name.grid(column=0, row=1, padx=10, pady=10)
        add_book_btn.grid(column=0, row=2, padx=5, pady=5)

    def edit_book():
        def submit_data():
            interactions.edit_book_cmd(library=libraries[lib_name.get()],
                                       name=name.get(),
                                       release_date=release_date.get(),
                                       author=authors.get(),
                                       keyword=keyword.get())

        # creating a window to get information to edit with
        root_edit = tk.Tk()
        root_edit.title("Edit Book")

        header = tk.Label(root_edit,
                          text="Enter the new data",
                          height=3,
                          bd=3,
                          fg="black",
                          font=("Arial", 12))

        name_label = tk.Label(root_edit,
                              text="Name",
                              height=3,
                              bd=3,
                              fg="black",
                              font=("Arial", 8))
        name = tk.Entry(root_edit)

        warning = tk.Label(root_edit,
                           text="*the following data will replace the existing data \nof the book with the name above",
                           height=3,
                           bd=3,
                           fg="red",
                           font=("Arial", 8))

        release_date_label = tk.Label(root_edit,
                                      text="Release Date",
                                      height=3,
                                      bd=3,
                                      fg="black",
                                      font=("Arial", 8))
        release_date = tk.Entry(root_edit)
        authors_label = tk.Label(root_edit,
                                 text="Authors",
                                 height=3,
                                 bd=3,
                                 fg="black",
                                 font=("Arial", 8))
        authors = tk.Entry(root_edit)
        keyword_label = tk.Label(root_edit,
                                 text="Keyword",
                                 height=3,
                                 bd=3,
                                 fg="black",
                                 font=("Arial", 8))
        keyword = tk.Entry(root_edit)

        submit_btn = tk.Button(root_edit,
                               text="Submit Changes",
                               command=submit_data)

        # placing UI elements using Grid layout manager
        header.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        name_label.grid(column=0, row=1, padx=10, pady=10)
        name.grid(column=1, row=1, padx=10, pady=10)
        warning.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
        release_date_label.grid(column=0, row=3, padx=10, pady=10)
        release_date.grid(column=1, row=3, padx=10, pady=10)
        authors_label.grid(column=0, row=4, padx=10, pady=10)
        authors.grid(column=1, row=4, padx=10, pady=10)
        keyword_label.grid(column=0, row=5, padx=10, pady=10)
        keyword.grid(column=1, row=5, padx=10, pady=10)
        submit_btn.grid(column=0, row=6, padx=5, pady=5, columnspan=2)

    root = tk.Tk()
    root.title("Choosing Library")

    label = tk.Label(root,
                     text="Choose the library that you want to access it books:",
                     height=3,
                     bd=3,
                     fg="black")

    lib_name = tk.Entry(root)

    add_lib_btn = tk.Button(root,
                            text="Add to This Library",
                            command=add_book)

    del_lib_btn = tk.Button(root,
                            text="Remove from This Library",
                            command=del_book)

    edit_lib_btn = tk.Button(root,
                             text="Edit books From This Library",
                             command=edit_book)

    show_lib_btn = tk.Button(root,
                             text="Show from This Library",
                             command=show_book)

    mod_books = Wsb(label="Back to Main Menu",
                    root=root,
                    target_window=main_menu,
                    grid_place=(3, 0))

    label.grid(column=0, row=0, padx=10, pady=10, columnspan=4)
    lib_name.grid(column=0, row=1, padx=10, pady=10, columnspan=4)
    add_lib_btn.grid(column=0, row=2, padx=5, pady=5)
    del_lib_btn.grid(column=1, row=2, padx=5, pady=5)
    edit_lib_btn.grid(column=2, row=2, padx=5, pady=5)
    show_lib_btn.grid(column=3, row=2, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_menu()
