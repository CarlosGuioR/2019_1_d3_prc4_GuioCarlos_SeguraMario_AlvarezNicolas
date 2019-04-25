#include "datos_transaccion.h"
#include "ui_datos_transaccion.h"
#include <QFile>
#include <QTextStream>
#include <string>
#include <fstream>
#include <iostream>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>
#include <QFile>
#include <QTextStream>
int a=0,b=0,c=0,d=0,e=0;

void enviar1(char *x, int a);
int recibir1();

Datos_transaccion::Datos_transaccion(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Datos_transaccion)
{
    ui->setupUi(this);
}

Datos_transaccion::~Datos_transaccion()
{
    delete ui;
}

void Datos_transaccion::on_consignar_clicked()
{
    ui->valor->setEnabled(true);
    ui->saldo->setEnabled(true);
    ui->balance->setEnabled(true);
    ui->estado->setEnabled(true);
    ui->nombre->setEnabled(false);
    ui->apellido->setEnabled(false);
    ui->edad->setEnabled(false);
    a=1;
    b=0;
    c=0;
    d=0;


}

void Datos_transaccion::on_retirar_clicked()
{
    ui->valor->setEnabled(true);
    ui->saldo->setEnabled(true);
    ui->balance->setEnabled(true);
    ui->estado->setEnabled(true);
    ui->nombre->setEnabled(false);
    ui->apellido->setEnabled(false);
    ui->edad->setEnabled(false);
    a=0;
    b=1;
    c=0;
    d=0;
}

void Datos_transaccion::on_modificar_clicked()
{
    ui->valor->setEnabled(false);
    ui->saldo->setEnabled(false);
    ui->balance->setEnabled(false);
    ui->estado->setEnabled(false);
    ui->nombre->setEnabled(true);
    ui->apellido->setEnabled(true);
    ui->edad->setEnabled(true);
    a=0;
    b=0;
    c=1;
    d=0;
}

void Datos_transaccion::on_consultar_clicked()
{
    ui->valor->setEnabled(true);
    ui->saldo->setEnabled(true);
    ui->balance->setEnabled(true);
    ui->estado->setEnabled(true);
    ui->nombre->setEnabled(true);
    ui->apellido->setEnabled(true);
    ui->edad->setEnabled(true);
    a=0;
    b=0;
    c=0;
    d=1;
}

void Datos_transaccion::on_pushButton_clicked()
{
    if(a==1){
        char *a="1";
        enviar1(a,sizeof(char));
        int p=recibir1();
        QString h =ui->valor->text();
        QByteArray c=h.toLocal8Bit();
        char *n=c.data();
        enviar1(n,h.length());

    }else if(b==1){
        char *a="2";
        enviar1(a,sizeof(char));
        int p=recibir1();
        QString h =ui->valor->text();
        QByteArray c=h.toLocal8Bit();
        char *n=c.data();
        enviar1(n,h.length());
    }else if(c==1){
        char *a="3";
        enviar1(a,sizeof(char));
    }else if(d==1){
        char *a="4";
        enviar1(a,sizeof(char));
    }
}

void enviar1(char *x, int a){
    int fd=open("/home/carlos/Escritorio/fifo",O_WRONLY);
    write(fd,x,a);
    close(fd);
}

int recibir1(){
    char x;
    int fd=open("/home/carlos/Escritorio/fifo",O_RDONLY);
    read(fd,&x,sizeof(char));
    x=x-'0';
    close(fd);
    return int(x);
}

