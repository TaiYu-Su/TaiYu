import csv
def get_location_data_list(file_path, location):
    result_list = []
    with open(file_path, encoding = "UTF-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == location:
                result_list.append(row)
    return result_list

result_list = []
result_list += get_location_data_list("./Data/自來水水質抽驗結果(106年1月).csv", "平鎮區")
result_list += get_location_data_list("./Data/自來水水質抽驗結果(106年2月).csv", "平鎮區")
result_list += get_location_data_list("./Data/自來水水質抽驗結果(106年3月).csv", "平鎮區")

with open("./search_summary_list.csv", "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    for row in result_list:
        writer.writerow(row)