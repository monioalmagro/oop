Podemos hacer que se ejecute un método definido por nosotros cuando pasamos un objeto a la función print o cuando llamamos a la función str (convertir a string)

¿Qué sucede cuando llamamos a la función print y le pasamos como parámetro un objeto?

class Persona:
    def __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape
 
persona1=Persona("Jose","Rodriguez")
print(persona1)

Nos muestra algo parecido a esto:

<__main__.Persona object at 0x03E99C90>

Python nos permite redefinir el método que se debe ejecutar. Esto se hace definiendo en la clase el método especial __str__

En el ejemplo anterior si queremos que se muestre el nombre y apellido separados por coma cuando llamemos a la función print el código que debemos implementar es el siguiente:

class Persona:
    def __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape

    def __str__(self):
        cadena=self.nombre+","+self.apellido
        return cadena
 
persona1=Persona("Jose","Rodriguez")
print(persona1)

Como vemos debemos implementar el método __str__ y retornar un string, este luego será el que imprime la función print:

    def __str__(self):
        cadena=self.nombre+","+self.apellido
        return cadena

Esta característica definida en Python nos permite crear programas muy legibles y flexibles.

El método __str__ también se ejecuta si llamamos a la función str y pasamos como parámetro un objeto que tiene definido dicho método:

class Persona:
    def __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape

    def __str__(self):
        cadena=self.nombre+","+self.apellido
        return cadena


# bloque principal
 
persona1=Persona("Jose","Rodriguez")
persona2=Persona("Ana","Martinez")
print(str(persona1)+"-"+str(persona2))  # Jose,Rodriguez-Ana,Martinez 
