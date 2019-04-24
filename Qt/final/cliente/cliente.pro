#-------------------------------------------------
#
# Project created by QtCreator 2019-04-24T01:26:35
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = cliente
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    datos_transaccion.cpp

HEADERS  += mainwindow.h \
    datos_transaccion.h

FORMS    += mainwindow.ui \
    datos_transaccion.ui
