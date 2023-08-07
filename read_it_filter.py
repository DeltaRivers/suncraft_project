from suncraft_parsing import admin_url, upc, part, line, meta_name, meta_data, import_handeling, catsubtag_block, list_groups_as_string, name, description, file_saving_txt
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
    part_name_max_length = max([len(i) for i in part(imported_dict, pages_id, False)])
    this_group = list_groups_as_string(imported_dict,pages_id,type_of_group,False)

    for i in looking_for:
        any_of_these = i

        if any_of_these in this_group:
            all_cat.update(list_groups_as_string(imported_dict, pages_id,"Categories",False))
            all_subcat.update(list_groups_as_string(imported_dict, pages_id,"subcategories", False))
            all_tags.update(list_groups_as_string(imported_dict, pages_id,"tags", False))

            meta_name_list = meta_name(imported_dict, pages_id, False, "- ")
            meta_data_list = meta_data(imported_dict, pages_id, False)
            meta_dict = dict(zip(meta_name_list, meta_data_list))


            upc_list = upc(imported_dict, pages_id, False)
            part_list = part(imported_dict, pages_id, False)
            parts_dict = dict(zip(part_list, upc_list))

                #Page
            product_page += \
                f'{name(imported_dict, pages_id)}\n' +\
                f'{line(30)}' +\
                f'{catsubtag_block(imported_dict, pages_id)}' +\
                f'{line(30)}' +\
                f'{description(imported_dict, pages_id)}\n' +\
                f'{line(30)}' +\
                f'| UPC | {str.center("Part", part_name_max_length)}|  Info\n' +\
                f'{admin_url(pages_id)}\n' +\
                f'{line(30)}' +\
                f''
            
            for i in parts_dict:
                try:
                    product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)} {meta_dict[i]}\n')
                except KeyError:
                    product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)}\n')

    body += product_page 
# body += "Categories: " + string_it(all_cat) + "\n"
# body += "Subcategories: " + string_it(all_subcat) + "\n"
# body += "Tags: " + string_it(all_tags) + "\n"


# Creates and/or opens the file to work with.
file_saving_txt(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)




