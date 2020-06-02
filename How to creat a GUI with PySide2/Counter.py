from PySide2 import QtWidgets, QtGui, QtCore

class QCounter(QtWidgets.QWidget):
    def __init__(self):
        super(QCounter, self).__init__()

        self.count = 0

        self.label_count = QtWidgets.QLabel("0")
        self.label_count.setParent(self)
        self.label_count.show()
        self.label_count.setGeometry(5, 5, 120, 50)
        self.label_count.setStyleSheet("background-color: rgb(244, 200, 100)")
        self.font_label = QtGui.QFont()
        self.font_label.setPointSize(16)
        self.label_count.setFont(self.font_label)
        self.label_count.setAlignment(QtCore.Qt.AlignCenter)

        self.button_add_one = QtWidgets.QPushButton("Press Me!!")
        self.button_add_one.setParent(self)
        self.button_add_one.show()
        self.button_add_one.setGeometry(5, 60, 120, 20)
        self.button_add_one.clicked.connect(self.add_one)

    def add_one(self):
        self.count += 1
        self.label_count.setText(str(self.count))