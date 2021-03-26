import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")
        self.button_is_checked = True
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.setFixedSize(QSize(400, 300))
        self.button.setChecked(self.button_is_checked)
        # set the central widget of the widow
        self.setCentralWidget(self.button)
    
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loop
app.exec_()