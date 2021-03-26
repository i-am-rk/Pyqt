import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QToolBar, 
    QAction, 
    QStatusBar,
    QCheckBox
)


# tag::MainWindow[]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowTitle("ToolBar")
        self.setWindowTitle("My App")
        
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar") 
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)
        
        button_action = QAction("Your Button", self)
        button_action.setIcon(QIcon("bug.png"))
        button_action.setStatusTip("This is your action")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)
        
        # -------Separator
        toolbar.addSeparator()

        # action2
        button_action2 = QAction(QIcon("bug.png"), "your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.setCheckable(True)
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setShortcut(QKeySequence("Ctrl+o"))
        toolbar.addAction(button_action2)
        

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu("Sub-meu")
        file_submenu.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()