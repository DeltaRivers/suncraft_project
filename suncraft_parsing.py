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

def live_url(id, imported_dict):
    url = "https://suncraftind.com/catalog/" + imported_dict[id]["slug_product"]
    return url

def cat(id, imported_dict):
    counter = 0
    listed = []
    try:
        for i in imported_dict[id]["Categories"]["data"]:
            listed.append(imported_dict[id]["Categories"]["data"][counter]["attributes"]["name_category"])
            counter += 1
    except Exception as error:
        output = error

    output = f"Category: {string_it(listed)}\n"
    return output

def subcat(id, imported_dict):
    counter = 0
    listed = []
    try:
        for i in imported_dict[id]["subcategories"]["data"]:
            listed.append(imported_dict[id]["subcategories"]["data"][counter]["attributes"]["name"])
            counter += 1
    except Exception as error:
        output = error

    output = f"Subcategory: {string_it(listed)}\n"
    return output

def tags(id, imported_dict):
    counter = 0
    listed = []
    try:
        for i in imported_dict[id]["tags"]["data"]:
            listed.append(imported_dict[id]["tags"]["data"][counter]["attributes"]["name"])
            counter += 1
    except Exception as error:
        output = error

    output = f"Tags: {string_it(listed)}\n"
    return output

def items_block(id, imported_dict):
    output = ""
    for items in imported_dict[id]["Colors"]:
        output += f' {items["upc_color"]} | {items["part_number"]}\n'
    output += ("-" * 18) + "\n\n"
    return output

def file_handeling(dict_file = str, inputloop = False):
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

def catsubtag_block(id, imported_dict):
    output = f"   {cat(id, imported_dict)}{subcat(id, imported_dict)}       {tags(id, imported_dict)}"
    return output
