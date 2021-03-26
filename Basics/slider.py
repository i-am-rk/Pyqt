import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QApplication, QSlider) 



# subclss Qmainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider")

        widget = QSlider(Qt.Horizontal)

        widget.setRange(-10,3)

        widget.setSingleStep(2)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)

        
        self.setCentralWidget(widget)
    

    def value_changed(self, i):
        print(f'Value Changed new value is : {i}')
    
    def slider_position(self, p):
        print(f'Slider position changed new value: {p}')
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start envent loopwi
app.exec_()  