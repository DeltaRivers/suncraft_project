import glob

def get_pic_files_dict(\
                        path_to_folders = "/Users/LisaH/Library/CloudStorage/GoogleDrive-lisah@suncraftind.com/My Drive/Product Pics All Sources/Product Images Sorted",\
                        path_more = "/**/*.*"):
    dir_list = glob.glob(path_to_folders + path_more)
    files_dict = dict()

    for i in dir_list:
        files_dict[i.split("/")[-1].split("_")[0]] = i
    return(files_dict)


