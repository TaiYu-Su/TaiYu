# step0 : 定義資料結構
class Receipt:
    def __init__(self, tag, date, cost: int, event):
        self.tag = tag
        self.date = date
        self.cost = cost
        self.event = event

    def print_info(self):
        print(f"[{self.tag}]{self.date} ${self.cost}-{self.event}")


# step1：擷取 tag、date、cost、event 的函式
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
f.close()

# step3 : 使用者輸入
search_tag = input("請輸入 tag : ")

# step4 : 查詢資料
receipt_list = []
for i, d in enumerate(file_data_list):
    if d != "\n":
        d = d.strip()
        # 分析資料
        try:
            tag, date, cost, event = get_tag_date_cost_event(d)
            r = Receipt(tag, date, int(cost), event)
        except:
            print(f"第 {i+1} 筆，發生錯誤 : {d}")
        receipt_list.append(r)

# 創建結果的串列
result_receipt_list = []

# 搜尋所有收據，如果等於查詢的 tag ，就放入搜尋結果的list。
for r in receipt_list:
    if r.tag == search_tag:
        result_receipt_list.append(r)
# 印出搜尋結果
total_cost_in_sesult = 0
for r in result_receipt_list:
    total_cost_in_sesult += r.cost
# 印出平均花費
try:
    print(total_cost_in_sesult / len(result_receipt_list))
except ZeroDivisionError:
    print(f"沒有查到 {search_tag} 此tag資料。")
