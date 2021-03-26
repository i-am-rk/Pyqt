import sys

from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QStyle,
    QPushButton
)

class MainWindow(QWidget):
    """Main Window"""
    def __init__(self):
        super().__init__()
        button = QPushButton("push")
        button.setParent(self)
        style = button.style()
        icon = style.standardIcon(QStyle.SP_MessageBoxCritical)
        button.setIcon(icon)






app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()


