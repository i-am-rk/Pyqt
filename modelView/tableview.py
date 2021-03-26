import sys
import numpy as np
from datetime import date, datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt





COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0',
'#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row(), index.column()]
            return str(value)
        
        if role == Qt.TextAlignmentRole:
            return Qt.AlignHCenter

    def rowCount(self, index):
        return self._data.shape[0]
    
    def columnCount(self, index):
        return self._data.shape[1]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        data = np.array([
            [1, 9, 2],
            [1, 0, -1],
            [3, 5, 2],
            [3, 3, 2],
            [5, 8, 9],
        ])
        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()