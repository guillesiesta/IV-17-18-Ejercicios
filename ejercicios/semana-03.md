#### Ejercicio 1.  Descargar y ejecutar las pruebas de alguno de los proyectos anteriores, y si sale todo bien, hacer un pull request a este proyecto con tests adicionales, si es que faltan (en el momento que se lea este tema).

En este caso he hecho fork al repositorio [tdd-gdg](https://github.com/guillesiesta/tdd-gdg) de JJ y he añadido un par de funciones más y unos tests que las testean.

![Funciones añadidas](imgs/S3-ej1A.png)

![Funciones añadidas](imgs/S3-ej1B.png)

![Funciones añadidas](imgs/S3-ej1C.png)

#### Ejercicio 2. Para la aplicación que se está haciendo, escribir una serie de aserciones y probar que efectivamente no fallan. Añadir tests para una nueva funcionalidad, probar que falla y escribir el código para que no lo haga (vamos, lo que viene siendo TDD).

Primero he añadido una función en la que se introduce el título de una historia y se ha testeado. 

![setTitle](imgs/S3-ej2A.png)


![test_setTitle](imgs/S3-ej2B.png)

![pytest test_setTitle](imgs/S3-ej2C.png)

Después he añadido la funcionalidad de que ese texto no tiene faltas de ortografía. Para lo segundo, he usado un [diccionario de Hunspell con codificación UTF-8 en Español](https://github.com/titoBouzout/Dictionaries). 

![test_setTitle](imgs/S3-ej2D.png)

Pruebo el test con el título que le he puesto y me da error, pues "enanito" no está reconocida en la rae.

![test_setTitle](imgs/S3-ej2E.png)

Corrijo el error. Sustituyo "enanitos" por "enanos", testeo y el test se pasa con éxito.

![test_setTitle](imgs/S3-ej2F.png)


#### Ejercicio 3. Convertir los tests unitarios anteriores con assert a programas de test y ejecutarlos desde mocha, usando descripciones del test y del grupo de test de forma correcta. Si hasta ahora no has subido el código que has venido realizando a GitHub, es el momento de hacerlo, porque lo vas a necesitar un poco más adelante.

Como estoy usando python. Usaré [Behave](http://pythonhosted.org/behave/index.html), que es lo equivalente a Mocha en python. 




