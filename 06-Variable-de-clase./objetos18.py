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
			print("Cliente Suspendido.")
		else:
			print("Cliente no suspendido.")	

	def suspender(self):
		Cliente.suspendido.append(self.codigo)

# bloque principal

cliente1=Cliente(1,"Diego")
cliente2=Cliente(2,"Armando")
cliente3=Cliente(3,"Maradona")
cliente4=Cliente(4,"Yaque")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()   
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendido)			