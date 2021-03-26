import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")
        
        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))
        # set the central widget of the widow
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loop
app.exec_()