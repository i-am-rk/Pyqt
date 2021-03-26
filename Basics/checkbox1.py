import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.widget = QCheckBox("This is a checkboxA")
        self.widget.setCheckState(Qt.Checked)
        self.widget.setTristate(True)
        self.widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(self.widget)
    def show_state(self, s):
        print(s == Qt.Checked, s)
        print(self.widget.isTristate())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loopwi
app.exec_()