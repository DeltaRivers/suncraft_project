from suncraft_parsing import list_groups_as_string, name, description, meta_data, meta_name, part, upc, hex_to_color_name_dict, color_hex

def read_it_csv_for_db_pages(imported_dict):
    product_page_list = list() # This holds the information for this loop don't remove it

    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):

        meta_name_list = meta_name(imported_dict, pages_id, False, "- ")
        meta_data_list = meta_data(imported_dict, pages_id, False)
        meta_dict = dict(zip(meta_name_list, meta_data_list))

        upc_list = upc(imported_dict, pages_id, False)
        part_list = part(imported_dict, pages_id, False)
        parts_dict = dict(zip(part_list, upc_list))
        color_list_hex = color_hex(imported_dict, pages_id)

        #Page
        product_page_list.append({
                "Page Name":name(imported_dict, pages_id),
                "Categories": ", ".join(list_groups_as_string(imported_dict, pages_id, "cat", False)),
                "Subcategories": ", ".join(list_groups_as_string(imported_dict, pages_id, "sub", False)),
                "Tags":", ".join(list_groups_as_string(imported_dict, pages_id, "tag", False)),
                "Discription":description(imported_dict, pages_id),
                "UPC list":",".join(upc_list),
                "Part # list":",".join(part_list),
                "Extra Info list":",".join(meta_data_list),
                "color":""
                })
        
    return product_page_list


