# name = input("請輸入名字: ")
# # print(f"您好, {name}")

# Error Handling
try:
    num1 = input("請輸入數值1: ")
    num2 = input("請輸入數值2: ")
    print(int(num1) + int(num2))
except ValueError:
    print("請輸入數值。")
except FileNotFoundError:
    pass
except:
    print("發生錯誤!")

print("123")