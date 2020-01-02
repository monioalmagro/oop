"""
Plantear una clase Persona que contenga dos atributos: nombre y edad. 
Definir como responsabilidades la carga por teclado y su impresin.
En el bloque principal del programa definir un objeto de la clase persona 
y llamar a sus mtodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona 
y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo 
superior a 3000)
Tambin en el bloque principal del programa crear un objeto de la clase 
Empleado.
"""

class Persona:

	def __init__(self):
		self.nombre = input("Ingrese Nombre: ")
		self.edad = int(input("Ingrese edad: "))

	def imprimir(self):
		print("Nombre: ",self.nombre)
		print("Edad: ",self.edad)

class Empleado(Persona):
	def __init__(self):
		super().__init__()	
		self.sueldo = float(input("Ingrese sueldo: "))

	def imprimir(self):
		super().imprimir()
		print("sueldo: ",self.sueldo)

	def paga_impuestos(self):
		if self.sueldo >= 3000:
			print("El empleado debe pagar impuestos.")
		else:
			print("No paga impuestos.")

#bloque principal
persona1=Persona()
persona1.imprimir()
print("---------------------------------")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
"""
La clase Persona no tiene ninguna sintaxis nueva, como vemos definimos sus métodos __init__ e imprimir, y sus dos atributos nombre y edad:

class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

En el bloque principal creamos un objeto de la clase Persona:

# bloque principal

persona1=Persona()
persona1.imprimir()

La herencia se presenta en la clase Empleado, en la declaración de la clase indicamos entre paréntesis el nombre de la clase de la cual hereda:

class Empleado(Persona):

Con esta sintaxis indicamos que la clase Empleado hereda de la clase Persona. Luego de esto podemos decir que la clase Empleado ya tiene dos atributos heredados que son el nombre y la edad, también hereda las funcionalidades __init__ e imprimir.

La clase Empleado define un nuevo atributo que es el sueldo y tres funcionalidades __init__, imprimir y paga_impuestos.

En el método __init__ de la clase Empleado primero llamamos al método __init__ de la clase padre y luego cargamos el sueldo:

    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo:"))

Mediante la función super() podemos llamar al método __init__ de la clase padre.

Lo mismo sucede con el método imprimir donde primero llamamos al imprimir de la clase padre y luego mostramos el sueldo del empleado:

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

La tercer funcionalidad es:

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")

En el bloque principal de nuestro programa definimos un objeto de la clase Empleado y llamamos a sus funcionalidades:

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
"""


