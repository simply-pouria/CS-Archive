import os.path
from utilities import csv_to_lib
from GUI import main_menu

for library in os.listdir(f'{os.getcwd()}\\csv_files'):
        
        basename = os.path.basename(f'{os.getcwd()}\\csv_files')
        csv_to_lib(basename, library)

main_menu()
