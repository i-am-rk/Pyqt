import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        v = QVBoxLayout()
        h = QHBoxLayout()

        for a in range(10):
            button = QPushButton(str(a))
            button.clicked.connect(lambda checked, a=a: self.button_clicked(checked,a))

            h.addWidget(button)
        
        v.addLayout(h)
        self.label = QLabel("")
        v.addWidget(self.label)

        w = QWidget()
        w.setLayout(v)
        self.setCentralWidget(w)
    def button_clicked(self,f,n):
        self.label.setText(str(n))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()