# 定義資料結構
class data:
    def __init__(self, tag, date, cost: int, event):
        self.tag = tag
        self.date = date
        self.cost = cost
        self.event = event
    def print_info(self):
        print(f"[{self.tag}]{self.date} ${self.cost}-{self.event}")

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
f = open("./CostData.txt", encoding="utf8")
file_data_list = f.readlines()

receipt_list = []
for d in file_data_list:
    if d != "\n":
        d = d.strip()
        tag, date, cost, event = get_tag_date_cost_event(d)
        # 創建 Receipt 並放入 receipt_list 中。
        r = Receipt(tag, date, int(cost), event)
        receipt_list.append(r)


max_receipt: Receipt = receipt_list[0]
for r in receipt_list:
    if r.event == "早餐":
        if r.cost > max_receipt.cost:
            max_receipt = r
# print(max_receipt.tag)
# print(max_receipt.date)
# print(max_receipt.cost)
# print(max_receipt.event)
max_receipt.print_info()

# print(f"[{max_receipt.tag}]{max_receipt.date} ${max_receipt.cost}-{max_receipt.event}")
