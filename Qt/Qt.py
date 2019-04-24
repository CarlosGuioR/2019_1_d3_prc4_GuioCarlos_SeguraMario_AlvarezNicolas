#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:31:57 2019

@author: carlos
"""

import sys
#import PyQt5 
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont



class Ventana(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        
        uic.loadUi("Qt_banco.ui",self)
        self.setWindowTitle("Qt_Banco")
        #self.showMaximized()
             
        self.setMinimumSize(1366/2,768)#tamañominimo
        self.setMaximumSize(1366/2,768)#tamaño maximo
        self.move(0,0)
        
        qfont=QFont("Arial",8,QFont.Bold)
        self.setFont(qfont)
        
        #self.setStyleSheet("background-color: #000")
        
    def closeEvent(self,event):
        resultado=QMessageBox.question(self,"salir","¿Sguro que quiere salir de la aplicacion?",QMessageBox.Yes|QMessageBox.No)
        if resultado==QMessageBox.Yes:event.accept()
        else:event.ignore()
    
    
app = QApplication(sys.argv)

_ventana=Ventana()

_ventana.show()

app.exec_()