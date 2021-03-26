import sys

from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QMainWindow

)
from CounterWindow import Ui_MainWindow
# import resources_rc
import resources


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()


app = QApplication(sys.argv)
app.setStyle('Fusion')
w = MainWindow()
app.exec_()



