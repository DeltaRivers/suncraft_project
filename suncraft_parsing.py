from json import load
import traceback, re, csv, glob


def admin_url(id):
    url = "https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/" + id
    return url

def live_url(imported_dict, id, string = True):
    url = "https://suncraftind.com/catalog/" + imported_dict[id]["slug_product"]
    return url

def list_groups_as_string(imported_dict, id, kind, string = True):
    if kind in ["cat", "c", "categories", "Categories", "category", "Category"]:
        group_type = "Categories"
    elif kind in ["sub", "s", "subcategories", "Subcategories", "Subcategory", "subcategory"]:
        group_type = "subcategories"
    elif kind in ["tag", "t", "tags", "Tags", "Tag"]:
        group_type = "tags"

    counter = 0
    listed = []
    key_for_name = "name_category" if group_type == "Categories" else "name"
    try:
        for i in imported_dict[id][group_type]["data"]:
            listed.append(imported_dict[id][group_type]["data"][counter]["attributes"][key_for_name])
            counter += 1
        if string:
            output = f'{group_type}: {" ".join(listed)}\n'
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
        output = " ".join(listed) + "\n"
    else:
        output = listed
    return output

def upc(imported_dict, id, string = True):
    listed = []
    for items in imported_dict[id]["Colors"]:
        listed.append(f'{items["upc_color"]}')
    if string:
        output = f" ".join(listed) + "\n"
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
    output = f'   {list_groups_as_string(imported_dict, id,"Categories")}{list_groups_as_string(imported_dict, id, "subcategories")}         {list_groups_as_string(imported_dict, id,"tags")}'
    return output

def file_saving_txt(filename:str, body:str):
    working_file = open(f'{filename}.txt', "w")
    working_file.write(body)
    working_file.close()
    print(f'\nDone: {filename}.txt has been saved\n')

def file_saving_tsv(filename:str, dict_list:list):
    with open(f'{filename}.tsv', "w", newline="") as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter="\t")
        header = dict_list[0].keys()
        tsv_writer.writerow(header)
        for row in dict_list:
            tsv_writer.writerow(row.values())
    print(f'\nDone: {filename} has been saved\n')

def meta_name(imported_dict, id, string = True, remove = '', replace_with = ''):
    listed = [str(i["name"]) for i in imported_dict[id]["Meta"]]
    re_pattern = "*".join(list(remove)) + "*"
    clean_list = [re.sub(re_pattern,replace_with,i) for i in listed]
    return " ".join(clean_list) + "\n" if string else clean_list

def meta_data(imported_dict, id, string = True,):
    listed = [i["value"] for i in imported_dict[id]["Meta"]]      
    return " ".join(listed) + "\n" if string else listed

def name(imported_dict, id):
    output = imported_dict[id]["name_product"]
    return output

def description(imported_dict, id):
    output = imported_dict[id]["description"]
    return output

def sort_rank(imported_dict, id):
    output = f'{imported_dict[id]["rank"]}\n'
    return output

def line(number, segment = "-"):
    return (segment * number) + "\n"

def get_pic_files_dict(\
                        path_to_folders = "/Users/LisaH/Library/CloudStorage/GoogleDrive-lisah@suncraftind.com/My Drive/Product Pics All Sources/Product Images Sorted",\
                        path_more = "/**/*.*"):
    dir_list = glob.glob(path_to_folders + path_more)
    files_dict = dict()

    for i in dir_list:
        files_dict[i.split("/")[-1].split("_")[0]] = i
    return(files_dict)

