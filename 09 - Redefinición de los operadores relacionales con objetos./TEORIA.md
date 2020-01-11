Python también nos permite redefinir los operadores relacionales cuando planteamos una clase.

Los métodos especiales que podemos implementar son los siguientes:

Para el operador ==:

__eq__(self,objeto2)
Para el operador !=:

__ne__(self,objeto2)

Para el operador >:

__gt__(self,objeto2)

Para el operador >=:

__ge__(self,objeto2)

Para el operador <:

__lt__(self,objeto2)

Para el operador <=:

__le__(self,objeto2)


Es importante recordar que una redefinición de un operador tiene sentido si ayuda y hace más claro nuestro algoritmo.