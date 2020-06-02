from PySide2 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication()

my_widget = QtWidgets.QWidget()
my_widget.show()
my_widget.setWindowTitle("記帳本")
my_widget.setFixedSize(400,600)

my_list = QtWidgets.QListWidget()
my_list.setParent(my_widget)
my_list.setGeometry(5, 300, 390, 295)
my_list.show()

# 新增
def add_item():
    my_list.addItem(button_date.text() + " " + button_category.text() + " " + "NTD$ " + button_amount.text() + " " + button_remark.text())

# 刪除
def remove_item():
    items = my_list.selectedItems()
    my_list.takeItem(my_list.row(items[0]))

my_font = QtGui.QFont()
my_font.setPointSize(16)

button_date = QtWidgets.QLineEdit()
button_date.setParent(my_widget)
button_date.setGeometry(10, 10, 180, 50)
button_date.show()
button_date.setPlaceholderText("記 帳 日 期")
button_date.setFont(my_font)
button_date.setAlignment(QtCore.Qt.AlignCenter)

button_category = QtWidgets.QLineEdit()
button_category.setParent(my_widget)
button_category.setGeometry(210, 10, 180, 50)
button_category.show()
button_category.setPlaceholderText("記 帳 類 別")
button_category.setFont(my_font)
button_category.setAlignment(QtCore.Qt.AlignCenter)

button_amount = QtWidgets.QLineEdit()
button_amount.setParent(my_widget)
button_amount.setGeometry(10, 80, 180, 50)
button_amount.show()
button_amount.setPlaceholderText("記 帳 金 額")
button_amount.setFont(my_font)
button_amount.setAlignment(QtCore.Qt.AlignCenter)

button_remark = QtWidgets.QLineEdit()
button_remark.setParent(my_widget)
button_remark.setGeometry(210, 80, 180, 50)
button_remark.show()
button_remark.setPlaceholderText("備 註")
button_remark.setFont(my_font)
button_remark.setAlignment(QtCore.Qt.AlignCenter)

button_add = QtWidgets.QPushButton("新增")
button_add.setParent(my_widget)
button_add.setGeometry(10, 220, 180, 50)
button_add.show()
button_add.clicked.connect(add_item)

button_remove = QtWidgets.QPushButton("刪除")
button_remove.setParent(my_widget)
button_remove.setGeometry(210, 220, 180, 50)
button_remove.show()
button_remove.clicked.connect(remove_item)

sys.exit(app.exec_())

