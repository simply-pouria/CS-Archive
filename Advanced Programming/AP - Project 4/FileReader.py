# Pouria Moradpour 4024023040

import os
import pandas as pd

# just to have indexes for the category_index column of our dataframe
category_index = {"Art": 1, "Politics": 2, "Science": 3, "Sport": 4}


# to handle the data we need to add to the dataframe
class FileData:

    def __init__(self, directory_name: str, file_number: str) -> None:

        self.directory_name = directory_name
        self.file_number = file_number

        path = f"{os.getcwd()}\\{self.directory_name}\\{self.file_number}"

        with open(f"{path}", "r") as file:
            self.text = file.read()

    # generates a complete single row of the dataframe
    def get_row(self):

        return {"file_index": self.file_number, "text": self.text,
                "category_name": self.directory_name, "category_index": category_index[self.directory_name]}


def fill_dataframe(df: pd.DataFrame):

    for directory in os.listdir(os.getcwd()):

        # this statement is here to prevent indexing unwanted directories such as ipynb checkpoints, Pycharm .idea,
        # venv, etc
        if directory in category_index.keys():

            for file in os.listdir(f"{os.getcwd()}\\{directory}"):

                data = FileData(directory, file)
                df.loc[len(df.index)] = data.get_row()







