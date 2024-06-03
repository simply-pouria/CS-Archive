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
    def __init__(self , lib_name: str, *args : Book):
        self.lib_name = lib_name
        self.books = list(args)
        self.books_dict = {'name':[] , 'author': [],'keyword': [],'release_date': []}
        for book in self.books:
            self.books_dict['name'].append(book.name)
            self.books_dict['author'].append(book.author)
            self.books_dict['keyword'].append(book.keyword)
            self.books_dict['release_date'].append(book.release_date)
        df = pd.DataFrame(self.books_dict)
                        
    def to_csv(self):
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
            if df.iloc[ind, 0] == book.name:
                self.books_dict['name'].remove(book.name)
                self.books_dict['author'].remove(book.author)
                self.books_dict['keyword'].remove(book.keyword)
                self.books_dict['release_date'].remove(book.release_date)
                
                print('The book is deleted')
        new_df = pd.DataFrame(self.books_dict)
        new_df.to_csv('library.csv', index=False)    
    
    def edit(self, oldbook : Book , newbook : Book):
        # delete the current book
        df = pd.DataFrame(self.books_dict)
        for ind in range(len(df)):
            if df.iloc[ind, 0] == newbook.name:
                self.books_dict['name'].remove(oldbook.name)
                self.books_dict['author'].remove(oldbook.author)
                self.books_dict['keyword'].remove(oldbook.keyword)
                self.books_dict['release_date'].remove(oldbook.release_date)
        
                # add the new book
        self.books_dict['name'].append(newbook.name)        
        self.books_dict['author'].append(newbook.author)
        self.books_dict['keyword'].append(newbook.keyword)
        self.books_dict['release_date'].append(newbook.release_date)
        new_df = pd.DataFrame(self.books_dict)
        new_df.to_csv('library.csv', sep='-', index=False)  

    def exists(self, name : str):
         df = pd.DataFrame(self.books_dict)
         for ind in range(len(df)):
            if df.iloc[ind, 0] == name:
                return True
            else:
                return False
            
def csv_to_lib(csvfile,name):
        df = pd.read_csv(csvfile,sep='-')
        books = []
        for ind in range(len(df)):
            
            books.append(Book((df.iloc[ind,0]),(df.iloc[ind,1]),(df.iloc[ind,2]),(df.iloc[ind,3])))
        books = tuple(books)
        return Library(name,*books)


# run
book1 = Book('On the Origin of Species', 'Charles Darwin','akf','1859')
book2 = Book('Cosmos', 'Carl Sagan','acf','1980')
book3 = Book('The Selfish Gene', 'Richard Dawkin','csd','1976')
science_lib = Library('sci', book1, book2, book3)
science_lib.to_csv()
book4 = Book('Silent Spring', 'Rachel Carson','auf','1962')
science_lib.delete(book2)
science_lib.delete(book3)
book5 = Book('The Elegant Universe', 'Brian Greene','auk','1999')
science_lib.add(book5)
book6 = Book('The Grand Design', 'Leonard Mlodinow','guk','2010')
science_lib.add(book6)
book7 = Book('The Grand Design', 'Leonard Mlodinow','guk','2016')
science_lib.edit(book6,book7)
csv_to_lib('library.csv','lib')