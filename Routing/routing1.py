import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("click in this widow")
        self.status = self.statusBar()
        self.setFixedSize(QSize(200, 100))
        self.setCentralWidget(self.label)
    
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        print(f'{e.x()} {e.y()}')
    
    def mousePressEvent(self, e):
        route = {
            Qt.LeftButton: self.left_mousePressEvent,
            Qt.MiddleButton: self.middle_mousePressEvent,
        }
        button  = e.button()
        fn = route.get(button)
        if fn:
            fn(e)
    
    def left_mousePressEvent(self, e):
        self.label.setText("mousePressEvent LEFT")
        if e.x() < 100:
            self.status.showMessage("Left click on left")
            self.move(self.x() - 10, self.y())
        else:
            self.status.showMessage("Left click on right")

            self.move(self.x() + 10, self.y())
    
    def middle_mousePressEvent(self, e):
        pass
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()