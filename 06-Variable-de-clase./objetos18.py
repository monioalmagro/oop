""" 
Definir una clase Cliente que almacene un código de cliente y un nombre.
En la clase Cliente definir una variable de clase de tipo lista que almacene 
todos los clientes que tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y el estado que se encuentra 
su cuenta corriente.
"""

class Cliente:
	suspendido = []
	def __init__(self,codigo,nombre):
		self.codigo = codigo
		self.nombre = nombre

	def imprimir(self):
		print(self.codigo)
		print(self.nombre)
		self.esta_suspendido()

	def esta_suspendido(self):
		if self.codigo in Cliente.suspendido :
		