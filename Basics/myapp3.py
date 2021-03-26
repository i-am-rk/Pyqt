import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")
        self.setFixedSize(QSize(400, 300))
        
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.button_was_clicked)
        # set the central widget of the widow
        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        self.setWindowTitle("My Oneshot App")
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loop
app.exec_()