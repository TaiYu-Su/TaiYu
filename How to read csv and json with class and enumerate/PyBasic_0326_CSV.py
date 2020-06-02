import csv
#
# max_download_count = 0
# max_download_name = ""
#
# with open("opendata_requests.csv", encoding="UTF-8") as file:
#     reader = csv.reader(file)
#     for i, row in enumerate(reader):
#         if i != 0:
#             count = int(row[3].replace(",", ""))
#             if count > max_download_count:
#                 max_download_count = count
#                 max_download_name = row[1]
#     print(f"最高下載次數: {max_download_count} 是{max_download_name}")

# with open("opendata_requests.csv", encoding="UTF-8") as file:
#     rows = csv.DictReader(file)
#     for row in rows:
#         print(row["下載次數"].replace(",", ""))

with open("./output.csv", "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["班級", "座號", "分數"])
    writer.writerow(["A30", "1", "99"])
    writer.writerow(["A30", "2", "60"])