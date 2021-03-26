import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit) 



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line Edit")
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text ....")

        # signals
        widget.returnPressed.connect(self.returnPressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        widget.setInputMask('00-00;_')
        self.setCentralWidget(widget)
    
    def returnPressed(self):
        print("Return Pressed")
        self.centralWidget().setText("BOOM")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
    
    def text_changed(self, s):
        print("Text changed.....")
        print(s)

    def text_edited(self, s):
        print("Text edited........")
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loopwi
app.exec_()  