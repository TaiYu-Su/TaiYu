from PySide2 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication()

my_widget = QtWidgets.QWidget()
my_widget.show()

my_input_field = QtWidgets.QLineEdit()
my_input_field.setParent(my_widget)
my_input_field.setGeometry(5, 5, 100, 20)
my_input_field.show()
# 設定成密碼模式
my_input_field.setEchoMode(QtWidgets.QLineEdit.Password)
# 設定提示文字
my_input_field.setPlaceholderText("password")

# 取得輸入的值
def get_value():
    print(my_input_field.text())

my_button = QtWidgets.QPushButton("取值")
my_button.setParent(my_widget)
my_button.setGeometry(5, 27, 100, 20)
my_button.show()
my_button.clicked.connect(get_value)

sys.exit(app.exec_())

