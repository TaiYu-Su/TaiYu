# step1：擷取 tag、date、cost、event
def get_tag_date_cost_event(text: str):
    segment_1 = text.split("]")
    segment_2 = segment_1[0].split("[")
    tag = segment_2[1]
    segment_3 = segment_1[1].split(" $")
    date = segment_3[0]
    segment_4 = segment_3[1].split("-")
    cost = segment_4[0]
    event = ""
    # 有 event 資料
    if len(segment_4) > 1:
        event = segment_4[1]
    return tag, date, cost, event

# step2：讀取全部資料
f = open("./data/CostData.txt", encoding="utf8")
file_data_list = f.readlines()

dict_list = []
for d in file_data_list:
    if d != "\n":
        d = d.strip()
        tag, date, cost, event = get_tag_date_cost_event(d)
        dict_list.append({"tag": tag, "date": date, "cost": cost,"event":event})
        # print("標籤:{} 日期:{} 花費:{}".format(tag, date, cost))
        # print(f"標籤:{tag} 日期:{date} 花費:{cost} 事件:{event}")

max_cost = 0
max_tag = ""
max_date = ""
max_event = ""

for d in dict_list:
    if d["event"] == "早餐":
        if int(d["cost"]) > max_cost:
            max_cost = int(d["cost"])
            max_tag = d["tag"]
            max_date = d["date"]
            max_event = d["event"]

print(f"[{max_tag}]{max_date} ${max_cost}-{max_event}")