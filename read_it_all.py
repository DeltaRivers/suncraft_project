from suncraft_parsing import color_hex, list_groups_as_string, name, description, meta_data, meta_name, part, upc, catsubtag_block, line, admin_url, hex_to_color_name_dict
import re

def read_it_all(imported_dict):
    body = ""
    all_cat = set()
    all_subcat = set()
    all_tags = set()

    number_of_parts_list = list()
    counts = dict()

    # This for loop sorts the product pages in "rank" order
    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        product_page = "" # This holds the information for this loop don't remove it

        #Just for formatting later
        part_name_max_length = max([len(i) for i in part(imported_dict, pages_id, False)])

        # Updating the "all_lists"
        all_cat.update(list_groups_as_string(imported_dict, pages_id,"cat", False))
        all_subcat.update(list_groups_as_string(imported_dict, pages_id,"sub", False))
        all_tags.update(list_groups_as_string(imported_dict, pages_id,"tag", False))

        # Making dicts of these things - may make this a function later
        parts_dict = dict(zip(part(imported_dict, pages_id, False), upc(imported_dict, pages_id, False)))
        upc_dict = dict(zip(upc(imported_dict, pages_id, False), part(imported_dict, pages_id, False)))

        meta_dict = dict(zip(meta_name(imported_dict, pages_id, False, "- "), meta_data(imported_dict, pages_id, False)))
        color_dict = dict(zip(upc(imported_dict, pages_id, False), color_hex(imported_dict, pages_id, False)))


        #The actual page formatting
        #product_page += \
            # f'\n\n{name(imported_dict, pages_id)}' + f'   -> {admin_url(pages_id)}\n' 
        no = ""
        for i in parts_dict: # i is the part number
                try:
                    if hex_to_color_name_dict[str.lower(color_dict[parts_dict[i]])] in ["Chrome", "Nickel", "Bronze", "Brass", "Black", "White"] \
                        and hex_to_color_name_dict[str.lower(color_dict[parts_dict[i]])] not in str(re.sub("[,.)(]", "", meta_dict[i])).split(" "):

                        product_page += (f'|{str.rjust(parts_dict[i], 5)}| {str.rjust(meta_dict[i], 60)} | {hex_to_color_name_dict[str.lower(color_dict[parts_dict[i]])]} {admin_url(pages_id)}\n')
                except KeyError:
                    product_page += (f'{color_dict[parts_dict[i]]} | {parts_dict[i]} -> {admin_url(pages_id)}\n')
                    print(name(imported_dict, pages_id))
        body += product_page

    # Lists of all the cat-sub-tags for when this is used in a filtered version.
    # body += "Categories: " + ", ".join(all_cat) + "\n"
    # body += "Subcategories: " + ", ".join(all_subcat) + "\n"
    # body += "Tags: " + ", ".join(all_tags) + "\n"
    # all_list = list(all_cat) + list(all_subcat) + list(all_tags)
    # body += str(all_list)
    

    return body






#I'ma just keep this down here out of the way for a bit
        # product_page += \
        #     f'\n\n{name(imported_dict, pages_id)}' + f'   -> {admin_url(pages_id)}\n' +\
        #     f'{line(30)}' +\
        #     f'{catsubtag_block(imported_dict, pages_id)}' +\
        #     f'{line(30)}' +\
        #     f'{description(imported_dict, pages_id)}\n' +\
        #     f'{line(30)}' +\
        #     f'| UPC | {str.center("Part", part_name_max_length)}|  Info\n' +\
        #     f'{line(30)}' +\
        #     f''
        # for i in parts_dict:
        #     try:
        #         product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)} {meta_dict[i]}\n')
        #     except KeyError:
        #         product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_max_length + 1)}\n')
