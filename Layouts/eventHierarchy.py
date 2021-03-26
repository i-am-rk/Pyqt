import sys
from PyQt5.QtWidgets import(
    QApplication,
    QMainWindow,
    QMenu,
    QAction
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    def mousePressEvent(self, event):
        print("Mouse Pressed")
        # super().contextMenuEvent(event)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.addAction(QAction("test 4", self))
        context.exec_(e.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()