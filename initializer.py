import os
from utilities import csv_to_lib
from GUI import main_menu

for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        csv_file_name = os.path.basename(library)
        lib_name = csv_file_name.removesuffix('.csv')
        csv_to_lib(library, library)

main_menu()