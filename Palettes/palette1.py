"""sys import """
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMainWindow
)
from PyQt5.QtGui import(QPalette, QColor)

class Main(QMainWindow):
    """
    Main class
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel(self)
        label.setText("chck")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        # self.show()

palette = QPalette()
palette.setColor(QPalette.Window, QColor(53,78,98))
app = QApplication(sys.argv)
app.setPalette(palette)
w = Main()
w.show()

app.exec_()
