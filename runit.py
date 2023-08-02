from read_it_all import read_it_all
from suncraft_parsing import import_handeling, file_saving
from suncraft_varriables import suncraft_database_file

file_name_prefix = "all"
imported_dict = import_handeling(suncraft_database_file, False)
body = read_it_all(imported_dict)
file_saving(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)
