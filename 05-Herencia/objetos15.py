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
	def __init__():
		super().__init__()	
		self.sueldo = float(input("Ingrese sueldo: "))

	def imprimir(self):
		super().imprimir()
		print("sueldo: ",self.sueldo)		




#bloque principal
persona1=Persona()
persona1.imprimir()


