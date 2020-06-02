from PySide2 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication()

my_widget = QtWidgets.QWidget()
my_widget.resize(256,256)
my_widget.show()
my_widget.setWindowTitle("我的應用程式")

# 設定應用程式的 Icon
my_icon = QtGui.QIcon("./記帳圖示.png")
my_widget.setWindowIcon(my_icon)

# 放圖片(將圖片設計成一個元件)
my_pixmap = QtGui.QPixmap("./記帳圖示.jpg")
# 顯示圖片大小
# print(my_pixmap.size())

# 縮放label
my_label = QtWidgets.QLabel()
my_label.setPixmap(my_pixmap.scaled(128, 128))
my_label.setParent(my_widget)
my_label.show()

def on_click():
    print("click!")

# 設定按鈕
my_button = QtWidgets.QPushButton()
my_button.setIcon(QtGui.QIcon(my_icon))
my_button.setParent(my_widget)
my_button.setGeometry(0, 130, 128, 128)
my_button.show()
my_button.clicked.connect(on_click)
# 調整Icon大小
my_button.setIconSize(QtCore.QSize(100, 100))

# 將程式打包，需要先安裝PyInstaller
# pip install PyInstaller
# 在Terminal執行pyinstaller會出現使用方式
# 在Terminal輸入pyinstaller -F -w PyBasic_0406_GUI4.py，之後可以在資料夾中找到dist資料夾，執行檔就在裡面
# 如果沒有-F，會變成一個資料夾裡面很多檔案，而不是一個.exe執行檔
# -F後面加上-w，可以讓程式執行時，不會多一個terminal視窗，以避免讓使用者知道我們debug的方式
# 如果有此程式有關聯其他檔案，例如圖片、音樂，需要將關聯檔案與.exe執行檔放在同一個dist資料夾，這樣圖示才會顯示

sys.exit(app.exec_())

# print(score_dictionary["王五"])