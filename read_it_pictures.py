from suncraft_parsing import admin_url, upc, part, line, meta_name, meta_data, catsubtag_block, list_groups_as_string, name, description, get_pic_files_dict
from suncraft_varriables import looking_for, type_of_group

def read_it_pictures(imported_dict):
    body = ""
    all_cat = set()
    all_subcat = set()
    all_tags = set()
    most_pics = get_pic_files_dict()

    # This part is the body of the document and how it's formatted
    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        product_page = "" # This holds the information for this loop don't remove it

        part_name_max_length = 20 #max([len(i) for i in part(imported_dict, pages_id, False)])
        this_group = list_groups_as_string(imported_dict,pages_id,type_of_group,False)

        for i in looking_for:
            any_of_these = i

            if any_of_these in this_group:
                all_cat.update(list_groups_as_string(imported_dict, pages_id,"cat",False))
                all_subcat.update(list_groups_as_string(imported_dict, pages_id,"sub", False))
                all_tags.update(list_groups_as_string(imported_dict, pages_id,"tag", False))
                meta_name_list = meta_name(imported_dict, pages_id, False, "- ")
                meta_data_list = meta_data(imported_dict, pages_id, False)
                meta_dict = dict(zip(meta_name_list, meta_data_list))
                upc_list = upc(imported_dict, pages_id, False)
                part_list = part(imported_dict, pages_id, False)
                parts_dict = dict(zip(part_list, upc_list))
                

                    #Page
                product_page += \
                    f''
                    # f'{name(imported_dict, pages_id)}' +\
                    # f'   --> {admin_url(pages_id)}\n' +\
                
                #UPC Part Meta Block
                for i in parts_dict:
                    try:
                        nothing = (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)} {most_pics[parts_dict[i]]}\n')
                    except KeyError:
                        product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)} Find file for --> {[parts_dict[i]]}\n')

        body += product_page + ""
    return(body)




