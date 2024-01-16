
import os
import path_root

path = path_root.get()
folder_path = path + "/contents/indicators/"
folder_list = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

for folder in folder_list:
    mpath = folder_path + folder

    print(mpath)


# print(folder_list)









# with open(mpath + "class_template.json") as class_file:
#         if class_file:
#             class_txt = class_file.read()
#             class_template_dic = json.loads(class_txt)
