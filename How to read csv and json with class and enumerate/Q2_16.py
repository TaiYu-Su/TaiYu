import csv

search_unit = input("請輸入欲查詢機關名稱 : ")

with open("opendata_requests.csv", encoding="UTF-8") as file:
    reader = csv.reader(file)
    search_unit_list = []
    first_row = []
    try:
       # search_unit = input("請輸入欲查詢機關名稱 : ")
        for i, d in enumerate(reader):
            if i == 0:
                first_row = d
            if d[0] == search_unit:
                search_unit_list.append(d)
        if len(search_unit_list) == 0:
            print(f"找不到 {search_unit} 此單位。")
        with open(f"{search_unit}_search_unit_list.csv", "w", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(first_row)
            for r in search_unit_list:
                writer.writerow(r)
    except:
        print(f"找不到 {search_unit} 此單位。")
