from suncraft_parsing import list_groups_as_string, name, description, meta_data, meta_name, part, upc


def read_it_all(imported_dict, body = "", all_cat = set(), all_subcat = set(), all_tags = set()):

    # This part is the body of the document and how it's formatted
    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        part_name_max_length = max([len(i) for i in part(imported_dict, pages_id, False)])
        product_page = "" # This holds the information for this loop don't remove it
        part_name_length = 0
        for i in part(imported_dict, pages_id, False):
            if len(i) > part_name_length:
                part_name_length = len(i)

        all_cat.update(list_groups_as_string(imported_dict, pages_id,"Categories", False))
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
            f'{name(imported_dict, pages_id)}\t' +\
            f'{", ".join(list_groups_as_string(imported_dict, pages_id, "Categories", False))}\t' +\
            f'{", ".join(list_groups_as_string(imported_dict, pages_id, "subcategories", False))}\t' +\
            f'{", ".join(list_groups_as_string(imported_dict, pages_id, "tags", False))}\t' +\
            f'{description(imported_dict, pages_id)}\t' +\
            f''
        
        for i in parts_dict:
            try:
                product_page += (f'{parts_dict[i]}\t{i}\t{meta_dict[i]}\t')
            except KeyError:
                product_page += (f'{parts_dict[i]}\t{i}\t')






        #     f'{name(imported_dict, pages_id)}\n' +\
        #     f'{line(30)}' +\
        #     f'{catsubtag_block(imported_dict, pages_id)}' +\
        #     f'{line(30)}' +\
        #     f'{description(imported_dict, pages_id)}\n' +\
        #     f'{line(30)}' +\
        #     f'| UPC | {str.center("Part", part_name_max_length)}|  Info\n' +\
        #     f'{admin_url(pages_id)}\n' +\
        #     f'{line(30)}' +\
        #     f''
        
        # for i in parts_dict:
        #     try:
        #         product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)} {meta_dict[i]}\n')
        #     except KeyError:
        #         product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)}\n')
                
        body += product_page 

    # body += "Categories: " + ", ".join(all_cat) + "\n"
    # body += "Subcategories: " + ", ".join(all_subcat) + "\n"
    # body += "Tags: " + ", ".join(all_tags) + "\n"

    return body
    # Creates and/or opens the file to work with.


# # Variables

