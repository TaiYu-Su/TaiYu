import json

Concentration_Num = 0

with open("./空氣品質小時值_桃園市_中壢站.json", encoding="UTF-8") as file:
    # print(file.read())
    object_from_json = json.loads(file.read())
    # print(object_from_json)

    max_concentration = 0
    max_monitorDate = ""
    for i, d in enumerate(object_from_json):
        # print(i, d)
        if (d["ItemEngName"]) == "PM2.5":
            try:
                if float(d["Concentration"]) > max_concentration:
                    max_concentration = float(d["Concentration"])
                    max_monitorDate = d["MonitorDate"]
            except:
                print("資料錯誤", i, d)
    # print(f"時間 {max_monitorDate} 濃度 {max_concentration} 為最高")
