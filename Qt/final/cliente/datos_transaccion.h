#ifndef DATOS_TRANSACCION_H
#define DATOS_TRANSACCION_H

#include <QDialog>

namespace Ui {
class Datos_transaccion;
}

class Datos_transaccion : public QDialog
{
    Q_OBJECT

public:
    explicit Datos_transaccion(QWidget *parent = 0);
    ~Datos_transaccion();

private slots:
    void on_consignar_clicked();

    void on_retirar_clicked();

    void on_modificar_clicked();

    void on_consultar_clicked();

    void on_pushButton_clicked();

private:
    Ui::Datos_transaccion *ui;
};

#endif // DATOS_TRANSACCION_H
