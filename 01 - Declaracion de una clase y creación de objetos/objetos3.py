# Mazzurque Emiliano
# Programación Orientada a Objetos


"""Confeccionar una clase que permita carga el nombre y la edad 
de una persona. Mostrar los datos cargados. Imprimir un mensaje 
si es mayor de edad (edad>=18)"""

class Persona:

	def inicilizar(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def imprimir(self):
		print("El nombre es :",self.nombre)
		print("Y su edad es : ", self.edad)

	def mostrar_mayor(self):
		if self.edad >= 18:
			print(self.nombre, " es mayor de edad.")
		else:
			print(self.nombre, " es menor de edad.")

#Bloque principal

persona1 = Persona()
persona1.inicilizar("Yaque", 34)
persona1.imprimir()
persona1.mostrar_mayor()

persona1 = Persona()
persona1.inicilizar("Figueroa", 10)
persona1.imprimir()
persona1.mostrar_mayor()


