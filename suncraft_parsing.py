from json import load
import traceback

def string_it(s):
    string = ""
    for i in s:
        string += i + ", "
    string = string[:-2]
    return string

def admin_url(id):
    url = "https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/" + id
    return url

def live_url(imported_dict, id, string = True):
    url = "https://suncraftind.com/catalog/" + imported_dict[id]["slug_product"]
    return url

def cat(imported_dict, id, string = True):
    counter = 0
    listed = []
    try:
        for i in imported_dict[id]["Categories"]["data"]:
            listed.append(imported_dict[id]["Categories"]["data"][counter]["attributes"]["name_category"])
            counter += 1
        if string:
            output = f"Categories: {string_it(listed)}\n"
        else:
            output = listed

    except Exception as error:
        print(error)
        output = "Error\n"
    return output

def subcat(imported_dict, id, string = True):
    counter = 0
    listed = []
    try:
        for i in imported_dict[id]["subcategories"]["data"]:
            listed.append(imported_dict[id]["subcategories"]["data"][counter]["attributes"]["name"])
            counter += 1
        if string:
            output = f"Subcategores: {string_it(listed)}\n"
        else:
            output = listed

    except Exception as error:
        print(error)
        output = "Error\n"
    return output

def tags(imported_dict, id, string = True):
    counter = 0
    listed = []
    try:
        for i in imported_dict[id]["tags"]["data"]:
            listed.append(imported_dict[id]["tags"]["data"][counter]["attributes"]["name"])
            counter += 1
        if string:
            output = f"Tags: {string_it(listed)}\n"
        else:
            output = listed

    except Exception as error:
        print(error)
        output = "Error\n"
    return output

def items_block(imported_dict, id:str):
    output = ""
    for items in imported_dict[id]["Colors"]:
        output += f' {items["upc_color"]} | {items["part_number"]}\n'
    return output

def part(imported_dict, id, string = True):
    listed = []
    for items in imported_dict[id]["Colors"]:
        listed.append(f'{items["part_number"]}')
    if string:
        output = f"{string_it(listed)}\n"
    else:
        output = listed
    return output

def upc(imported_dict, id, string = True):
    listed = []
    for items in imported_dict[id]["Colors"]:
        listed.append(f'{items["upc_color"]}')
    if string:
        output = f"{string_it(listed)}\n"
    else:
        output = listed
    return output

def import_handeling(dict_file = str, inputloop = False):
    attempts_other_error = 3
    not_found_tries = 0
    if inputloop is False:
        imported_dict = load(open(dict_file))
    while inputloop:
        try:
            dict_file = input("Enter File To Parse: ")
            imported_dict = load(open(dict_file))

        except FileNotFoundError:
            # Ways to exit the loop
            if dict_file in ["quit", "exit", "end", "q"]:
                exit()

            print("\nFile not found.")

            # If too many mistakes are made, the program will quit:
            if not_found_tries == 1:
                print("Make sure you spelled it correctly, it's case sensitive.\n")
            if not_found_tries == 2:
                print("Make sure you include the extention\n")
            if not_found_tries == 3:
                print("But don't include the path, just put it in the working directory.\n")
            if not_found_tries == 4:
                print("I got nothing else for ya.\n")
            if not_found_tries == 5:
                print("Go check your file name and that it's where you think it is and come back to try again.\n")
                exit()
                
            not_found_tries += 1

        except Exception as error:
            print("Something else went wrong")
            traceback.print_exc()
            if attempts_other_error > 0:
                print(f"{attempts_other_error} tries remaining")
                attempts_other_error -= 1
            else:
                exit()
    return imported_dict

def catsubtag_block(imported_dict, id):
    output = f"  {cat(imported_dict, id)}{subcat(imported_dict, id)}        {tags(imported_dict, id)}"
    return output

def file_saving(filename:str, body:str):
    working_file = open(f'{filename}.txt', "w")
    working_file.write(body)
    working_file.close()
    print(f'\nDone: {filename}.txt has been saved\n')

def meta_name(imported_dict, id, string = True):
    listed = []
    for items in imported_dict[id]["Meta"]:
        listed.append(f'{items["name"]}')
    if string:
        output = f"{string_it(listed)}\n"
    else:
        output = listed
    return output

def meta_data(imported_dict, id, string = True,):
    listed = []
    for items in imported_dict[id]["Meta"]:
        listed.append(f'{items["value"]}')
    if string:
        output = f"{string_it(listed)}\n"
    else:
        output = listed
    return output
