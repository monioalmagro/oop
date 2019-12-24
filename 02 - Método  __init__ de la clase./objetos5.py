# Mazzurque Emiliano
# Programación Orientada a Objetos

"""

El método __init__ es un método especial de una clase en Python. 
El objetivo fundamental del método __init__ es inicializar los 
atributos del objeto que creamos.

Básicamente el método __init__ remplaza al método inicializar que 
habíamos hecho en el concepto anterior.

Las ventajas de implementar el método __init__ en lugar del método 
inicializar son:

1-    El método __init__ es el primer método que se ejecuta cuando se 
    	crea un objeto.
2-    El método __init__ se llama automáticamente. Es decir es 
    	imposible de olvidarse de llamarlo ya que se llamará 
    	automáticamente.
3-    Quien utiliza POO en Python (Programación Orientada a Objetos) 
    	conoce el objetivo de este método.

Otras características del método __init__ son:

    Se ejecuta inmediatamente luego de crear un objeto.
    El método __init__ no puede retornar dato.
    el método __init__ puede recibir parámetros que se utilizan 
    normalmente para inicializar atributos.
    El método __init__ es un método opcional, de todos modos es muy 
    omún declararlo.

Veamos la sintaxis del constructor:

    
def __init__([parámetros]):
        [algoritmo]

Debemos definir un método llamado __init__ (es decir utilizamos 
dos caracteres de subrayado, la palabra init y seguidamente 
otros dos caracteres de subrayado). 
"""

#Problema 1:

#Confeccionar una clase que represente un empleado. 
#Definir como atributos su nombre y su sueldo. 
#En el método __init__ cargar los atributos por teclado y 
#luego en otro método imprimir sus datos y por último uno que 
#imprima un mensaje si debe pagar impuestos 
#(si el sueldo supera a 3000) 

class Empleado:

	def __init__ (self):
		self.nombre = input("Ingrese el nombre: ")
		self.sueldo = int(input("Ingrese sueldo: "))

	def imprimir(self):
		print("El nombre del empleado es :",self.nombre)
		print("El sueldo del empleado es :",self.sueldo)

	def paga_impuestos(self):
		if self.sueldo > 3000:
			print("Paga impuestos.")
		else:
			print("No paga impuestos")

empleado=Empleado()
empleado.imprimir()
empleado.paga_impuestos()

			