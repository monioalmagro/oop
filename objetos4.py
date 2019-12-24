# Mazzurque Emiliano
# Programación Orientada a Objetos

"""Desarrollar un programa que cargue los lados de un triángulo e 
implemente los siguientes métodos: inicializar los atributos, 
imprimir el valor del lado mayor y otro método que muestre 
si es equilátero o no. El nombre de la clase llamarla Triangulo."""

class Triangulo:

	def inicializar(self,lado1,lado2,lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def equilatero(self):
		if self.lado1 == self.lado2 == self.lado3 :
			print ("es un triangulo Equilátero")


triangulo=Triangulo()
triangulo.inicializar(4,4,4)
input("Ingrese una tecla:")
triangulo.equilatero()

