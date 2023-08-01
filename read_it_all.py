from suncraft_parsing import items_block, live_url, admin_url, import_handeling, catsubtag_block, tags, subcat, cat, name, description, sort_rank, string_it, file_saving, meta_data, meta_name, meta_name2, part, upc
from suncraft_varriables import suncraft_database_file, looking_for, type_of_group

# Variables
file_name_prefix = "all"
imported_dict = import_handeling(suncraft_database_file, False)
body = ""
all_cat = set()
all_subcat = set()
all_tags = set()


# This part is the body of the document and how it's formatted
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    product_page = "" # This holds the information for this loop don't remove it
    

    meta_name_list = meta_name2(imported_dict, pages_id, False, "- .")
    meta_data_list = meta_data(imported_dict, pages_id, False)
    meta_dict = dict(zip(meta_name_list, meta_data_list))

    upc_list = upc(imported_dict, pages_id, False)
    part_list = part(imported_dict, pages_id, False)
    parts_dict = dict(zip(part_list, upc_list))

    all_cat.update(cat(imported_dict, pages_id, False))
    all_subcat.update(subcat(imported_dict, pages_id, False))
    all_tags.update(tags(imported_dict, pages_id, False))

    #Page
    product_page += ("=" * 30) + "\n"
    product_page += f'{name(imported_dict, pages_id)}\n'
    product_page += ("=" * 30) + "\n"
    product_page += catsubtag_block(imported_dict, pages_id)
    product_page += ("=" * 30) + "\n"
    product_page += description(imported_dict, pages_id) + "\n"
    product_page += ("-" * 30) + "\n"
    xx = 0
    for i in part(imported_dict, pages_id, False):
        if len(i) > xx:
            xx = len(i)
    product_page += f'| UPC | {str.center("Part", xx)}|  Info\n'
    product_page += ("-" * 30) + "\n"

    for i in parts_dict:
        try:
            product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", xx + 1)} {meta_dict[i]}\n')
        except KeyError:
            product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", xx + 1)}\n')


    product_page += f'\n'
    body += product_page 

body += "Categories: " + string_it(all_cat) + "\n"
body += "Subcategories: " + string_it(all_subcat) + "\n"
body += "Tags: " + string_it(all_tags) + "\n"


# Creates and/or opens the file to work with.
file_saving(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)




