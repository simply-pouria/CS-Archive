import pandas as pd
import os


class Book:
    def __init__(self, name: str, author: str, keyword: str, release_date: str) -> None:
        self.name = name
        self.author = author
        self.keyword = keyword
        self.release_date = release_date

    def edit_name(self, name: str):
        self.name = name

    def edit_author(self, author: str):
        self.author = author

    def edit_keyword(self, keyword: str):
        self.keyword = keyword

    def edit_release_date(self, release_date: str):
        self.release_date = release_date


libraries = {}


class Library:
    def __init__(self, lib_name: str, *args: Book) -> None:

        self.lib_name = lib_name
        self.books = list(args)
        books_dict = {'name': [], 'author': [], 'keyword': [], 'release_date': []}
        for book in self.books:
            books_dict['name'].append(book.name)
            books_dict['author'].append(book.author)
            books_dict['keyword'].append(book.keyword)
            books_dict['release_date'].append(book.release_date)
        self.df = pd.DataFrame(books_dict)
        libraries[lib_name] = self

    def save_csv(self) -> None:

        self.df.to_csv(f"{os.getcwd()}\\csv_files\\{self.lib_name}", sep=' ', index=False)

    def add(self, book: Book) -> None:
        self.df.loc[len(self.df.index)] = [book.name, book.author, book.keyword, book.release_date]

        self.save_csv()

    def delete_book(self, book_name: str) -> None:

        data_with_index = self.df.set_index("name")
        data_with_index = data_with_index.drop(book_name)

        self.save_csv()

    def edit(self, newbook: Book) -> None:

        row_index = self.df.loc[self.df['name'] == newbook.name].index[0]
        self.df.loc[row_index, 'author'] = newbook.author
        self.df.loc[row_index, 'keyword'] = newbook.keyword
        self.df.loc[row_index, 'release_date'] = newbook.release_date

        self.save_csv()

    def exists(self, name: str) -> bool:

        for ind in range(len(self.df)):
            if self.df.iloc[ind, 0] == name:
                return True
            else:
                return False

    def del_library(self, lib_name) -> None:
        os.remove(f"{os.getcwd()}\\csv_files\\{self.lib_name}")
        print("file deleted")
        del libraries[lib_name]
        print("file deleted from library dictionary")


def csv_to_lib(csvfile, name) -> Library:
    df = pd.read_csv(csvfile, sep=' ')
    books = []
    for ind in range(len(df)):
        books.append(Book((df.iloc[ind, 0]), (df.iloc[ind, 1]), (df.iloc[ind, 2]), (df.iloc[ind, 3])))
    books = tuple(books)
    return Library(name, *books)

# run
# book1 = Book('On the Origin of Species', 'Charles Darwin', 'akf', '1859')
# book2 = Book('Cosmos', 'Carl Sagan', 'acf', '1980')
# book3 = Book('The Selfish Gene', 'Richard Dawkin', 'csd', '1976')
# science_lib = Library('sci', book1, book2, book3)

# book4 = Book('Silent Spring', 'Rachel Carson', 'auf', '1962')
# science_lib.delete(book2)
# science_lib.delete(book3)
# book5 = Book('The Elegant Universe', 'Brian Greene', 'auk', '1999')
# science_lib.add(book5)
# book6 = Book('The Grand Design', 'Leonard Mlodinow', 'guk', '2010')
# science_lib.add(book6)
# book7 = Book('The Grand Design', 'Leonard Mlodinow', 'guk', '2016')
# science_lib.edit(book7)
# science_lib.del_library('sci')
# print(library_dicts)
