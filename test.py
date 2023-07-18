from suncraft_varriables import test_import
from json import load
from suncraft_parsing import upc, admin_url, part, file_saving, meta_data, meta_name

imported_dict = load(open("SClist_2023_07_18_02:22PM.json"))
body = ""
meta_dict = {}

for id in imported_dict:
        
    meta_dict[meta_name(imported_dict, id)] = meta_data(imported_dict, id)

    for i in meta_dict:
        body += f'{i, meta_dict[i]} \n'

file_saving("test", body)


