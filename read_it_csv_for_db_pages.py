from suncraft_parsing import list_groups_as_string, name, description, meta_data, meta_name, part, upc, hex_to_color_name_dict, color_hex

def read_it_csv_for_db_pages(imported_dict):
    product_page_list = list() # This holds the information for this loop don't remove it

    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        parts_list = part(imported_dict, pages_id, False)

        try:
            parts_list.remove("====")
        except ValueError:
            parts_list = parts_list
            

        m_partnumber_to_m_data_dict = dict(zip(meta_name(imported_dict, pages_id, False, "- "), meta_data(imported_dict, pages_id, False)))
        for i in parts_list:
            data_list = m_partnumber_to_m_data_dict[i]

        c_partnumber_to_c_upc_dict = dict(zip(part(imported_dict, pages_id, False), upc(imported_dict, pages_id, False)))
        
        c_partnumber_to_c_hex_dict = dict(zip(part(imported_dict, pages_id, False), color_hex(imported_dict, pages_id, False)))



        #Page
        product_page_list.append({
                "Page Name":name(imported_dict, pages_id),
                "Categories": ", ".join(list_groups_as_string(imported_dict, pages_id, "cat", False)),
                "Subcategories": ", ".join(list_groups_as_string(imported_dict, pages_id, "sub", False)),
                "Tags":", ".join(list_groups_as_string(imported_dict, pages_id, "tag", False)),
                "Discription":description(imported_dict, pages_id),
                "UPC list":",".join(),
                "Part # list":",".join(parts_list),
                "Extra Info list":",".join(data_list),
                "color":""
                })
        
    return product_page_list


