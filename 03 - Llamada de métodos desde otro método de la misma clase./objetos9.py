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
