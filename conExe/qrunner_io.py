import sys

import requests
import re 
from PyQt5.QtCore import(
    QObject,
    QRunnable,
    QThreadPool,
    QTimer,
    pyqtSignal,
    pyqtSlot
)

from PyQt5.QtWidgets import(
    QApplication,
    QLabel,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    data
        `tuple` of (identifier, data)
    """
    data = pyqtSignal(tuple)

class Worker(QRunnable):
    """
    Worker Thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up

    :param id: The id for this worker
    :param url: The url to retrieve
    """
    def __init__(self, id, url, parsers):
        super().__init__()
        self.id = id
        self.url = url
        self.parsers = parsers

        self.signals = WorkerSignals()
    
    @pyqtSlot()
    def run(self):
        r = requests.get(self.url)

        data = {}

        for name, parser in self.parsers.items():
            m = parser.search(r.text)
            if m:
                data[name] = m.group(1).strip()
        
        self.signals.data.emit((self.id, data))

        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.urls = [
            "https://www.learnpyqt.com/",
            "https://www.mfitzp.com/",
            "https://www.google.com",
            "https://www.udemy.com/create-simple-gui-applications-with-python-and-qt/",
        ]

        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        button = QPushButton("GO GET EM!")
        button.pressed.connect(self.execute)

        layout.addWidget(self.text)
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
        )

        self.parsers = {
            # Regular expression parsers, to extract data from the HTML.
            "title": re.compile(r"<title.*?>(.*?)<\/title>", re.M |re.S),
            "h1": re.compile(r"<h1.*?>(.*?)<\/h1>", re.M | re.S),
            "h2": re.compile(r"<h2.*?>(.*?)<\/h2>", re.M | re.S),
        }
    
    def execute(self):
        for n, url in enumerate(self.urls):
            worker = Worker(n, url, self.parsers)
            worker.signals.data.connect(self.display_output)

            # Execute
            self.threadpool.start(worker)
    
    def display_output(self, data):
        id, s = data
        self.text.appendPlainText("WORKER %d: %s" %(id, s))
        #elf.text.appendHtml("WORKER %d: %s" %(id, s))

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
