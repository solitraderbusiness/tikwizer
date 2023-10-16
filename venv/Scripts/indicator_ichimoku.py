import json

path="G:/fxDreema/venv/contents"

input_dic = {}
with open(path+"/ichimoku/input.json") as input_file:
    if input_file:
        input_txt = input_file.read()
        input_dic = json.loads(input_txt)

class_template_dic = {}
with open(path+"/ichimoku/class_template.json") as class_file:
    if class_file:
        class_txt = class_file.read()
        class_template_dic = json.loads(class_txt)

field_body_dic = {}
with open(path+"/ichimoku/field_body.json") as field_file:
    if field_file:
        field_txt = field_file.read()
        field_body_dic = json.loads(field_txt)

fun_body_dic = {}
with open(path+"/ichimoku/fun_body.json") as fun_file:
    if fun_file:
        fun_txt = fun_file.read()
        fun_body_dic = json.loads(fun_txt)

fun_body_dic = {}
with open(path+"/ichimoku/fun_body.json") as fun_file:
    if fun_file:
        fun_txt = fun_file.read()
        fun_body_dic = json.loads(fun_txt)

init_body_dic = {}
with open(path+"/ichimoku/init_body.json") as init_file:
    if init_file:
        init_txt = init_file.read()
        init_body_dic = json.loads(init_txt)

for key in input_dic:
    init_body_dic["init_body"] = init_body_dic.get("init_body").replace(key + "_val", str(input_dic.get(key)))

mql4_body = class_template_dic.get("class_template") \
    .replace("field_body", field_body_dic.get("field_body")) \
    .replace("init_body", init_body_dic.get("init_body")) \
    .replace("fun_body", fun_body_dic.get("fun_body")) \
    .replace("field_body", field_body_dic.get("field_body"))

mql4_json = {}
mql4_json["mql4_body"] = mql4_body

print(mql4_json.get("mql4_body"))

with open(path+"/ichimoku/mql4_ichimoku.mq4", "w") as result_file:
    result_file.write(mql4_body)




