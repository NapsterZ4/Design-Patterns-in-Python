# Design-Patterns-in-Python
Most commonly used python design patterns

**1. Abstract Factory:** 

**2. Builder:** *En este patrón, por su naturaleza realiza la construcción de representaciones por diferentes métodos, utilizamos un ejemplo en la compra de una computadora que tiene diferentes características, tomamos en cuenta la cantidad de memoria física (RAM), cantidad de espacio en disco duro y el modelo de tarjeta gráfica. 

**3. Factory Method:** En el primer patrón de encontrado en el código, tenemos un ejemplo sencillo de la fábrica abstracta en el cual tenemos que decidir el nombre y el sexo de una persona a través de métodos de entrada, insertamos el nombre y el género representado por: Masculino="M" y Femenino="F". Se realiza por medio e una clase central y la clase fábrica se encarga de la clasificación de las funciones o instancias creadas por la clase abstracta central. 
Tenemos una clase llamada persona con dos métodos para obtener el nombre y genero que a su vez cuentan con dos subclases que permiten imprimir el mensaje. La clase Fábrica tiene los métodos que tienen los argumentos del nombre y género de la persona. El cliente crea la instancia de la clase fábrica y llama los métodos con los argumentos.

*Referencias:* Verma, R. and Giridhar, C. (2011). Design Patters in Python. 1st ed. Testing Perspective, pp.33 - 34.
