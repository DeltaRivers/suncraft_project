from suncraft_parsing import items_block, live_url, admin_url, import_handeling, catsubtag_block, tags, subcat, cat, name, description, sort_rank, string_it, file_saving, meta_data, meta_name
from suncraft_varriables import suncraft_database_file, looking_for, type_of_group

# Variables
file_name_prefix = "filter"
imported_dict = import_handeling(suncraft_database_file, False)
body = ""
all_cat = set()
all_subcat = set()
all_tags = set()

# This part is the body of the document and how it's formatted
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    product_page = "" # This holds the information for this loop don't remove it
    
    meta_dict = {meta_name(imported_dict, pages_id):meta_data(imported_dict, pages_id)}


    all_cat.update(cat(imported_dict, pages_id, False))
    all_subcat.update(subcat(imported_dict, pages_id, False))
    all_tags.update(tags(imported_dict, pages_id, False))

    #Page
    product_page += f'{name(imported_dict, pages_id)}\n'
    product_page += ""



    product_page += f'\n'
    

    body += product_page 

body += "Categories: " + string_it(all_cat) + "\n"
body += "Subcategories: " + string_it(all_subcat) + "\n"
body += "Tags: " + string_it(all_tags) + "\n"


# Creates and/or opens the file to work with.
file_saving(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)




