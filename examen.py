
"""Problema 1:

Implementaremos una clase llamada Persona que tendrá como 
atributo (variable) su nombre y dos métodos (funciones), 
uno de dichos métodos inicializará el atributo nombre y el 
siguiente método mostrará en la pantalla el contenido del mismo.

Definir dos objetos de la clase Persona."""

""" class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)


p=Persona('emiliano')
p.mostrar_nombre()
 """

"""Problema 2:

Implementar una clase llamada Alumno que tenga como atributos 
su nombre y su nota. Definir los métodos para inicializar sus 
atributos, imprimirlos y mostrar un mensaje si está regular 
(nota mayor o igual a 4)

Definir dos objetos de la clase Alumno."""

""" class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(self.nombre)
        print(self.nota)

    def estado(self):
        if self.nota >= 4:
            print('esta regular')
        else:
            print('no esta regular')

alu = Alumno()
alu.inicializar('Emiliano',10)
alu.imprimir()
alu.estado() """


"""Confeccionar una clase que permita carga el nombre y la edad 
de una persona. Mostrar los datos cargados. Imprimir un mensaje 
si es mayor de edad (edad>=18)"""

""" class Persona:

    def inicializar(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print('Nombre: ',self.nombre)
        print('Edad: ',self.edad)
    
    def estado(self):
        if self.edad >= 18:
            print("es mayor de edad.")
        else:
            print("es menor de edad")

per= Persona()
per.inicializar('Emiliano',34)
per.mostrar()
per.estado() """

"""Desarrollar un programa que cargue los lados de un triángulo e 
implemente los siguientes métodos: inicializar los atributos, 
imprimir el valor del lado mayor y otro método que muestre 
si es equilátero o no. El nombre de la clase llamarla Triangulo."""

class Triangulo:

    def inicializar(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def mayor(self):

        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("el lado más grande es : ", self.lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("el lado más grande es : ", self.lado2)
        else:
            print("el lado más grande es : ", self.lado3)
    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print('El triangulo es equilatero')
        else:
            print('El triangulo no es equilatero.')

t = Triangulo()
t.inicializar(132,12,12)
t.mayor()
t.equilatero()

