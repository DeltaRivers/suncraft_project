import re
from suncraft_varriables import test_import
from json import load
from suncraft_parsing import upc, admin_url, part, file_saving, meta_data, meta_name

imported_dict = load(open("SClist_2023_07_18_02:22PM.json"))
body = ""
meta_dict = {}
meta_dict_partkeys = {}

for pages_id in imported_dict:
    counter = 0
    for i in imported_dict[pages_id]["Meta"]:
        meta_dict[imported_dict[pages_id]["Meta"][counter]["name"]] = imported_dict[pages_id]["Meta"][counter]["value"]
        counter += 1

for i in meta_dict:
    meta_dict_partkeys[re.sub("[- ]", "", i)] = meta_dict[i]

for pages_id in imported_dict:
    name = imported_dict[pages_id]["name_product"]
    counter = 0
    block = ""
    page_parts = part(imported_dict, pages_id, False)
    page_upcs = upc(imported_dict, pages_id, False)
    longest = 0

    for i in page_parts:
        if len(i) > longest:
            longest = len(i)

    for i in page_parts:
        try:
            block += f'{page_upcs[counter]} | {i}{" " * (longest - len(i))} | {meta_dict_partkeys[i]} \n'
        except KeyError:
            block += f'{page_upcs[counter]} | {i}{" " * (longest - len(i))} |\n'
        counter += 1

    body += f'{name}\n{block}\n\n'
        
file_saving("test", body)


