Python nos permite utilizar distintas metodologías de programación. Hemos implementado inicialmente programas utilizando la programación lineal, luego vimos funciones y trabajamos con programación estructurada.

Ahora introduciremos los conceptos de programación orientada a objetos. A partir de este concepto mostraremos en forma sencilla la metodología de Programación Orientada a Objetos.

Se irán introduciendo conceptos de objeto, clase, atributo, método etc. y de todos estos temas se irán planteando problemas resueltos.

Prácticamente todos los lenguajes desarrollados en los últimos 25 años implementan la posibilidad de trabajar con POO (Programación Orientada a Objetos)

El lenguaje Python tiene la característica de permitir programar con las siguientes metodologías:

    Programación Lineal: Es cuando desarrollamos todo el código sin emplear funciones. El código es una secuencia lineal de comando.
    Programación Estructurada: Es cuando planteamos funciones que agrupan actividades a desarrollar y luego dentro del programa llamamos a dichas funciones que pueden estar dentro del mismo archivo (módulo) o en una librería separada.
    Programación Orientada a Objetos: Es cuando planteamos clases y definimos objetos de las mismas (Este es el objetivo de los próximos conceptos, aprender la metodología de programación orientada a objetos y la sintaxis particular de Python para la POO)

Conceptos básicos de Objetos

Un objeto es una entidad independiente con sus propios datos y programación. Las ventanas, menúes, carpetas de archivos pueden ser identificados como objetos; el motor de un auto también es considerado un objeto, en este caso, sus datos (atributos) describen sus características físicas y su programación (métodos) describen el funcionamiento interno y su interrelación con otras partes del automóvil (también objetos).

El concepto renovador de la tecnología de Orientación a Objetos es la suma de funciones a elementos de datos, a esta unión se le llama encapsulamiento.
Por ejemplo, un objeto Auto contiene ruedas, motor, velocidad, color, etc, llamados atributos. Encapsulados con estos datos se encuentran los métodos para arrancar, detenerse, dobla, frenar etc.
La responsabilidad de un objeto auto consiste en realizar las acciones apropiadas y mantener actualizados sus datos internos.
Cuando otra parte del programa (otros objetos) necesitan que el auto realice alguna de estas tareas (por ejemplo, arrancar) le envía un mensaje. A estos objetos que envían mensajes no les interesa la manera en que el objeto auto lleva a cabo sus tareas ni las estructuras de datos que maneja, por ello, están ocultos.
Entonces, un objeto contiene información pública, lo que necesitan los otros objetos para interactuar con él e información privada, interna, lo que necesita el objeto para operar y que es irrelevante para los otros objetos de la aplicación.

******************************************************************************************************************************************************************************************************************

La programación orientada a objetos se basa en la definición de clases; a diferencia de la programación estructurada, que está centrada en las funciones.

Una clase es un molde del que luego se pueden crear múltiples objetos, con similares características.

Un poco más abajo se define una clase Persona y luego se crean dos objetos de dicha clase.

Una clase es una plantilla (molde), que define atributos (lo que conocemos como variables) y métodos (lo que conocemos como funciones).

La clase define los atributos y métodos comunes a los objetos de ese tipo, pero luego, cada objeto tendrá sus propios valores y compartirán las mismas funciones.

Debemos declarar una clase antes de poder crear objetos (instancias) de esa clase. Al crear un objeto de una clase, se dice que se crea una instancia de la clase o un objeto propiamente dicho.