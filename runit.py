from read_it_csv_for_db_pages import read_it_csv_for_db_pages
from read_it_all import read_it_all
from read_it_filter import read_it_filter
from read_it_pictures import read_it_pictures
from suncraft_parsing import import_handeling, file_saving_tsv, file_saving_txt
from suncraft_varriables import suncraft_database_file 


def run_file_all():
    file_name_prefix = "all"
    imported_dict = import_handeling(suncraft_database_file, False)
    body = read_it_all(imported_dict)
    file_saving_txt(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
    return()
def run_file_csv():
    file_name_prefix = "csv_for_catalog"
    imported_dict = import_handeling(suncraft_database_file, False)
    body = read_it_csv_for_db_pages(imported_dict)
    file_saving_tsv(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
    return()
def run_file_filter():
    file_name_prefix = "filter"
    imported_dict = import_handeling(suncraft_database_file, False)
    body = read_it_filter(imported_dict)
    file_saving_txt(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
    return()
def run_file_pictures():
    file_name_prefix = "picture_list"
    imported_dict = import_handeling(suncraft_database_file, False)
    body = read_it_pictures(imported_dict)
    file_saving_txt(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
    return()



run_file_csv()