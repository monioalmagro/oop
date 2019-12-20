"""Problema 2:

Implementar una clase llamada Alumno que tenga como atributos 
su nombre y su nota. Definir los métodos para inicializar sus 
atributos, imprimirlos y mostrar un mensaje si está regular 
(nota mayor o igual a 4)

Definir dos objetos de la clase Alumno."""

class Alumno:

	def inicializar(self,nombre,nota):
		self.nombre = nombre
		self.nota = nota

	def imprimir(self):
		print("Nombre: ",self.nombre)
		print("Nota: ",self.nota)

	def regular(self):
		if self.nota >= 4:
			print("Alumno regular.")
		else:
			print("Alumno no regular.")	

#bloque


