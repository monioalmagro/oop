Hasta ahora todos los problemas planteados hemos llamado a los métodos desde donde definimos un objeto de dicha clase, por ejemplo:

empleado1=Empleado("diego",2000)
empleado1.paga_impuestos()

Utilizamos la sintaxis:

[nombre del objeto].[nombre del método]

Es decir antecedemos al nombre del método el nombre del objeto y el operador punto

Ahora bien que pasa si queremos llamar dentro de la clase a otro método que pertenece a la misma clase, la sintaxis es la siguiente:

self.[nombre del método]

Es importante tener en cuenta que esto solo se puede hacer cuando estamos dentro de la misma clase.