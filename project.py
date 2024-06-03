from os import name
from numpy import delete
import pandas as pd

class Book:
    def __init__(self, name: str, author: str, keyword: str, release_date: str):
        self.name = name
        self.author = author
        self.keyword = keyword
        self.release_date = release_date

    def edit_name(self,  name: str):
        self.name = name

    def edit_author(self,  author: str):
        self.author = author

    def edit_keyword(self,  keyword: str):
        self.keyword = keyword

    def edit_release_date(self,  release_date: str):
        self.release_date = release_date


class Library:
    def __init__(self, lib_name: str, *args : Book):
        self. lib_name = lib_name
        self.books = list(args)
        self.books_dict = {'name':[] , 'author': [],'keyword': [],'release_date': []}
        for book in self.books:
            self.books_dict['name'].append(book.name)
            self.books_dict['author'].append(book.author)
            self.books_dict['keyword'].append(book.keyword)
            self.books_dict['release_date'].append(book.release_date)
        df = pd.DataFrame(self.books_dict)
        df.to_csv('library.csv',sep='-', index=False)  
    
    def add(self, book : Book):
    
        self.books_dict['name'].append(book.name)
        self.books_dict['author'].append(book.author)
        self.books_dict['keyword'].append(book.keyword)
        self.books_dict['release_date'].append(book.release_date)
        df = pd.DataFrame(self.books_dict)
        df.to_csv('library.csv', index=False)  

    def delete(self, book : Book):
        df = pd.DataFrame(self.books_dict)
        for ind in range(len(df)):
            if self.df.iloc[ind, 0] == book.name:
                self.df.drop([ind])

    def edit(self, book : Book):
        # delete the current book
        for ind in self.range(len(self.df)):
            if self.df.iloc[ind, 0] == book.name:
                self.df.drop([ind])
                # add the new book
                self.books_dict['name'].append(book.name)
                self.books_dict['author'].append(book.author)
                self.books_dict['keyword'].append(book.keyword)
                self.books_dict['release_date'].append(Book.release_date)
                df = pd.DataFrame(self.books_dict)
                df.to_csv('library.csv', sep='-', index=False)  

                

    def exists(self, book : Book):
         for ind in self.range(len(self.df)):
            if self.df.iloc[ind, 0] == book.name:
                return True
            else:
                return False


book1 = Book('On the Origin of Species', 'Charles Darwin','akf','1859')
book2 = Book('Cosmos', 'Carl Sagan','acf','1980')
book3 = Book('The Selfish Gene', 'Richard Dawkin','csd','1976')
science_lib = Library('sci', book1, book2, book3)
book4 = Book(name='Silent Spring', author='Rachel Carson',keyword='auf',release_date='1962')
science_lib.delete(book4)




        
        
        