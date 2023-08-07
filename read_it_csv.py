from suncraft_parsing import list_groups_as_string, name, description, meta_data, meta_name, part, upc

def read_it_csv(imported_dict):
    # This part is the body of the document and how it's formatted
    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        product_page_list = list() # This holds the information for this loop don't remove it


        meta_name_list = meta_name(imported_dict, pages_id, False, "- ")
        meta_data_list = meta_data(imported_dict, pages_id, False)
        meta_dict = dict(zip(meta_name_list, meta_data_list))

        upc_list = upc(imported_dict, pages_id, False)
        part_list = part(imported_dict, pages_id, False)
        parts_dict = dict(zip(part_list, upc_list))


        #Page
        for i in parts_dict:
            product_page_list.append({"Page Name":name(imported_dict, pages_id),\
                    "Categories": ", ".join(list_groups_as_string(imported_dict, pages_id, "Categories", False)),\
                    "Subcategories": ", ".join(list_groups_as_string(imported_dict, pages_id, "subcategories", False)),\
                    "Tags":", ".join(list_groups_as_string(imported_dict, pages_id, "tags", False)),\
                    "Discription":description(imported_dict, pages_id),\
                    "UPC":parts_dict[i],\
                    "Part #":i,\
                    "Extra Info":meta_dict[i]\
                    })
        
    return product_page_list


