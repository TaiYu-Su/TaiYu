from PySide2 import QtWidgets, QtGui, QtCore
import sys

from Counter import QCounter

app = QtWidgets.QApplication()

my_widget = QtWidgets.QWidget()
my_widget.show()

# my_count = QCounter()
# my_count.setParent(my_widget)
# my_count.show()
#
# my_count2 = QCounter()
# my_count2.setParent(my_widget)
# my_count2.setGeometry(5, 100, 120, 200)
# my_count2.show()

my_count1 = QCounter()
my_count2 = QCounter()
my_count3 = QCounter()
my_count4 = QCounter()
my_count5 = QCounter()

h_layout = QtWidgets.QVBoxLayout()
h_layout.addWidget(my_count1)
h_layout.addWidget(my_count2)
h_layout.addWidget(my_count3)
h_layout.addWidget(my_count4)
h_layout.addWidget(my_count5)

my_widget.setLayout(h_layout)


sys.exit(app.exec_())
