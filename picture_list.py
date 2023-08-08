import os
import glob

path = "/Users/LisaH/Library/CloudStorage/GoogleDrive-lisah@suncraftind.com/My Drive/Product Pics All Sources/Product Images Sorted"
dir_list = glob.glob(f"{path}/**/*.*")

for i in dir_list:
#    file = 
    print(i.split("/")[-1])

# final_list = list()
# for i in dir_list:
#     print(i)
#     file_list = os.listdir(i)
#     for i in file_list:
#         print(i)

