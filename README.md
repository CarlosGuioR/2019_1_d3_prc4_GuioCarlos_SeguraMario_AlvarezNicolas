# Laboratorio 4 
# Sistemas Digitales III

### Presentado por:

- Carlos Fernando Guio Rodriguez
- Mario Alberto Segura Albarracin
- Nicolas Alzarez Casadiego

# Introduccion:
	
En este laboratorio se cean dos interfaces graficas, la primera es a la que ingresa un funcionario del banco para realizar los procedimientos de: consulta de clientes y de cuentas, creacion de un nuevo cliente, creacion de una nueva cuenta, depositar y retirar de una cuenta, bloquear y desbloquear una cuenta, modificar un cliente, y mostrar una lista con todos los clientes y todas las cuentas existentes en el banco.

La otra interfaz grafica es para los usuarios, en esta se puede puede retirar y consignar a la cuenta, puede  verificar los datos y modificar los datos del cliente. Las dos interfaces graficas son hechas con QT. La interfaz grafica del usuario esta ambientada entre QT y c++; la interfaz grafica del funcionario del banco esta ambientada entre QT y python. 

# Desarrollo del programa

## Interfaz grafica del funcionario:

El desarrollo del programa se realizo entre python y QT-Designer, este programa serviria como el servidor ya que en el se guardaron todos los datos tanto del cliente como de las cuentas, para lograr este objetivo se crearon dos clases (Cliente y Cuenta), en la clase Cliente se tiene como propiedades el Nombre, Apellido, Edad e Identificacion. En la clase Cuenta se tiene como propiedades el Numero de la cuenta, Estado, Clave, Balance y la identificacion del dueño.

Se creo un formato en QT del tipo MainWindow en el que se desplegan las siguientes opciones:

### Crear cliente:

Al presionar esta opcion se abre una nueva ventana en al que se le pide al funcionario que ingrese los datos correspondientes al cliente (nombre, apellido, edad, identificacion), se valida que la identificacion se encuentre registrada con los clientes existentes, al pasar esta verificacion se crea un nuevo objeto de la clase CLiente y se guarda en una lista que contiene solo objetos del tipo cliente (list clientes).

### Mostrar clientes:

Al presionar esta opcion se abre una ventana con un QTableWidget en el que se muestran todos los clientes, esta lista se llena con un "for" que va desde 0 hasta len(clientes) para recorrer toda la lista, se accede a los datos de la forma clientes[i].propiedad. De esta manera se llena la tabla con todos los clientes exitentes.

### Mostrar cuentas:

En esta opcion se muestran las cuentas existentes, el metodo de llenado es igual que en el de mostrar clientes, las cuentas estan guardadas en una lista que guarda objetos del tipo de la clase Cuenta y se accede a sus propiedades mediante la indexacion.

### Modificar datos de un cliente:

En esta opcion se valida la existencia de un cliente mediante su identificacion, al tener esta se procede a modificar las propiedades del objero del tipo Cliente que tiene la identificacion buscada. Las propiedades son publicas ya que el acceso a este programa es privado, es decir, solo para funcionarios del banco.

### Crear cuenta:

En esta opcion se valida la existencia de un cliente mediante su identificacion para poder asignarle la nueva cuenta, al verificar que este existe se procede a crear un objeto del tipo de la clase Cuenta que se guarda en la lista cuentas, en esta ventana se pide al funcionario que agrege la clave, el estado y el balance, el numero de cuenta se asigna automaticamente para mantener un control de este conteo.

### Depositar-Retirar

En esta opcion se le pide al funcionario que ingrese el numero de la cuenta, la clave de esta y el monto deseado, la primera verificacion es que el numero de la cuenta exista y que la clave pertenesca a esta cuenta, al verificar esto se procede a verificar el monto en caso de ser un retiro, si el monto de la cuenta es mayor se descuenta este monto y se funaliza el proceso, en caso de ser una consignacion se adiciona este valor al balance de la cuenta.

### Bloquear-Desbloquear

En esta opcion se le pide al funcionario que ingrese el numero de la cuenta y la clave de esta para verificar el estado actual, despues de verificar los datos se habilita la opcion para cambiar el estado de la cuenta entre bloqueada y desbloqueada, este es un limitante para poder retirar, consignar o hacer algun movimiento con la cuenta.

### Consultar

En esta opcion se le pide al funcionario el numero de identificacion del cliente o el numero de cuenta que quiere buscar, en caso de existir se mostraran en pantalla todos los valores relacionados con estos datos.


## Interfaz grafica del usuario:
	
La interfaz grafica del usuario esta ambientada entre C++ y QT-CREATOR, en esta se le pide al usuario que ingrese la identificacion y una clave para validar su identidad, despues de esto se le ofrecen cuatro opciones: Consignar, Retirar, Modificar datos y consultar.

### Consignar-Retirar

En la interfaz grafica se muestra el saldo actual de la cuenta y se le da la opcion de ingresar un monto y de elejir entre consignar y retirar, este valor se envia al servidor y se verifica el monto, n caso de ser posible se procede a realizar la transaccion y mostrar el saldo de la cuenta.

### Modificar datos

En esta opcion se le pide que ingrese los datos que quiere modificar,se envian al servidor y se realiza la operacion. Finalmente se muestra el usuario modificado.

### Consultar cliente 

En esta opcion se me muestra la informacion del cliente y de las cuentas.


## Comunicacion 

El proceso de la interfaz del funcionario y de la interfaz del cliente son diferentes por lo que es necesario compartir la informacion, en este caso se hizo por medio de tuperias FIFO, aunque la sintaxis en cada lenguaje de programacion es diferente, la idea o tematica del mismo es igual, es por esto que se puede realizar la comunicacion entre estos dos lenguajes de programacion.


# Conclusiones:
	
- El banco no tiene limite de clientes inscritos mas alla de la capacidad del computador, al ser manejado con listas en python proveen una facilidad de tratamiento de datos muy grande

- La comunicacion entre QT y python es mas facil (concepto propio del grupo) que la comunicacion entre QT y C++, la forma de escribir las funciones y de realizar las conexiones es mas intuitiva y facil.

- La plataforma QT es una gran herramienta grafica, aunque no exploramos todas las posibilidades que esta ofrece, si se observo que es muy amplia y robusta.

- La comunicacion por tuberias entre estos dos lenguajes de programacion es un poco complicada debido al cambio de sintaxis, sin embargo es muy util y entendible conforme a la experiencia y al uso de esta.


	




















