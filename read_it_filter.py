from suncraft_parsing import items_block, live_url, admin_url, import_handeling, catsubtag_block, tags, subcat, cat, name, description, sort_rank, string_it
from suncraft_varriables import suncraft_database_file, looking_for, type_of_group

# Variables
parsed_file_name = "filter"
imported_dict = import_handeling(suncraft_database_file, False)

body = ""
all_cat = set()
all_subcat = set()
all_tags = set()

# This part is the body of the document and how it's formatted
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    product_page = "" # This holds the information for this loop don't remove it
    
    if type_of_group == "category":
        this_group = cat(imported_dict, pages_id, False)
    if type_of_group == "subcategory":
        this_group = subcat(imported_dict, pages_id, False)
    if type_of_group == "tag":
        this_group = tags(imported_dict, pages_id, False)

    for i in looking_for:
        any_of_these = i

        if any_of_these in this_group:
                all_cat.update(cat(imported_dict, pages_id, False))
                all_subcat.update(subcat(imported_dict, pages_id, False))
                all_tags.update(tags(imported_dict, pages_id, False))

                #Page
                product_page += f'{name(imported_dict, pages_id)}\n'
                product_page += f'{imported_dict[pages_id]["slug_product"]}\n'
                product_page += f'{sort_rank(imported_dict, pages_id)}\n'
                product_page += f'{admin_url(pages_id)}\n'
                product_page += f'{live_url(imported_dict, pages_id)}\n'
                product_page += f'\n'
    

    body += product_page 
body += "Categories: " + string_it(all_cat) + "\n"
body += "Subcategories: " + string_it(all_subcat) + "\n"
body += "Tags: " + string_it(all_tags) + "\n"


# Creates and/or opens the file to work with.
write_to_this_file = f'{parsed_file_name}_{suncraft_database_file.split(".")[0]}.txt'
working_file = open(write_to_this_file, "w")
working_file.write(body)
working_file.close()
print(f'\nDone: {write_to_this_file} has been saved\n')


