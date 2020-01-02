"""Ahora plantearemos otro problema empleando herencia. 
Supongamos que necesitamos implementar dos clases que llamaremos Suma y Resta. 
Cada clase tiene como atributo valor1, valor2 y resultado. Los métodos a 
definir son cargar1 (que inicializa el atributo valor1), carga2 (que 
inicializa el atributo valor2), operar (que en el caso de la clase "Suma" 
suma los dos atributos y en el caso de la clase "Resta" hace la diferencia 
entre valor1 y valor2), y otro método mostrar_resultado.

Si analizamos ambas clases encontramos que muchos atributos y métodos son 
idénticos. En estos casos es bueno definir una clase padre que agrupe dichos 
atributos y responsabilidades comunes.

La relación de herencia que podemos disponer para este problema es:

                                        Operacion

                        Suma                              Resta

Solamente el método operar es distinto para las clases Suma y Resta 
(esto hace que no lo podamos disponer en la clase Operacion en principio), 
luego los mtodos cargar1, cargar2 y mostrar_resultado son idnticos a las 
dos clases, esto hace que podamos disponerlos en la clase Operacion. Lo mismo 
los atributos valor1, valor2 y resultado se definirn en la clase padre 
Operacion.
"""
class Operacion:
	def __init__(self):
		self.valor1=0
		self.valor2=0
		self.resultado=0

	def cargar1(self):
		self.valor1=int(input("Ingrese el primer valor: "))	

	def cargar2(self):
		self.valor2=int(input("Ingrese el segundo valor: "))

	def mostrar_resultado(self):
		print(self.resultado)	

	def operar(self):
		pass	

class Suma(Operacion):

	def operar(self):			
		self.resultado = self.valor1 + self.valor2

class Resta(Operacion):
	
	def operar(self):
		self.resultado = self.valor1 - self.valor2

# bloque princpipal

suma1=Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
print("La suma de los dos valores es")
suma1.mostrar_resultado()

resta1=Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
print("La resta de los valores es:")
resta1.mostrar_resultado()			
"""
En este problema la clase Operación tiene por objetivo agrupar atributos y funcionalidades que se heredarán en otras clases.

La clase Operación inicializa en el metodo __init__ tres atributos:

class Operacion:

    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0

Define dos métodos para cargar los atributos valor1 y valor2:

    def cargar1(self):
        self.valor1=int(input("Ingrese primer valor:"))

    def cargar2(self):
        self.valor2=int(input("Ingrese segundo valor:"))

Definimos un método para imprimir el atributo resultado:

    def mostrar_resultado(self):
        print(self.resultado)

Como la clase Operación se trata de una clase genérica que busca agrupar 
funcionalidades y atributos para otras clases podemos definir un método 
operar pero no podemos implementar ninguna funcionalidad:

    def operar(self):
        pass

En Python para indicar que un método está vacío se utiliza la palabra clave 
"pass".

En el bloque principal de nuestro programa no creamos objetos de la clase 
Operación. La clase Operación tiene sentido que otras clases hereden de esta.


Tanto la clase Suma y Resta heredan de la clase Operación y reescriben el 
método operar con la funcionalidad que le corresponde a cada clase:

class Suma(Operacion):

    def operar(self):
        self.resultado=self.valor1+self.valor2


class Resta(Operacion):

    def operar(self):
        self.resultado=self.valor1-self.valor2

Finalmente en el bloque principal de nuestro programa en Python creamos un objeto de la clase Suma y otro de la clase Resta y llamamos a sus respectivos métodos en un orden lógico:

# bloque princpipal

suma1=Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
print("La suma de los dos valores es")
suma1.mostrar_resultado()

resta1=Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
print("La resta de los valores es:")
resta1.mostrar_resultado()

"""	