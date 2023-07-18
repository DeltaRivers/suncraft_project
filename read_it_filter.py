from suncraft_parsing import items_block, live_url, admin_url, file_handeling, catsubtag_block, tags, subcat, cat

# Variables
parsed_file_name = "filter"
suncraft_database_file = "SClist_2023_07_17_06:07PM.json"
imported_dict = file_handeling(suncraft_database_file, False)
line_length = 18
big_line = "=" * line_length + "\n"
small_line = "-" * line_length + "\n"
upc_header = f"  UPC  |  Part   \n{small_line}"
body = ""
all_cat = set()
all_subcat = set()
all_tags = set()

# Creates and opens the file to work with.
write_to_this_file = f'{parsed_file_name}_{suncraft_database_file.split(".")[0]}.txt'
working_file = open(write_to_this_file, "w")



# This part is the body of the document and how it's formatted
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    product_page = "" # This holds the information for this loop
    name = imported_dict[pages_id]["name_product"]
    description = imported_dict[pages_id]["description"]
    
    for i in ["mb", "MB"]:
        any_of_these = i

    if any_of_these in name:
        all_cat.update(cat(imported_dict, pages_id, False))
        all_subcat.update(subcat(imported_dict, pages_id, False))
        all_tags.update(tags(imported_dict, pages_id, False))

        #Title
        product_page += f'    {name}\n{big_line}{catsubtag_block(imported_dict, pages_id)}{big_line}\n'     #\nAdmin URL --> {admin_url(pages_id)}\nAdmin URL --> {live_url(pages_id, imported_dict)}\n
        # Discription
        product_page += f'{description}\n\n'
        # items UPC | Part
        product_page += upc_header + items_block(imported_dict, pages_id) + small_line + "\n"
        body += product_page 

# Writes and closes the file and indicates that the task is compleate
working_file.write(body)
working_file.close()
print(f'\nDone: {write_to_this_file} has been saved\n')


