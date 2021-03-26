import sys
from PyQt5.QtWidgets import(
    QApplication, 
    QMainWindow,
    QPushButton,
    QDialog
)

from my_widgets import(
    CustomDialog
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dailog")
        button.clicked.connect(self.button_pressed)
        self.setCentralWidget(button)

    def button_pressed(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel")


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()