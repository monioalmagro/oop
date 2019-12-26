"""Plantear una clase que administre dos listas de 5 nombres de 
alumnos y sus notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa."""

class Alumnos:
	def __init__(self):
		self.alumnos= []
		self.notas = []
		

	def menu(self):

		while True:
			opcion=int(input("Seleccione\n 1 para cargar\n 2 para listar\n 3 alumnos con notas superiores o iguales a 7\n 4 para salir.  "))
			if opcion == 1:
				self.cargar_alumnos()
			elif opcion == 2:
				self.listar()
			elif opcion == 3:
				self.mayores()
			else:
				break		



	def cargar_alumnos(self):
		for x in range (5):
			print("****************************************")
			nombre = input("Ingrese un nombre: ")
			self.alumnos.append(nombre)
			nota = int(input("Ingrese la nota: "))
			self.notas.append(nota)
			print("****************************************")
		return self.alumnos, self.notas

	def listar(self):
		for x in range(5):
			print("****************************************")
			print("Nombre del alumno: ",self.alumnos[x])
			print("Nota: ",self.notas[x])
		

	def mayores(self):
		for x in range(5):
			if self.notas[x] >= 7:
				print("Alumno con notas mayores o iguales a 7 ")
				print(self.alumnos[x])



alumno=Alumnos()
alumno.menu()		