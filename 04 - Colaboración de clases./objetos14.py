"""Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en 
el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del 
nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor 
antigüedad en el club. """

class Socio:
	
	def __init__(self):
		self.nombre=input("Ingrese Nombre del Socio: ")
		self.anti=int(input("Ingrese la Antigüedad del Socio: "))
			