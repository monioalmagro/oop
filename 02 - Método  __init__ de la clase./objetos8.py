"""Implementar la clase Operaciones. Se deben cargar dos valores 
enteros por teclado en el método __init__, calcular su suma, resta, 
multiplicación y división, cada una en un método, imprimir dichos 
resultados."""

class Operaciones:

	def __init__(self):
		self.valor1 = int(input("Ingrese un valor: "))
		self.valor2 = int(input("Ingrese otro valor: "))

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

#bloque principal

operacion=Operaciones()
operacion.suma()
operacion.resta()
operacion.multiplicacion()
operacion.division()