import sys
import time
import traceback
import uuid
import random

from PyQt5.QtCore import(
    QObject,
    QRunnable,
    QThreadPool,
    pyqtSignal,
    pyqtSlot
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class WorkerSignals(QObject):
    """
    Defines the signals avialable from a running worker thread.
    
    Signals:

       progrss:
           int progress complete, from 0-100
    """
    progress = pyqtSignal(str,int)
    finished = pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Store constructor arguments(re-used for processing)
        self.args = args
        self.kwargs = kwargs
        self.job_id = uuid.uuid4().hex
        self.signals = WorkerSignals()
    
    @pyqtSlot()
    def run(self):
        total_n = 100
        #delay = random.randint(1, 99) / 100 # random delay value.
        for n in range(total_n):
            progress_pc = int(100 * float(n+1)/total_n) # progress 0-100% as int
            self.signals.progress.emit(self.job_id, progress_pc)
            time.sleep(0.1)
        
        self.signals.finished.emit(self.job_id)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()

        self.progress = QProgressBar()

        button = QPushButton("START IT UP")
        button.pressed.connect(self.execute)

        self.status = QLabel("0 workers")

        layout.addWidget(self.progress)
        layout.addWidget(button)
        layout.addWidget(self.status)

        w = QWidget()
        w.setLayout(layout)

        # Dict hold the progress of current workers.
        self.worker_progress = {}

        self.setCentralWidget(w)

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
        )
    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        worker.signals.finished.connect(self.cleanup)

        # Execute
        self.threadpool.start(worker)
    
    def cleanup(self, job_id):
        #?print("cleanup")
        if job_id in self.worker_progress:
            del self.worker_progress[job_id]

            # Update the progress bar if we removed a value
            self.refresh_progress()
    
    def update_progress(self, job_id, progress):
        self.worker_progress[job_id] = progress
        print("progress %d" % progress)
        self.refresh_progress()
    
    def calculate_progress(self):
        if not self.worker_progress:
            return 0
        return sum(v for v in self.worker_progress.values()) / len(self.worker_progress)
    def refresh_progress(self):
        # Calculate total progress
        # ?print("refresh progress")
        progress = self.calculate_progress()
        print(self.worker_progress)
        self.progress.setValue(progress)
        self.status.setText("%d workers" % len(self.worker_progress))
    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()