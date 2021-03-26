import sys
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from MainWindow import Ui_MainWindow

tick = QtGui.QImage('tick.png')
t = QtGui.QColor('green')

class TodModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            _,text = self.todos[index.row()]
            return text
        
        if role == Qt.DecorationRole:
            status,_ = self.todos[index.row()]
            if status:
                print(status)
                # return tick
                return t
        
    
    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodModel()
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
    
    def add(self):
        """
        Add an item to our todo list, getting the text from
        the QLineEdit .todoEdit and then clearing it.
        """
        text = self.todoEdit.text()
        text = text.strip() # remove white spaces
        
        if text: # Don't add empty strings
            # access the list via the model
            self.model.todos.append((False, text))
            # trigger refresh.
            self.model.layoutChanged.emit()
            # clear the input
            self.todoEdit.setText("")
            self.save()
    
    def delete(self):
        """
        Delete Item from list, getting index from
        QListView .todoList and deleting it
        """
        # get selected indexs
        indexes = self.todoView.selectedIndexes()
        # remove selected item and refresh
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # clear the selection
            self.todoView.clearSelection()
            self.save()
    
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()
            print("complete")
    
    def load(self):
        try:
            with open('data.json', 'r') as f:
                self.model.todos = json.load(f)
            
        except Exception:
            pass
    
    def save(self):
        with open('data.json', 'w') as f:
            data = json.dump(self.model.todos, f)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()