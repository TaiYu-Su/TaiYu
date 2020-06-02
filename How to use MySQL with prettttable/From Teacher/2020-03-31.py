# import prettytable

# t=prettytable.PrettyTable(["Id","Title"], encoding="utf8")
# t.add_row(["1","AAA"])
# t.add_row(["2","BBB"])
# t.add_row(["3","CCC"])
# for i in range(1,10,1):
# 	t.add_row([i,"CCC"+str(i)])
# t.align["Id"]="r"
# t.align["Title"]="r"

# print(t)

# import colorama

# colorama.init(True)

# print("ABC")
# print(colorama.Style.BRIGHT+"ABC")
# print(colorama.Fore.RED+"ABC")
# print(colorama.Fore.GREEN+"ABC")
# print(colorama.Back.GREEN+"ABC")
import pymysql

link=pymysql.connect(
	host="localhost",
	user="root",
	passwd="",
	db="2020-03-31",
	charset="utf8"
)

c=link.cursor()

# param={
# 	"title":input("請輸入標題："),
# 	"source":input("請輸入新聞來源："),
# 	"create_date":input("請輸入發佈日期："),
# 	"description":input("請輸入新聞描述：")
# }

# c.execute(
# 	"INSERT INTO `news`(`title`,`source`,`create_date`,`description`) "+
# 	"VALUES(%(title)s,%(source)s,%(create_date)s,%(description)s);"
# ,param)
# link.commit()

# param={
# 	"id":input("請輸入你要修改的資料ID："),
# 	"title":input("請輸入標題："),
# 	"source":input("請輸入新聞來源："),
# 	"create_date":input("請輸入發佈日期："),
# 	"description":input("請輸入新聞描述：")
# }

# c.execute(
# 	"UPDATE `news` SET "+
# 	"`title`=%(title)s,`source`=%(source)s,`create_date`=%(create_date)s,`description`=%(description)s "+
# 	"WHERE `id`=%(id)s;"
# ,param)
# link.commit()


param={
	"id":input("請輸入你要刪除的資料ID：")
}

c.execute(
	"DELETE FROM `news` WHERE `id`=%(id)s;"
,param)
link.commit()


link.close()
