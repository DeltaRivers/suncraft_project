from json import load
import traceback
from titles_and_formatting import pretty_title

def string_it(s):
    string = ""
    for i in s:
        string += i + ", "
    string = string[:-2]
    return string
def admin_url(id):
    url = "https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/" + id
    return url
def live_url(id):
    url = "https://suncraftind.com/catalog/" + imported_dict[id]["slug_product"]
    return url
def cat(id):
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
def subcat(id):
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
def tags(id):
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
        output += f'| {items["upc_color"]} | {items["part_number"]}\n'
    output += ("-" * 19) + "\n\n"
    return output

# Variables
parsed_file_name = "report"
inputloop = False # If you want to input the file in terminal set inputloop to true
suncraft_database_file = "SClist_2023_07_17_08:13AM.json" # Otherwise, place the proper file here
not_found_tries = 0
attempts_other_error = 3

big_line = "=" * 19
cat_subcat_header = "     Category      |      Sub Category    "
upc_header = pretty_title("  UPC  |  Part   ", "-")

# Creates and opens the file to work with.
write_to_this_file = f'{parsed_file_name}_{suncraft_database_file.split(".")[0]}.txt'
working_file = open(write_to_this_file, "w")
body = ""

# File input handeling.
if inputloop is False:
    imported_dict = load(open(suncraft_database_file))
while inputloop:
    try:
        suncraft_database_file = input("Enter File To Parse: ")
        imported_dict = load(open(suncraft_database_file))

    except FileNotFoundError:
        # Ways to exit the loop
        if suncraft_database_file in ["quit", "exit", "end", "q"]:
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

# This part is the body of the document and how it's formatted NOW WITH FUNCTIONS!!!
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    product_page = "" # This holds the information for this loop
    name = imported_dict[pages_id]["name_product"]
    description = imported_dict[pages_id]["description"]

    #Title
    product_page += f'{big_line}\n{name}\n\nAdmin URL --> {admin_url(pages_id)}\nAdmin URL --> {live_url(pages_id)}\n{big_line}\n'
    # Discription
    product_page += f'\n{description}\n\n'
    # Categories
    product_page += cat(pages_id)
    # Subcategories
    product_page += subcat(pages_id)
    # Tags
    product_page += tags(pages_id)
    #items UPC | Part
    product_page += upc_header
    product_page += items_block(pages_id)

    body += product_page # Adds the loop to the body

# Writes and closes the file and indicates that the task is compleate
working_file.write(body)
working_file.close()
print(f'\nDone: {write_to_this_file} has been saved\n')


