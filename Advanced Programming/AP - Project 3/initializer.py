import os.path
from utilities import Library, Book
from GUI import main_menu
import pandas as pd


for library in os.listdir(f'{os.getcwd()}\\csv_files'):

    books = []
    df = pd.read_csv(f'{os.getcwd()}\\csv_files\\{library}', sep=' ')

    for i in range(len(df.index)):
        row = df.iloc[i, :].to_dict()
        print(row)
        books.append(Book(name=row['name'], author=row['author'], keyword=row['keyword'], release_date=row['release_date']))

    print(library)

    Library(library, *books)

main_menu()
