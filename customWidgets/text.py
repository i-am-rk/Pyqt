import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QMainWindow,
    QApplication,
    QLabel
) 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_someting()
    
    def draw_someting(self):
        painter = QtGui.QPainter(self.label.pixmap())

        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor("green"))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily("Times")
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, "Hellow, World!")
        painter.end()


app = QApplication(sys.argv) 
w = MainWindow()
w.show()
app.exec_()