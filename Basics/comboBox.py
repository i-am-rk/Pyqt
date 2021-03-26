import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, QComboBox



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox")
        widget = QComboBox()
        widget.addItems(["One", "Two","Three"])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAtBottom)
        
        self.setCentralWidget(widget)
    def index_changed(self, i):
        print(f'Index Changed! Now index is {i}')

    def text_changed(self, s):
        print(f'Text Changed! Now Text is {s}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loopwi
app.exec_()