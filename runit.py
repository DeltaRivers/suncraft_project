from read_it_csv import read_it_csv
from read_it_all import read_it_all
from read_it_filter import read_it_filter
from suncraft_parsing import import_handeling, file_saving_tsv, file_saving_txt
from suncraft_varriables import suncraft_database_file 

def run_file_all():
    file_name_prefix = "all"
    imported_dict = import_handeling(suncraft_database_file, False)
    body = read_it_all(imported_dict)
    file_saving_txt(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
    return()
def run_file_csv():
    file_name_prefix = "csv"
    imported_dict = import_handeling(suncraft_database_file, False)
    body = read_it_csv(imported_dict)
    file_saving_tsv(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
    return()
def run_file_filter():
    file_name_prefix = "filter"
    imported_dict = import_handeling(suncraft_database_file, False)
    body = read_it_filter(imported_dict)
    file_saving_txt(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
    return()



run_file_filter()