"""
Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos 
__init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de 
clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos 
minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero. 
"""

class Jugador:
	minutos = 30

	def __init__(self,nombre,puntaje):
		self.nombre = nombre
		self.puntaje = puntaje

	def imprimir(self):
		print("Jugador: ",self.nombre)
		print("Puntaje: ",self.puntaje)
		print("Fin de juego en",Jugador.minutos,"minutos")

	def pasar_tiempo(self):
		Jugador.minutos = Jugador.minutos -1


#BP
jugador1=Jugador("Yaque",50)		
jugador2=Jugador("Figueroa",150)

while Jugador.minutos > 0:
	jugador1.imprimir()
	jugador2.imprimir()
	jugador1.pasar_tiempo()


