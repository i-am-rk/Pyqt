import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ListBox")
        widget = QListWidget()
        widget.addItems(["One", "Two","Three"])

        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)

        
        self.setCentralWidget(widget)
    def item_changed(self, i):
        print(f'Item Changed! Now Item is {i}')
 
    def text_changed(self, s):
        print(f'Text Changed! Now Text is {s}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loopwi
app.exec_()