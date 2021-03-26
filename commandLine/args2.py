import sys

from PyQt5.QtWidgets import(
    QApplication,
    QMainWindow,
    QTextEdit
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = QTextEdit()
        # remove script file from args
        if __file__ in sys.argv:
            sys.argv.remove(__file__)

        # open file and read
        if sys.argv:
            filename = sys.argv[0]
            self.open_file(filename)

        self.setCentralWidget(self.editor) 
        self.setWindowTitle("Text Viewer")
    def open_file(self, fn):
        with open(fn, "r") as f:
            text = f.read()

            
        self.editor.setPlainText(text)





app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()