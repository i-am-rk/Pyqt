import sys
from PyQt5.QtWidgets import(
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton
)

        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouse Move Event")
        print(e.pos())
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()