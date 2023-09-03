from suncraft_parsing import  meta_data


def read_it_test(imported_dict):
    breakpoint()
    body = ""

    # This for loop sorts the product pages in "rank" order
    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        product_page = "" # This holds the information for this loop don't remove it
        meta_data(imported_dict, pages_id, False)

    body += product_page

    return body






