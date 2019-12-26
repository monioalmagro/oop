"""Confeccionar una clase que administre una agenda personal. 
Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa. """

import os

class Agenda:
	def __init__(self):
		self.nombre=[]
		self.telefono=[]
		self.mail=[]

	def menu(self):
		while True:
			
			opcion=int(input("Ingrese su opción:\n 1) cargar contacto\n 2) Listar\n 3) buscar por nombre\n 4) Modificación de mail o teléfono\n 5) Salir. "))
			if opcion == 1:
				self.carga()
			elif opcion == 2:
				self.listar()
			elif opcion == 3:
				self.consulta()
			elif opcion == 4:
				self.modificar()
			else:
				break

	def carga(self):
		os.system("clear")
	 							

	def listar(self):
		os.system("clear")
	 	 

	def consulta(self):
		os.system("clear")
	 	

	def modificar(self):
		os.system("clear")
	 	 	

#bloque principal
agenda=Agenda()
agenda.menu()
