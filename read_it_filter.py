from suncraft_parsing import items_block, live_url, admin_url, import_handeling, catsubtag_block, tags, subcat, cat

# Variables
parsed_file_name = "filter"
suncraft_database_file = "SClist_2023_07_31_12:09PM.json"
imported_dict = import_handeling(suncraft_database_file, False)
line_length = 18
big_line = "=" * line_length + "\n"
small_line = "-" * line_length + "\n"
upc_header = f"  UPC  |  Part   \n{small_line}"
body = ""
all_cat = set()
all_subcat = set()
all_tags = set()



# This part is the body of the document and how it's formatted
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    product_page = "" # This holds the information for this loop don't remove it

    name = imported_dict[pages_id]["name_product"]
    description = imported_dict[pages_id]["description"]
    catagory = cat(imported_dict, pages_id, False)
    url = live_url(imported_dict, pages_id)
    a_url = admin_url(pages_id)

    for i in ["Glass Vessels"]:
        any_of_these = i

        if any_of_these in catagory:
                all_cat.update(cat(imported_dict, pages_id, False))
                all_subcat.update(subcat(imported_dict, pages_id, False))
                all_tags.update(tags(imported_dict, pages_id, False))

                #Page
                product_page += f'{name}\n'
#                product_page += f'{imported_dict[pages_id]["slug_product"]}\n'
                product_page += f'{imported_dict[pages_id]["rank"]}\n'
                product_page += f'{a_url}\n'
                product_page += f'{url}\n'
                product_page += f'\n'

    body += product_page 

# Creates and/or opens the file to work with.
write_to_this_file = f'{parsed_file_name}_{suncraft_database_file.split(".")[0]}.txt'
working_file = open(write_to_this_file, "w")
working_file.write(body)
working_file.close()
print(f'\nDone: {write_to_this_file} has been saved\n')


