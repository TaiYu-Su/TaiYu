def get_tag_date_cost_item(text: str):
    segment_1 = text.split("]")
    segment_2 = segment_1[0].split("[")
    tag = segment_2[1]
    segment_3 = segment_1[1].split(" $")
    date = segment_3[0]
    segment_4 = segment_3[1].split("-")
    cost = segment_4[0]
    item = ""
    # 判別是否有註記的資料
    if len(segment_4) > 1:
        item = segment_4[1]
    return tag, date, cost, item

f = open("./CostData.txt", encoding="UTF-8")
file_data_list = f.readlines()
dict_list = []
for d in file_data_list:
    if d != "\n":
        d = d.strip()
        tag, date, cost, item = get_tag_date_cost_item(d)
        dict_list.append({"tag": tag, "date": date, "cost": cost, "item": item})
        # print(f"標籤:{tag} 日期:{date} 花費:{cost} 事件:{item}")
# print(dict_list)

# 找出早餐最高的花費
max_cost = 0
max_tag = ""
max_date = ""
max_item = ""
for d in dict_list:
    if d["item"] == "早餐":
        if int(d["cost"]) > max_cost:
            max_cost = int(d["cost"])
            max_tag = d["tag"]
            max_date = d["date"]
            max_item = d["item"]
# print(max_cost)
print(f"[{max_tag}]{max_date} ${max_cost}-{max_item}")