# 使用PySide2作為GUI介面

# import PySide2
from PySide2 import QtWidgets, QtGui, QtCore
import sys

# step 1: 創建一個QApp
app = QtWidgets.QApplication()

# 創建一張畫布
my_widget = QtWidgets.QWidget()
# 畫上去
my_widget.show()
#改變視窗標題
my_widget.setWindowTitle("範例程式")
# 設定初始視窗大小
my_widget.resize(256, 256)
# 限制視窗拖拉大小
# my_widget.setMinimumSize(102, 77)
# my_widget.setMaximumSize(1200, 900)

# 設定視窗固定大小
# my_widget.setFixedSize(256,256)

# 出現在特定座標並設置視窗大小
# my_widget.setGeometry(0,0,256,256)

my_label = QtWidgets.QLabel("0")
# my_label.setText("123")
# 指定要畫在畫布上的哪裡
my_label.setParent(my_widget)
my_label.show()
my_label.setGeometry(5, 10, 120, 50)
my_label.setStyleSheet("background-color: rgb(244, 200, 100)")

# 創建字體 (上面要import QtGui)
my_font = QtGui.QFont()
my_font.setPointSize(16)
# 設定字體
my_label.setFont(my_font)
# 設定Label置中，AlignHCenter是水平跟垂直都置中
my_label.setAlignment(QtCore.Qt.AlignCenter)

# 設置計數器
count = 0
def button_click():
    global count
    count += 1
    print(f"{count}")
    my_label.setText(str(count))

# 設置Button
my_button = QtWidgets.QPushButton("Press Me!!")
my_button.setParent(my_widget)
my_button.show()

# 串接Button事件，.clicked要加ed
my_button.clicked.connect(button_click)

# 變更按鈕位置
my_button.setGeometry(5, 60, 120, 20)

# 做一個計數器





# 執行app
sys.exit(app.exec_())






