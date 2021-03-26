import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

from my_widgets import Color



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVBoxLayout")
        
        # layout = QVBoxLayout()
        layout = QHBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()