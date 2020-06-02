import os
# 拿到資料夾內的所有內容
# print(os.listdir("./Data"))
# 找到上一層路徑有哪些資料
# print(os.listdir("../"))

# 如何拿到某個物件的資料夾路徑
# file_path = "C:/Users/lenovo/PycharmProjects/Python0330/Data/自來水水質抽驗結果(106年1月).csn"
# print(os.path.dirname(file_path))
# print(os.listdir(os.path.dirname(file_path)))

# 檢查物件或資料夾是否存在
# print(os.path.exists("./Q3_16.py"))
# print(os.path.exists("./Data"))
# print(os.path.exists("./Data123"))

# 創建資料夾
# os.mkdir("./資料夾")
# os.mkdir("./FromPython")

# open無法創建資料夾，需先檢查資料夾是否存在
# 如果沒有，就創建一個資料夾
# step 1: 拿到檔案路徑

# step 2: 確認此資料夾是否存在
# print(os.path.exists("os.path.dirname(file_path)"))

# step 3: 如果沒有，就創建一個資料夾
# file_path = "./Data123/file.txt"
# file_dir_path = os.path.dirname(file_path)
# if not os.path.exists(file_dir_path):
#     os.mkdir(file_dir_path)

# 如果有相同的副檔名，就加上-1、-2...
# index = 1
# while os.path.exists(file_path):
#     file_path = f"./Data123/file-{index}.txt"
#     index += 1
#
# with open(file_path, "w", encoding = "UTF-8") as file:
#     pass

# 重新命名檔案
# os.rename("./output.csv", "./output_1.csv")
# os.rename("./test", "./test123")

# 剪下、貼上 => 更改檔名到不同的資料夾
# os.rename("./Data/自來水水質抽驗結果(106年1月).csv", "自來水水質抽驗結果(106年1月).csv")

# 刪除檔案 (要特別注意無法在資源回收桶裡找到，已被永久刪除)
# os.remove("./test123/__init__.py")

# 刪除資料夾
# os.mkdir(("./test"))
# os.rmdir("./test")

# 讀取資料夾內的亂數檔名，並改成特定檔名
# step 1: 讀取資料夾內的檔案
# step 2: 改名字 -> Data-1、Data-2...
#
# index = 1
# for r in os.listdir("./dataset"):
#     os.rename("./dataset/" + r, f"./dataset/Data-{index}.txt")
#     index += 1

import glob
# 找到特定開頭的檔案
# print(glob.glob("out*"))
# 找到特定結尾(副檔名)的檔案
# print(glob.glob("*csv"))
# 找到特定開頭與特定結尾的檔案
# print(glob.glob("./dataset/Data*.txt"))
