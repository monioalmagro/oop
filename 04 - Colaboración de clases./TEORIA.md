Normalmente un problema resuelto con la metodología de programación orientada a objetos no interviene una sola clase, sino que hay muchas clases que interactúan y se comunican.

Plantearemos un problema separando las actividades en dos clases.
Problema 1:

Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Cliente y la clase Banco.

Luego debemos definir los atributos y los métodos de cada clase:

Cliente		
    atributos
        nombre
        monto
    métodos
        __init__
        depositar
        extraer
        retornar_monto

Banco
    atributos
        3 Cliente (3 objetos de la clase Cliente)
    métodos
        __init__
        operar
        depositos_totales
Primero hacemos la declaración de la clase Cliente, en el método __init__ inicializamos los atributos nombre con el valor que llega como parámetro y el atributo monto con el valor cero:

class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

Recordemos que en Python para diferenciar un atributo de una variable local o un parámetro le antecedemos la palabra clave self (es decir nombre es el parámetro y self.nombre es el atributo):

        self.nombre=nombre

El método que aumenta el atributo monto es:

    def depositar(self,monto):
        self.monto=self.monto+monto

Y el método que reduce el atributo monto del cliente es:

    def extraer(self,monto):
        self.monto=self.monto-monto

Lo más común para que otro objeto conozca el monto depositado por un cliente es la implementación de un método que lo retorne:

    def retornar_monto(self):
        return self.monto

Para mostrar los datos del cliente tenemos el método:

    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.monto)

La segunda clase de nuestro problema es el Banco. Esta clase define tres atributos de la clase Cliente (la clase Cliente colabora con la clase Banco):

class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")

El método operar realiza una serie de depósitos y extracciones de los clientes:

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

El método que muestra cuanto dinero tiene depositado el banco se resuelve pidiendo a cada cliente que retorne el monto que tiene:

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

En el bloque principal de nuestro programa en Python procedemos a crear un objeto de la clase Banco y llamar a los dos métodos:

# bloque principal        

banco1=Banco()
banco1.operar()
banco1.depositos_totales()

En el bloque principal no se requiere crear objetos de la clase Cliente, esto debido que los clientes son atributos del Banco.