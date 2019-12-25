# Mazzurque Emiliano
# Programación Orientada a Objetos

"""


"""

#Problema 1:

#Confeccionar una clase que represente un empleado. 
#Definir como atributos su nombre y su sueldo. 
#En el método __init__ cargar los atributos por teclado y 
#luego en otro método imprimir sus datos y por último uno que 
#imprima un mensaje si debe pagar impuestos 
#(si el sueldo supera a 3000) 

class Empleado:

	def __init__ (self):
		self.nombre = input("Ingrese el nombre: ")
		self.sueldo = int(input("Ingrese sueldo: "))

	def imprimir(self):
		print("El nombre del empleado es :",self.nombre)
		print("El sueldo del empleado es :",self.sueldo)

	def paga_impuestos(self):
		if self.sueldo > 3000:
			print("Paga impuestos.")
		else:
			print("No paga impuestos")

empleado=Empleado()
empleado.imprimir()
empleado.paga_impuestos()

			