from varables import test_import
from json import load
from suncraft_parsing import upc, admin_url, part

body = ""

imported_dict = load(open("SClist_2023_07_18_02:15PM.json"))

url_set = set()

for id in imported_dict:
    l = part(imported_dict, id, False)
    for i in l:
        if " " in i:
            url_set.add(admin_url(id))
            
for i in url_set:
    body += i + "\n"

write_to_this_file = f'Test_output.txt'
working_file = open(write_to_this_file, "w")
working_file.write(body)
working_file.close()
print(f'\nDone: {write_to_this_file} has been saved\n')

