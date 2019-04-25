#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "datos_transaccion.h"
#include <string>
#include <fstream>
#include <iostream>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>
#include <QFile>
#include <QTextStream>

using namespace std;

void enviar(char *x, int a);
int recibir();

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_validar_clicked()
{


    QString id=ui->id->text();
    //int ide = id.toInt();
    QString sclave=ui->clave->text();
    int clave=sclave.toInt();
    int numero=0;



    mkfifo("/home/carlos/Escritorio/fifo",0666);
    QByteArray c=id.toLocal8Bit();
    QString s1;
    char *b=c.data();
    enviar(b,id.length());
    int j = recibir();
    QByteArray c2=sclave.toLocal8Bit();;
    char *l=c2.data();
    enviar(l,sclave.length());
    int c1= recibir();
//    ui->clave->setText(s1.number(c1));
    if(c1==1){


    }else{
        Datos_transaccion datos;
        datos.setModal(true);
        datos.exec();
    }







}

void enviar(char *x, int a){
    int fd=open("/home/carlos/Escritorio/fifo",O_WRONLY);
    write(fd,x,a);
    close(fd);
}

int recibir(){
    char x;
    int fd=open("/home/carlos/Escritorio/fifo",O_RDONLY);
    read(fd,&x,sizeof(char));
    x=x-'0';
    close(fd);
    return int(x);
}

