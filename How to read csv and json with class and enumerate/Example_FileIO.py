# 使用"w"可以寫入資料
# f = open("data.txt", "w", encoding="UTF-8")
# user_input = input("請輸入文字 : ")
# f.write(user_input)

# with 可在使用完畢後自動關閉程式
with open("data.txt", "a", encoding="UTF-8") as file:
    user_input = input("請輸入文字 : ")
    file.write(user_input + "\n")
