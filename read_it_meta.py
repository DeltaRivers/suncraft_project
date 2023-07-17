from json import load
from pprint import pprint
import csv
from titles_and_formatting import pretty_title, underline, overline


suncraft_database_file = None
parsed_file_name = "Meta"
not_found_tries = 0
admin_url = "https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/" # + page_id


# Checks that the file is found, and opens it if it is. 
while suncraft_database_file == None:
    try:
#        suncraft_database_file = input("Enter File To Parse: ")
        suncraft_database_file = "SClist_2023_07_05_09:09AM.json"
        imported_dict = load(open(suncraft_database_file))

    except FileNotFoundError:
        # Ways to exit the loop
        if suncraft_database_file in ["quit", "exit", "end", "q"]:
            exit()

        print("File not found.")

        # If too many mistakes are made, the program will quit:
        if not_found_tries == 2:
            print("Make sure you spelled it correctly, it's case sensitive.")
        if not_found_tries == 3:
            print("Make sure you include the extention")
        if not_found_tries == 4:
            print("But don't include the path, just put it in the working directory.")
        if not_found_tries == 5:
            print("I got nothing else for ya.")
        if not_found_tries == 6:
            print("Go check your file name and that it's where you think it is and come back to try again.")
            exit()
            
        not_found_tries += 1

        # Resets the file name
        suncraft_database_file = None

    except:
        attempts = 3
        print("Something else went wrong")
        if attempts > 0:
            print(f"{attempts} tries remaining")
            attempts -= 1
        else:
            exit()
        
# Creates and opens the file to work with.
write_to_this_file = f"{parsed_file_name}_{suncraft_database_file.split('.')[0]}.txt"
working_file = open(write_to_this_file, "w")

# This part is the body of the document and how it's formatted

for pages_id in imported_dict:

    #Title
    working_file.write(f"\n======\n{imported_dict[pages_id]['name_product']}   --> Admin URL: https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/{pages_id}\n======\n")

    # Extra Info
    for meta_list in imported_dict[pages_id]["Meta"]:
        
        if meta_list['name'][0] not in [" ", "-"]:
            print(imported_dict[pages_id]["Meta"][meta_list]['name'])
                #working_file.write(f"{meta_list['name']} : {meta_list['value']} \n")




# Closes the file and indicates that the task is compleate
working_file.close()
print(f"\nDone\n{write_to_this_file} has been saved")



### Saved Code of checking for non dashed meta.
"""
for pages_id in imported_list:

    try:
        if imported_list[pages_id]["Meta"][0]["name"][0] not in [" ", "-"]:

            #Title
            working_file.write(f"\n======\n{imported_list[pages_id]['name_product']}   --> Admin URL: https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/{pages_id}\n======\n")

            # Extra Info
            for Meta in imported_list[pages_id]["Meta"]:
                
                working_file.write(f"{Meta['name']}\n")
    except IndexError:
                    #Title
            working_file.write(f"\n======\n{imported_list[pages_id]['name_product']}   --> Admin URL: https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/{pages_id}\n======\n" + \
                               "NO META AVAILABE\n")


"""