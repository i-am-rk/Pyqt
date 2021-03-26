import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QApplication, QSpinBox, QDoubleSpinBox) 



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")
        
        widget = QSpinBox()
        widget.setMaximum(18)
        widget.setMinimum(10)
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)

        self.setCentralWidget(widget) 
        self.setWindowTitle("Line Edit")
    def value_changed(self, v):
        print(v)
    def value_changed_str(self, s):
        print(s)
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loopwi
app.exec_()  