# data = "[伙食]2019/11/18 $50-早餐"
# step 1 : 擷取tag、date、cost
# 將一字串切兩半，不只可用一個字切，也可用一串字切。
# print(data.split("]")[0].split("[")[1])

# segment_1 = data.split("]")
# segment_2 = data.split("]")[0].split("[")
# tag = segment_2[1]
# segment_3 = segment_1[1].split(" $")
# date = segment_3[0]
# segment_4 = segment_1[1].split("-")
# cost = segment_4[1]
# print(tag, date, cost)

# ##Ctrl+Alt+L 可進行排版
# ##Ctrl+? 可加#

# 擷取日期跟花費
# print(data.split("]")[1].split(" ")[0])
# print(data.split(" ")[1].split(" $")[0])

# step 2 : 讀取全部資料
# 定義函式
# a: int = 10 可告訴python這是整數，下面text: str可告訴python此為字串
def get_tag_date_cost(text: str):
    segment_1 = text.split("]")
    segment_2 = segment_1[0].split("[")
    tag = segment_2[1]
    segment_3 = segment_1[1].split(" $")
    date = segment_3[0]
    segment_4 = segment_3[1].split("-")
    cost = segment_4[0]
    return tag, date, cost


# ./為相對路徑
f = open("./CostData.txt", encoding="UTF-8")
file_data_list = f.readlines()
# .append("a")可增加a到list中，.remove("b")可從List中移除b
# .index("c")可查詢c的號碼牌
dict_list = []
for d in file_data_list:
    if d != "\n":
        # .strip 可把最尾端的空白or換行符號刪掉
        d = d.strip()
        tag, date, cost = get_tag_date_cost(d)
        # print(f"標籤:{tag} 日期:{date} 花費:{cost}")
        # print("標籤:{} 日期:{} 花費:{}".format(tag, date, cost))

        # .pop("陳二")可拿掉dict中的陳二
        # del.("陳二")可拿掉dict中的陳二
        dict_list.append({"tag": tag, "date": date, "cost": cost})
print(dict_list)

# 查詢資料
# 總伙食花費
total_food_cost = 0
for t in dict_list:
    if t["tag"] == "伙食":
        # type可查詢型態
        # print(type(d["cost"]))
        total_food_cost += int(t["cost"])
print("五天伙食花費:", total_food_cost)

# 11/20的總花費
total_1120_cost = 0
for d in dict_list:
    if d["date"] == "2019/11/20":
        total_1120_cost += int(d["cost"])
print("11/20總花費:", total_1120_cost)

# 11/20的伙食總花費
total_1120_food_cost = 0
for dt in dict_list:
    if dt["date"] == "2019/11/20" and dt["tag"] == "伙食":
        total_1120_food_cost += int(dt["cost"])
print("11/20伙食總花費:", total_1120_food_cost)
