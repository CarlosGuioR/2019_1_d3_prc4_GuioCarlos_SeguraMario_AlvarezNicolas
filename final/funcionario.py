#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:53:16 2019

@author: carlos
"""
import sys, re
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget,QTableWidgetItem, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtCore import Qt
import threading
#import time
import os, tempfile

FIFO = '/home/carlos/Escritorio/fifo'


ncuenta=50

def thread_function():  
    bandera=0
    fifo=open(FIFO,'r')
    for line in fifo:
        print(line+"\n")
    fifo.close()
    print("aca\n")
    
    fifo=open(FIFO,'w')
    fifo.write('1')
    fifo.close()
     
    
    fifo=open(FIFO,'r')
    for line1 in fifo:
        print(line1)
    fifo.close()
    print(line)
    
    for a in range(0,len(clientes)):
        if cuentas[a].iddueño ==int(line) and cuentas[a].clave==int(line1):
            bandera=1
            posicion=a
            break
    print(bandera)
    
    if bandera==0:
        a='1'
        fifo=open(FIFO,'w')
        fifo.write(a)
        fifo.close()
        print(a)
    else:
        b='2'
        fifo=open(FIFO,'w')
        fifo.write(b)
        fifo.close()
        print(b)
        
        fifo=open(FIFO,'r')
        for line1 in fifo:
            print(line1+'\n')
        fifo.close()
        print("a")
        
        b='2'
        fifo=open(FIFO,'w')
        fifo.write(b)
        fifo.close()
        print(b)
            
        if int(line1)==1:
            fifo=open(FIFO,'r')
            for line1 in fifo:
                print(line1+'\n')
            fifo.close() 
            cuentas[posicion].balance+=int(line1)
        elif int(line1)==2:
            fifo=open(FIFO,'r')
            for line1 in fifo:
                print(line1+'\n')
            fifo.close() 
            cuentas[posicion].balance-=int(line1)
        
        elif int(line1)==3:
            a=2
            
        elif int(line1)==4:
            a=3
        
        
        
    
    

class Cliente:
    
    def __init__(self,nombre,apellido,edad,ide):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.ide=ide
        self.cuentas=0



class Cuenta:
    
    def __init__(self,numero,estado,clave,balance,iddueño):
        self.numero=numero
        self.estado=estado
        self.clave=clave
        self.balance=balance
        self.iddueño=iddueño
 



       
class Dialogo(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ventana_principal.ui", self)
        self.clientes.clicked.connect(self.abrir)
        self.crear_cliente.clicked.connect(self.abrir_MC)
        self.modificar_datos.clicked.connect(self.Modificar_MC)
        self.cuentas.clicked.connect(self.mcuentas)
        self.crear_cuenta.clicked.connect(self.Crcuenta)
        self.deposito_retiro.clicked.connect(self.dr)
        self.bloquear.clicked.connect(self.bl)
        self.consultar.clicked.connect(self.con)
        
    def abrir(self):
        Mostrar_clientes().exec_()
        
    def abrir_MC(self):
        Crear_cliente().exec_()
    
    def Modificar_MC(self):
        Modificar_cliente().exec_()
  
    def mcuentas(self):
        Mostrar_cuentas().exec_()
        
    def Crcuenta(self):
        Crear_cuenta().exec_()
        
    def dr(self):
        Dep_ret().exec_()
        
    def bl(self):
        Bl_DBL().exec_()
    
    def con(self):
        Ctar().exec_()
        
        
class Ctar(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("consultar.ui", self)
        self.c_cliente.clicked.connect(self.ccliente)
        self.c_cuenta.clicked.connect(self.ccuenta)
        
    def ccliente(self):
        ide=self.idcliente.text()
        for a in range (0,len(clientes)):
            if int(ide)==clientes[a].ide:
                bandera=a
                break
        self.nombre.setText(clientes[bandera].nombre)
        self.apellido.setText(clientes[bandera].apellido)
        self.edad.setText(str(clientes[bandera].edad))
            
    def ccuenta(self):
        cuenta=self.cuenta.text()
        for a in range (0,len(cuentas)):
            if int(cuenta)==cuentas[a].numero:
                bandera=a
                break
        self.saldo.setText(str(cuentas[bandera].balance))
        self.estado.setText(cuentas[bandera].estado)
        self.idd.setText(str(cuentas[bandera].iddueño))
        
        for a in range (0,len(clientes)):
            if cuentas[bandera].iddueño==clientes[a].ide:
                bandera=a
                self.d_du.setText(clientes[a].nombre)
                break
        
        

class Mostrar_cuentas(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Cuentas.ui", self)
        num_cuentas=len(cuentas)
        self.tabla_cuentas.setRowCount(num_cuentas)
        self.tabla_cuentas.setColumnCount(4)
        for i in range(0,num_cuentas):
            item=QTableWidgetItem(str(cuentas[i].numero))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_cuentas.setItem(i,0,item)
            item=QTableWidgetItem(cuentas[i].estado)
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_cuentas.setItem(i,1,item)
            item=QTableWidgetItem(str(cuentas[i].balance))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_cuentas.setItem(i,2,item)
            item=QTableWidgetItem(str(cuentas[i].iddueño))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_cuentas.setItem(i,3,item)



     
class Mostrar_clientes(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Clientes.ui", self)
        num_clientes=len(clientes)
        self.tabla_clientes.setRowCount(num_clientes)
        self.tabla_clientes.setColumnCount(4)
        for i in range(0,num_clientes):
            item=QTableWidgetItem(str(clientes[i].ide))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_clientes.setItem(i,0,item)
            item=QTableWidgetItem(clientes[i].nombre)
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_clientes.setItem(i,1,item)
            item=QTableWidgetItem(clientes[i].apellido)
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_clientes.setItem(i,2,item)
            item=QTableWidgetItem(str(clientes[i].edad))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.tabla_clientes.setItem(i,3,item)
   



         
class Modificar_cliente(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Modificar_cliente.ui", self)
        self.Id_MC.textChanged.connect(self.validar_ide)
        self.validar.clicked.connect(self.Buscar)
        self.Validar_MC.clicked.connect(self.modificar)
        
    def Buscar(self):
        if self.validar_ide():
            ide = self.Id_MC.text()
            bandera=0
            for a in range (0,len(clientes)):
                if int(ide)==clientes[a].ide:
                    QMessageBox.information(self,"Usuario existente", "Usuario existente",QMessageBox.Ok)
                    bandera=1
                    self.Nombre_MC.setEnabled(True)
                    self.Apellido_MC.setEnabled(True)
                    self.Edad_MC.setEnabled(True)
                    self.Validar_MC.setEnabled(True)
                    break
            if bandera==0:
                QMessageBox.warning(self,"Usuario inexistente", "Usuario inexistente",QMessageBox.Ok)
    
    def modificar(self):
        ide = self.Id_MC.text()
        edad = self.Edad_MC.text()
        apellido = self.Apellido_MC.text()
        nombre = self.Nombre_MC.text()
        for a in range (0,len(clientes)):
            if int(ide)==clientes[a].ide:
                bandera=a
                break
        clientes[bandera].edad=int(edad)
        clientes[bandera].nombre=nombre
        clientes[bandera].apellido=apellido
        QMessageBox.information(self,"Usuario Modificado","Usuario Modificado",QMessageBox.Ok)
        self.Nombre_MC.setEnabled(False)
        self.Apellido_MC.setEnabled(False)
        self.Edad_MC.setEnabled(False)
        self.Validar_MC.setEnabled(False)        

        
    def validar_ide(self):
        ide = self.Id_MC.text()
        validar = re.match('^[0-9]+$',ide,re.I)
        if ide == "":
            self.Id_MC.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Id_MC.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Id_MC.setStyleSheet("border: 1px solid green;")
            return True
        
 
class Crear_cuenta(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Crear_cuenta.ui", self)
        self.Id_NC.textChanged.connect(self.validar_ide) 
        self.validar.clicked.connect(self.habilitar)
        self.Crear_CN.clicked.connect(self.crearlo)

        
    def validar_ide(self):
        ide = self.Id_NC.text()
        validar = re.match('^[0-9]+$',ide,re.I)
        if ide == "":
            self.Id_NC.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Id_NC.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Id_NC.setStyleSheet("border: 1px solid green;")
            return True
        
    def habilitar(self):
        if self.validar_ide():
            ide = self.Id_NC.text()
            bandera=0
            for a in range (0,len(clientes)):
                if int(ide)==clientes[a].ide:
                    self.Estado_CN.setEnabled(True)
                    self.Balance_CN.setEnabled(True)
                    self.Clave_CN.setEnabled(True)
                    self.Crear_CN.setEnabled(True)
                    bandera=1
                    break
            if bandera==0:
                QMessageBox.warning(self,"Usuario inexistente", "Usuario inexistente",QMessageBox.Ok)
    
    def crearlo(self):
        #cuenta = self.Ncuenta.text()
        global ncuenta
        cuenta=ncuenta
        ncuenta+=1
        estado = self.Estado_CN.text()
        balance = self.Balance_CN.text()
        clave = self.Clave_CN.text()
        ide = self.Id_NC.text()
        cuentas.append(Cuenta(int(cuenta),estado,int(clave),int(balance),ide))
        self.Estado_CN.setEnabled(False)
        self.Balance_CN.setEnabled(False)
        self.Clave_CN.setEnabled(False)
        self.Crear_CN.setEnabled(False)
         


           
class Crear_cliente(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Crear_cliente.ui", self)  
        self.Nombre_CN.textChanged.connect(self.validar_nombre) 
        self.Apellido_CN.textChanged.connect(self.validar_apellido) 
        self.Edad_CN.textChanged.connect(self.validar_edad)
        self.Id_CN.textChanged.connect(self.validar_ide)
        self.Validar_CN.clicked.connect(self.validar_CN)
        #self.Validar_CN.clicked.connect(self.validar_CN)
        
    def validar_nombre(self):
        nombre = self.Nombre_CN.text()
        validar = re.match('^[a-zA-Z]+$',nombre,re.I)
        if nombre == "":
            self.Nombre_CN.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Nombre_CN.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Nombre_CN.setStyleSheet("border: 1px solid green;")
            return True
        
        
    def validar_apellido(self):
        apellido = self.Apellido_CN.text()
        validar = re.match('^[a-zA-Z]+$',apellido,re.I)
        if apellido == "":
            self.Apellido_CN.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Apellido_CN.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Apellido_CN.setStyleSheet("border: 1px solid green;")
            return True
        
        
    def validar_edad(self):
        edad = self.Edad_CN.text()
        validar = re.match('^[0-9]+$',edad,re.I)
        if edad == "":
            self.Edad_CN.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Edad_CN.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Edad_CN.setStyleSheet("border: 1px solid green;")
            return True
        
    def validar_ide(self):
        ide = self.Id_CN.text()
        validar = re.match('^[0-9]+$',ide,re.I)
        if ide == "":
            self.Id_CN.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.Id_CN.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.Id_CN.setStyleSheet("border: 1px solid green;")
            return True
        
        
    def validar_CN(self):
        if self.validar_nombre() and self.validar_apellido() and self.validar_edad():
            ide = self.Id_CN.text()
            edad = self.Edad_CN.text()
            apellido = self.Apellido_CN.text()
            nombre = self.Nombre_CN.text()
            bandera=0
            for a in range (0,len(clientes)):
                if int(ide)==clientes[a].ide:
                    QMessageBox.warning(self,"Usuario existente", "Usuario existente",QMessageBox.Ok)
                    bandera=1
                    break
            if bandera==0:   
                clientes.append(Cliente(nombre,apellido,int(edad),int(ide)))
                QMessageBox.warning(self,"Usuario creado correctamente", "Usuario creado correctamente",QMessageBox.Ok)
                self.Id_CN.setEnabled(False)
                self.Edad_CN.setEnabled(False)
                self.Apellido_CN.setEnabled(False)
                self.Nombre_CN.setEnabled(False)
        else:
            QMessageBox.warning(self,"Proceso fallido","Datos ingresados incorrectos",QMessageBox.Discard)
    
   
class Dep_ret(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("depositar-retirar.ui", self) 
        self.validar.clicked.connect(self.validar_datos)

        #if self.retirar.isChecked():
            
    def validar_datos(self):
        cuenta = self.id.text()
        clave = self.clave.text()
        monto = self.monto.text()
        bandera=0
        for a in range (0,len(cuentas)):
            if int(cuenta)==cuentas[a].numero and int(clave)==cuentas[a].clave:
                bandera=1
                NC=a
                break
        if bandera==1:
            if self.retirar.isChecked():
                if cuentas[NC].balance>=int(monto):
                    self.balance_actual.setText(str(cuentas[NC].balance))
                    cuentas[NC].balance-= int(monto)
                    self.balance_final.setText(str(cuentas[NC].balance))
                else:
                    self.balance_actual.setText(str(cuentas[NC].balance))
                    self.balance_final.setText("Monto insuficiente")
            elif self.depositar.isChecked():
                self.balance_actual.setText(str(cuentas[NC].balance))
                cuentas[NC].balance+= int(monto)
                self.balance_final.setText(str(cuentas[NC].balance))
        else:
            self.balance_final.setText("Numero de cuenta o clave incorrectos")
            
                    
                
class Bl_DBL(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("bloquear.ui", self) 
        self.validar.clicked.connect(self.validar_datos)
        self.aplicar.clicked.connect(self.ejecutar)
 
    def validar_datos(self):
        cuenta = self.cuenta.text()
        clave = self.clave.text()
        bandera=0
        for a in range (0,len(cuentas)):
            if int(cuenta)==cuentas[a].numero and int(clave)==cuentas[a].clave:
                bandera=1
                self.bloquear.setEnabled(True)
                self.desbloquear.setEnabled(True)
                NC=a
                break
        if bandera==1:
            self.anuncio.setText("Datos correctos, Estado actual:"+cuentas[NC].estado)
        else:
            self.anuncio.setText("Numero de cuenta o clave incorrectos")
    
    def ejecutar(self):
        cuenta = self.cuenta.text()
        clave = self.clave.text()
        for a in range (0,len(cuentas)):
            if int(cuenta)==cuentas[a].numero and int(clave)==cuentas[a].clave:
                NC=a
                break
        if self.bloquear.isChecked():
            cuentas[NC].estado="bloqueada"
            self.anuncio.setText("Operacion exitosa")
            self.bloquear.setEnabled(False)
            self.desbloquear.setEnabled(False)
        elif self.desbloquear.isChecked():
            cuentas[NC].estado="desbloqueada"
            self.anuncio.setText("Operacion exitosa")
            self.bloquear.setEnabled(False)
            self.desbloquear.setEnabled(False)
            
            
        
         
numclientes=0
numcuentas=0
clientes=[]
cuentas=[]

clientes.append(Cliente("carlos","guio",27,12345))
clientes.append(Cliente("diego","rodriguez",22,12346))
clientes.append(Cliente("felipe","rojas",32,12347))

cuentas.append(Cuenta(ncuenta,"desbloqueada",1234,200,12345))
ncuenta+=1
cuentas.append(Cuenta(ncuenta,"desbloqueada",1235,300,12346))
ncuenta+=1
cuentas.append(Cuenta(ncuenta,"desbloqueada",1236,400,12347))
ncuenta+=1

print("aca",clientes[0].ide)


th1 = threading.Thread(target=thread_function)
th1.start()

app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()











    