"""Plantear una clase Operaciones que solicite en el método __init__ 
la carga de dos enteros e inmediatamente muestre su suma, resta, 
multiplicación y división. Hacer cada operación en otro método de 
la clase Operación y llamarlos desde el mismo método __init__"""

class Operaciones:

	def __init__(self):
		self.valor1 = int(input("Ingrese un entero: "))
		self.valor2 = int(input("Ingrese un entero: "))
		self.suma()
		self.resta()
		self.multiplicacion()
		self.division()

	def suma(self):
		suma = self.valor1 + self.valor2
		print("La suma de los valores es ")
		print(suma)

	def resta(self):
		resta = self.valor1 - self.valor2
		print("La resta de los valores es ")
		print(resta)

	def multiplicacion(self):
		multiplicacion = self.valor1 * self.valor2
		print("La multiplicación de los valores es ")
		print(multiplicacion)

	def division(self):
		division = self.valor1 / self.valor2
		print("La división de los valores es ")
		print(division)	

# Bloque principal

operacion = Operaciones()		
			