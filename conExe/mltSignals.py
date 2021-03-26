import sys
import time
import random

from PyQt5.QtCore import (
    QTimer, 
    pyqtSlot, 
    QRunnable,
    QThreadPool,
    pyqtSignal,
    QObject
)
from PyQt5.QtWidgets import(
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    
)

class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    
    Supported signals are:

    finished:
        No data
    
    error:
        `str` Exception string
    
    result:
        `dict` data returned from processing
    """
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict)

class Worker (QRunnable):
    """
    Worker thread

    :@param args: Arguments to make available to the run code
    :param kwargs: Keyword arguments to make available to the run 
    :code
    :
    """

    def __init__(self, iterations=5):
        super().__init__()
        self.signals = WorkerSignals()
        self.iterations = iterations

    @pyqtSlot()
    def run(self):
        """
        Initialize the runner function with passed self.args, 
        self.kwargs
        """
        try:
            for n in range(self.iterations):
                time.sleep(0.01)
                v = 5 / (40 - n)
        except Exception as e:
            self.signals.error.emit(str(e))
        else:
            self.signals.finished.emit()
            self.signals.result.emit({"n": n, "value": v})

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout = QVBoxLayout()

        layout.addWidget(self.l) 
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout) 

        self.setCentralWidget(w)
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
        )

    def oh_no(self):
        worker = Worker(iterations=random.randint(10, 50))
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)
    
    # Worker ouptut function/slot
    def worker_output(self, s):
        print("RESULT", s)
    # worker complete function/slot
    def worker_complete(self):
        print("THREAD COMPLETE!")
    # worker error function/slot
    def worker_error(self, e):
        print("ERROR: %s" % e)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()


