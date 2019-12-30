"""Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en 
el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del 
nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor 
antigüedad en el club. """

class Socio:
	
	def __init__(self):
		self.nombre=input("Ingrese Nombre del Socio: ")
		self.anti=int(input("Ingrese la Antigüedad del Socio: "))

	def imprimir(self):
		print("El Socio: ",self.nombre,"tiene: ",self.anti,"años de antigüedad")	

	def retornar_datos:
		return self.nombre,self.anti

class club:
	
	def __init__(self):
		self.socio1=Socio()
		self.socio2=Socio()
		self.socio3=Socio()

	def mayor_antiguedad(self):
        print("Socio con mayor antiguedad")
        if (self.socio1.retornar_antiguedad()>self.socio2.retornar_antiguedad() and
            self.socio1.retornar_antiguedad()>self.socio3.retornar_antiguedad()):
            self.socio1.imprimir()
        else:
            if self.socio2.retornar_antiguedad()>self.socio3.retornar_antiguedad():
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()
    
#
club=Club() 
club.mayor_antiguedad()            	

