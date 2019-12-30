"""Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. 
También el banco requiere que al final del día calcule la cantidad de dinero 
que hay depositado."""

class Cliente:
	def __init__(self,nombre):
		self.nombre = nombre
		self.monto = 0

	def depositar(self, monto):
		self.monto = self.monto + monto

	def extraer(self,monto)	:
		self.monto = self.monto - monto

	def retornar_monto(self):
		return self.monto

	def imprimir(self):
		print(self.nombre," tiene depositado la suma de : ",self.monto)

			

