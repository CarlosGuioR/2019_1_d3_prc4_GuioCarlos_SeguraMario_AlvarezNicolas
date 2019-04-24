import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QWidget, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QRegExp
from PyQt5.QtGui import QPixmap, QImage, QRegExpValidator
import threading

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__(None)
        loadUi('untitled.ui',self)
        self.i = 0
        self.label.setText('HOLA')
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def thread_pipe(self):
        while(1):
            pass

    def pushButton_clicked(self):
        th1 = threading.Thread(target=self.thread_pipe)
        th1.start()
        self.i += 1
        print(f'Hola #{self.i}')

app = QApplication(sys.argv)
ui = mainwindow()
ui.setWindowTitle('Test Python Digital 3')
ui.show()
ret = app.exec_()
sys.exit(ret)