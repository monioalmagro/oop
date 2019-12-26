"""Desarrollar una clase que represente un Cuadrado y tenga los 
siguientes métodos: inicializar el valor del lado llegando como 
parámetro al método __init__ (definir un atributo llamado lado), 
imprimir su perímetro y su superficie."""

class Cuadrado:
	def __init__(self,lado):
		self.lado = lado

	def perimetro(self):
		perimetro = self.lado * 4
		print("El perímetro del cuadrado es :")
		print(perimetro)

	def superficie(self):
		superficie = self.lado ** 2 
		print("La superficie del cuadrado es :")
		print(superficie)	

cuadrado = Cuadrado(5)
cuadrado.perimetro()		
cuadrado.superficie()