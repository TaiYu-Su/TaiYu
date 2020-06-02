from PySide2 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication()

my_widget = QtWidgets.QWidget()
my_widget.show()

# 列表的顯示
my_list = QtWidgets.QListWidget()
my_list.setParent(my_widget)
my_list.show()

# 輸入列表
index = 0
def add_item():
    global index
    my_list.addItem(f"內容 : {index}")
    index += 1

# 刪除列表
def remove_item():
    items = my_list.selectedItems()
    # 找出點選的item是第幾列，並刪除第幾列的第一個號碼排
    my_list.takeItem(my_list.row(items[0]))


button_add = QtWidgets.QPushButton("新增")
button_add.setParent(my_widget)
button_add.setGeometry(20, 200, 100, 20)
button_add.show()
button_add.clicked.connect(add_item)

button_remove = QtWidgets.QPushButton("刪除")
button_remove.setParent(my_widget)
button_remove.setGeometry(125, 200, 100, 20)
button_remove.show()
button_remove.clicked.connect(remove_item)

sys.exit(app.exec_())

