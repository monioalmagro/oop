"""Problema 2:

Implementar una clase llamada Alumno que tenga como atributos 
su nombre y su nota. Definir los métodos para inicializar sus 
atributos, imprimirlos y mostrar un mensaje si está regular 
(nota mayor o igual a 4)

Definir dos objetos de la clase Alumno."""

class Alumno:#--> de esta manera declaramos la clase persona.

	def inicializar(self,nombre,nota):#--> esta es la manera de declarar un método de la clase.
		self.nombre = nombre
		self.nota = nota

	def imprimir(self):
		print("Nombre: ",self.nombre)
		print("Nota: ",self.nota)

	def mostrar_estado(self):
		if self.nota >= 4:
			print("Alumno regular.")
		else:
			print("Libre.")	

#bloque

alumno1 = Alumno()#-->Instanciamos la clase Persona 
alumno1.inicializar("Sinisterra", 10)
alumno1.imprimir()
alumno1.mostrar_estado() 

alumno2 = Alumno()
alumno2.inicializar("Cuartas", 3)
alumno2.imprimir()
alumno2.mostrar_estado() 



