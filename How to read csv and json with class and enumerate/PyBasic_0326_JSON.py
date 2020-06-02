import json

with open("./data.json", encoding="utf8") as file:
    # print(file.read())
    object_from_json = json.loads(file.read())
    for s in object_from_json:
        print(f"{s['name']} 分數：{s['scores'][2]}")

# data = [
#     {"name": "張三", "id": 1},
#     {"name": "李四", "id": 2}
# ]
#
# json_from_data = json.dumps(data, ensure_ascii=False)
# print(f"從物件來的字串：{json_from_data}")
# with open("from_python.json", "w", encoding="utf8") as file:
#     file.write(json_from_data)
