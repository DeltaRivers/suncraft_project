from suncraft_parsing import list_groups_as_string, name, description, meta_data, meta_name, part, upc, catsubtag_block, line, admin_url


def read_it_all(imported_dict):
    body = ""
    all_cat = set()
    all_subcat = set()
    all_tags = set()

    # This for loop sorts the product pages in "rank" order
    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        product_page = "" # This holds the information for this loop don't remove it

        #Just for formatting later
        part_name_max_length = max([len(i) for i in part(imported_dict, pages_id, False)])
        part_name_length = 0
        for i in part(imported_dict, pages_id, False):
            if len(i) > part_name_length:
                part_name_length = len(i)

        # Updating the "all_lists"
        all_cat.update(list_groups_as_string(imported_dict, pages_id,"cat", False))
        all_subcat.update(list_groups_as_string(imported_dict, pages_id,"sub", False))
        all_tags.update(list_groups_as_string(imported_dict, pages_id,"tag", False))

        # Making and Zipping the parts and meta dict for the combined parts block - may make this a function later
        meta_name_list = meta_name(imported_dict, pages_id, False, "- ")
        meta_data_list = meta_data(imported_dict, pages_id, False)
        meta_dict = dict(zip(meta_name_list, meta_data_list))
        upc_list = upc(imported_dict, pages_id, False)
        part_list = part(imported_dict, pages_id, False)
        parts_dict = dict(zip(part_list, upc_list))


        #The actual page formatting
        product_page += \
            f'\n\n{name(imported_dict, pages_id)}' +\
            f'   -> {admin_url(pages_id)}\n' +\
            f'{line(30)}' +\
            f'{catsubtag_block(imported_dict, pages_id)}' +\
            f'{line(30)}' +\
            f'{description(imported_dict, pages_id)}\n' +\
            f'{line(30)}' +\
            f'| UPC | {str.center("Part", part_name_max_length)}|  Info\n' +\
            f'{line(30)}' +\
            f''
        
        for i in parts_dict:
            try:
                product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)} {meta_dict[i]}\n')
            except KeyError:
                product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)}\n')
                
        # body += product_page 
        
# Lists of all the cat-sub-tags for when this is used in a filtered version.
    # body += "Categories: " + ", ".join(all_cat) + "\n"
    # body += "Subcategories: " + ", ".join(all_subcat) + "\n"
    # body += "Tags: " + ", ".join(all_tags) + "\n"
    all_list = list(all_cat) + list(all_subcat) + list(all_tags)
    body += str(all_list)
    return body



