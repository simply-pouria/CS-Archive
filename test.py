import pandas as pd
from utilities import Library, Book

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit',
                 'Aishwarya', 'Priyanka'],
        'Age': [21, 19, 20, 18],
        'Stream': ['Math', 'Commerce',
                   'Arts', 'Biology'],
        'Percentage': [88, 92, 95, 70]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age',
                                 'Stream',
                                 'Percentage'])

df.to_csv("test", header=False)

print("Given Dataframe :\n", df)

print("\nIterating over rows using loc function :\n")

# iterate through each row and select
# 'Name' and 'Age' column respectively.
# for i in range(len(df)):
#     print(df.loc[i, "Name"], df.loc[i, "Age"])
#
# print(df)
# print(df.loc[2, :])
# df = df.drop(index=2, axis=0)
# print(df)

def csv_to_lib(csvfile, name) -> Library:
    df = pd.read_csv(csvfile, sep=' ')
    books = []
    for ind in range(len(df)):
        # print(df.iloc[ind, 0], df.iloc[ind, 1], df.iloc[ind, 2], df.iloc[ind, 3])
        books.append(Book((df.iloc[ind, 0]), (df.iloc[ind, 1]), (df.iloc[ind, 2]), (df.iloc[ind, 3])))
    books = tuple(books)
    return Library(name, *books)


for i in range(len(df.index)):
    row = df.iloc[i, :]
    print(row.to_dict())




