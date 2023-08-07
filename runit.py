from read_it_csv import read_it_csv
from suncraft_parsing import import_handeling, file_saving_tsv 
from suncraft_varriables import suncraft_database_file 

file_name_prefix = "tsv_of"
imported_dict = import_handeling(suncraft_database_file, False)
body = read_it_csv(imported_dict)
file_saving_tsv(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
