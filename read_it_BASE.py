from json import load


# Variables
admin_url = "https://admin.suncraftind.com/dashboard/content-manager/collectionType/api::product.product/" # + page_id
live_url = "https://suncraftind.com/catalog/" # + slug_product
parsed_file_name = "repoort"
not_found_tries = 0

# File input handeling
# If you want to input the file in terminal set inputloop to true.
# Otherwise, place the proper file in suncraft_database_file
inputloop = False
suncraft_database_file = "SClist_2023_06_26_04:35PM.json"

if inputloop is False:
    imported_dict = load(open(suncraft_database_file))

# Checks that the file is found, and opens it if it is. 
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

    except:
        attempts = 3
        print("Something else went wrong")
        if attempts > 0:
            print(f"{attempts} tries remaining")
            attempts -= 1
        else:
            exit()
    

# Creates and opens the file to work with.
write_to_this_file = f'{parsed_file_name}_{suncraft_database_file.split(".")[0]}.txt'
working_file = open(write_to_this_file, "w")

# This part is the body of the document and how it's formatted
# This sorts the by rank
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):

    #Title
    working_file.write("\n\n" + ("=" * 19) + "\n" +\
                       f'{imported_dict[pages_id]["name_product"]}\n' +\
                       ("=" * 19) + "\n")
#                       f"Admin URL  -->  {admin_url}{pages_id}\n" +\
#                       f"Live URL   -->  {live_url}{pages_id}\n" +\
#                        ("-" * 25) + "\n")

    # Discription
    working_file.write(f'\n{imported_dict[pages_id]["description"]}\n\n')

    # working_file = The file you are writing
    # imported_dict = The json file you imported
    # pages_id = the ID number of each product page

   


   
   


# Closes the file and indicates that the task is compleate
working_file.close()
print(f'\nDone\n{write_to_this_file} has been saved\n')



