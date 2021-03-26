import sys
import random
from PyQt5.QtWidgets import(
    QApplication,
    QMainWindow
)

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        f1 = self.Label_1.font()
        f1.setPointSize(20)
        self.Label_1.setFont(f1)

        f2 = self.Label_2.font()
        f2.setPointSize(20)
        self.Label_2.setFont(f2)

        self.pushButton.pressed.connect(self.update_label)

    def update_label(self):
        n = random.randint(1, 6)
        self.Label_2.setText("%d" %n)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()