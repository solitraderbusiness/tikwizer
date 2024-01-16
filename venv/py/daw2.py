

# I wrote this script to help me with updating initializer files.




import os
import path_root
import json

path = path_root.get()
folder_path = path + "/contents/indicators/"
folder_list = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

for folder in folder_list:
    mpath = folder_path + folder + "/"
    with open(mpath + "initializer.json") as file:
        if file:
            text = file.read()
            dic = json.loads(text)
            init = dic.get("initializer")
            lines = init.split("\n")

            for i in range(len(lines)):
                lines[i] = lines[i] +"\n"

            mdic = {}
            mdic["initializer"] = dic.get("initializer")
            mdic["initializer_split"] = lines
            mdic["variable_name"] = dic.get("variable_name")
            print(json.dumps(mdic))
            # with open(mpath + "initializer.json", "w") as result_file:
            #     result_file.write( json.dumps(mdic))






# print(folder_list)









# with open(mpath + "class_template.json") as class_file:
#         if class_file:
#             class_txt = class_file.read()
#             class_template_dic = json.loads(class_txt)
